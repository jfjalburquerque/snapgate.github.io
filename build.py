#!/usr/bin/env python3
"""
Generador del sitio de Snapgate.

Sitio estatico puro para GitHub Pages: sin framework, sin dependencias y sin
nada que se descargue de terceros. El contenido de cada idioma vive en
`content/` y aqui solo estan las plantillas y el recorrido de ficheros.

    python3 build.py

Escribe un directorio por idioma en la raiz del repositorio, que es lo que
Pages publica directamente desde la rama principal.
"""

import json
import os
import shutil

from content.site import LANGS, LANG_NAMES, UI, LANDING
from content.legal import PRIVACY, TERMS
from content.blog import POSTS, BLOG_INDEX
from content.press import PRESS, COVERAGE

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_LANG = "en"

# Dominio publico del sitio, usado en las etiquetas hreflang. Por defecto apunta
# a la URL que da GitHub Pages; si se configura un dominio propio hay que
# cambiarlo aqui y volver a generar, porque un hreflang que apunta a un dominio
# que no existe es peor que no ponerlo.
SITE_URL = "https://snapgate.app"

# Descripcion de la raiz, que solo ven quien no ejecuta JavaScript y los buscadores.
ROOT_DESCRIPTION = ("Snapgate is an Android app that asks you, photo by photo and "
                    "right from the notification, which pictures Google Photos "
                    "should back up.")

# Firma del desarrollador: pie, autoría de los artículos y datos estructurados.
AUTHOR = "jfjalburquerque"

# Locale de Open Graph por idioma.
OG_LOCALES = {"es": "es_ES", "en": "en_US", "pt": "pt_PT", "fr": "fr_FR",
              "de": "de_DE", "it": "it_IT"}

# Paginas publicadas, para el sitemap: ruta -> {idioma: ruta equivalente}.
SITEMAP = {}


def url(path):
    """URL absoluta de una ruta relativa a la raiz; index.html se omite."""
    if path.endswith("index.html"):
        path = path[: -len("index.html")]
    return f"{SITE_URL}/{path}"


def hreflangs(alts):
    """Pares (hreflang, url) de una pagina, con x-default.

    Las portadas apuntan x-default a la raiz, que es el selector de idioma; el
    resto, a la version inglesa si existe.
    """
    pairs = [(code, url(alts[code])) for code in LANGS if code in alts]
    if all(p == f"{c}/index.html" for c, p in alts.items()):
        pairs.append(("x-default", url("index.html")))
    else:
        pairs.append(("x-default", url(alts.get(DEFAULT_LANG, next(iter(alts.values()))))))
    return pairs


def hreflang_links(alts):
    return "".join(
        f'<link rel="alternate" hreflang="{code}" href="{href}">'
        for code, href in hreflangs(alts)
    )


def same_page(name):
    """Equivalentes de una pagina que existe en todos los idiomas."""
    return {code: f"{code}/{name}" for code in LANGS}


def person():
    return {"@type": "Person", "name": AUTHOR}


def breadcrumbs(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": url(path)}
            for i, (name, path) in enumerate(items, 1)
        ],
    }


def jsonld_script(data):
    # "</" se escapa para que ningun texto pueda cerrar la etiqueta script.
    text = json.dumps(data, ensure_ascii=False, indent=1).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{text}\n</script>'


def shell(lang, *, title, description, body, path, alts, path_depth=1,
          og_type="website", jsonld=None, index=True):
    """Envoltura comun: cabecera, contenido y pie.

    `path` es la ruta de la pagina desde la raiz y `alts` sus equivalentes en
    cada idioma en que existe ({idioma: ruta}); de ahi salen el canonical, los
    hreflang y el selector de idioma. Las paginas con `index=False` llevan
    noindex y no entran en el sitemap.
    """
    ui = UI[lang]
    up = "../" * path_depth
    year = 2026
    if index:
        SITEMAP[path] = alts

    def nav_link(key, href, label, extra=""):
        cls = ' class="' + extra + '"' if extra else ""
        return f'<a href="{href}"{cls}>{label}</a>'

    # El selector lleva a la misma pagina en el otro idioma si existe, y a la
    # portada de ese idioma si no.
    langs = "".join(
        f'<li><a href="{up}{alts.get(code, code + "/").removesuffix("index.html")}" '
        f'hreflang="{code}">{LANG_NAMES[code]}</a></li>'
        for code in LANGS
    )

    alternates = hreflang_links(alts)
    robots = "" if index else '\n<meta name="robots" content="noindex, follow">'
    ld = "\n" + jsonld_script(jsonld) if jsonld else ""

    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">{robots}
<link rel="canonical" href="{url(path)}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{url(path)}">
<meta property="og:locale" content="{OG_LOCALES[lang]}">
<meta property="og:site_name" content="Snapgate">
<meta property="og:image" content="{SITE_URL}/assets/brand/og/{lang}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#15803d">
<link rel="icon" href="{up}assets/brand/mark-512.png">
<link rel="stylesheet" href="{up}assets/style.css">
{alternates}{ld}
</head>
<body>

<header class="site">
  <div class="wrap">
    <a class="brand" href="{up}{lang}/">
      <img src="{up}assets/brand/mark-512.png" alt="">
      <span>Snapgate</span>
    </a>
    <nav class="main" aria-label="{ui["nav_label"]}">
      {nav_link("features", up + lang + "/#how", ui["nav_how"], "hide-sm")}
      {nav_link("privacy", up + lang + "/privacy.html", ui["nav_privacy"])}
      {nav_link("blog", up + lang + "/blog/", ui["nav_blog"])}
      <details class="lang">
        <summary>{LANG_NAMES[lang]}</summary>
        <ul>{langs}</ul>
      </details>
    </nav>
  </div>
</header>

<main>
{body}
</main>

<footer class="site">
  <div class="wrap cols">
    <div>
      <strong style="color:var(--ink-soft)">Snapgate</strong> · {ui["footer_tagline"]}<br>
      <span>© {year}. {ui["footer_rights"]}</span>
    </div>
    <div class="links">
      <a href="{up}{lang}/privacy.html">{ui["nav_privacy"]}</a>
      <a href="{up}{lang}/terms.html">{ui["nav_terms"]}</a>
      <a href="{up}{lang}/blog/">{ui["nav_blog"]}</a>
      <a href="{up}{lang}/press.html">{ui["nav_press"]}</a>
    </div>
  </div>
</footer>

</body>
</html>
"""


PLAY_URL = "https://play.google.com/store/apps/details?id=com.snapgate.app"

# Enlace, no reproductor incrustado: el de YouTube carga cookies y rastreadores
# de Google al abrir la pagina, y la web promete no descargar nada de terceros.
FEATURED_VIDEO = "https://www.youtube.com/watch?v=TYNzg59ke30&amp;t=61s"

# Mismo orden que en Play. Los textos alternativos viven en content/site.py.
SHOT_NAMES = ["01-notif", "02-selection", "03-features", "04-onb1"]


def landing_html(lang):
    c = LANDING[lang]
    features = "".join(
        f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in c["features"]
    )
    steps = "".join(
        f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in c["steps"]
    )
    faq = "".join(
        f"<h3>{q}</h3><p>{a}</p>" for q, a in c["faq"]
    )
    # Las capturas de Play ya llevan su titular en el idioma de la pagina; las
    # que se sirven aqui son las copias ligeras de tools/web_shots.py.
    shots = "".join(
        f'<img src="../assets/web/shots/{lang}/{name}.webp" width="540" height="960" '
        f'loading="lazy" alt="{alt}">'
        for name, alt in zip(SHOT_NAMES, c["shots"])
    )

    # HowToMen ya tiene su sello; el resto de la cobertura va en una sola linea
    # discreta debajo, con el nombre corto de cada medio.
    also = " · ".join(
        f'<a href="{url}" rel="noopener">{short}</a>'
        for url, _, _, short in COVERAGE if short != "HowToMen"
    )

    body = f"""
<div class="wrap hero">
  <img class="app-icon" src="../assets/brand/mark-512.png" alt="Snapgate">
  <h1>{c["h1"]}</h1>
  <p class="lede">{c["lede"]}</p>
  <div class="cta">
    <a class="btn" href="{PLAY_URL}" rel="noopener">{c["cta_play"]}</a>
    <a class="btn ghost" href="#how">{c["cta_primary"]}</a>
    <a class="btn ghost" href="blog/">{c["cta_secondary"]}</a>
  </div>
  <p class="note">{c["note"]}</p>
  <a class="featured" href="{FEATURED_VIDEO}" rel="noopener">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>
    <span><strong>{c["featured_label"]}</strong><br>{c["featured_text"]}</span>
  </a>
  <p class="also">{c["also_label"]}: {also}</p>
</div>

<section id="screens">
  <div class="wrap">
    <h2>{c["shots_h2"]}</h2>
    <div class="shots">{shots}</div>
  </div>
</section>

<section id="problem">
  <div class="wrap">
    <h2>{c["problem_h2"]}</h2>
    <p class="sub">{c["problem_sub"]}</p>
    <div class="callout">{c["problem_callout"]}</div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <h2>{c["steps_h2"]}</h2>
    <p class="sub">{c["steps_sub"]}</p>
    <ol class="steps">{steps}</ol>
  </div>
</section>

<section id="features">
  <div class="wrap">
    <h2>{c["features_h2"]}</h2>
    <p class="sub">{c["features_sub"]}</p>
    <div class="grid">{features}</div>
  </div>
</section>

<section id="privacy">
  <div class="wrap">
    <h2>{c["privacy_h2"]}</h2>
    <div class="prose">{c["privacy_body"]}</div>
  </div>
</section>

<section id="faq">
  <div class="wrap prose">
    <h2>{c["faq_h2"]}</h2>
    {faq}
  </div>
</section>
"""
    path = f"{lang}/index.html"
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}/#website",
                "url": f"{SITE_URL}/",
                "name": "Snapgate",
                "inLanguage": LANGS,
                "publisher": {"@id": f"{SITE_URL}/#org"},
            },
            {
                "@type": "Organization",
                "@id": f"{SITE_URL}/#org",
                "name": "Snapgate",
                "url": f"{SITE_URL}/",
                "logo": f"{SITE_URL}/assets/brand/mark-512.png",
                "founder": person(),
                "sameAs": [PLAY_URL],
            },
            {
                "@type": "MobileApplication",
                "@id": f"{SITE_URL}/#app",
                "name": "Snapgate",
                "description": c["description"],
                "url": url(path),
                "operatingSystem": "Android 11+",
                "applicationCategory": "MultimediaApplication",
                "inLanguage": LANGS,
                "installUrl": PLAY_URL,
                "downloadUrl": PLAY_URL,
                "image": f"{SITE_URL}/assets/brand/mark-512.png",
                "screenshot": [
                    f"{SITE_URL}/assets/web/shots/{lang}/{name}.webp" for name in SHOT_NAMES
                ],
                # Prueba gratuita de 14 dias y despues pago unico (content/press.py).
                "offers": {"@type": "Offer", "price": "4.99", "priceCurrency": "EUR"},
                "author": person(),
                "publisher": {"@id": f"{SITE_URL}/#org"},
            },
        ],
    }
    return shell(lang, title=c["title"], description=c["description"], body=body,
                 path=path, alts=same_page("index.html"), jsonld=data)


def page_html(lang, doc, name, depth=1):
    body = f"""
<div class="wrap page prose">
  <h1>{doc["h1"]}</h1>
  <p class="meta">{doc["meta"]}</p>
  {doc["body"]}
</div>
"""
    path = f"{lang}/{name}"
    data = {"@context": "https://schema.org", **breadcrumbs(
        [("Snapgate", f"{lang}/index.html"), (doc["h1"], path)])}
    return shell(lang, title=doc["title"], description=doc["description"],
                 body=body, path_depth=depth, path=path, alts=same_page(name),
                 jsonld=data)


def blog_index_html(lang):
    c = BLOG_INDEX[lang]
    posts = [p for p in POSTS if lang in p["langs"]]
    items = ""
    for post in posts:
        t = post["langs"][lang]
        items += (
            f'<li><h2><a href="{post["slug"]}.html">{t["title"]}</a></h2>'
            f'<time datetime="{post["date"]}">{t["date_label"]}</time>'
            f'<p>{t["excerpt"]}</p></li>'
        )
    fallback = "" if posts else f'<p class="sub">{c["empty"]}</p>'
    body = f"""
<div class="wrap page">
  <h1>{c["h1"]}</h1>
  <p class="meta">{c["lede"]}</p>
  {fallback}
  <ul class="posts">{items}</ul>
</div>
"""
    # Un indice sin articulos en su idioma es contenido escaso: se publica para
    # que el menu no lleve a un 404, pero sin indexar.
    path = f"{lang}/blog/index.html"
    data = {"@context": "https://schema.org", **breadcrumbs(
        [("Snapgate", f"{lang}/index.html"), (c["h1"], path)])}
    return shell(lang, title=c["title"], description=c["lede"], body=body,
                 path_depth=2, path=path, alts=blog_alts(), jsonld=data,
                 index=bool(posts))


def blog_alts():
    """Idiomas con algun articulo: son los unicos cuyo indice se indexa."""
    langs = {code for post in POSTS for code in post["langs"]}
    return {code: f"{code}/blog/index.html" for code in LANGS if code in langs}


def post_html(lang, post):
    t = post["langs"][lang]
    body = f"""
<div class="wrap page prose">
  <h1>{t["title"]}</h1>
  <p class="meta"><time datetime="{post["date"]}">{t["date_label"]}</time> · {AUTHOR}</p>
  {t["body"]}
</div>
"""
    path = f"{lang}/blog/{post['slug']}.html"
    alts = {code: f"{code}/blog/{post['slug']}.html" for code in post["langs"]}
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "headline": t["title"],
                "description": t["excerpt"],
                "datePublished": post["date"],
                "inLanguage": lang,
                "url": url(path),
                "mainEntityOfPage": url(path),
                "image": f"{SITE_URL}/assets/brand/og/{lang}.png",
                "author": person(),
                "publisher": {
                    "@type": "Organization",
                    "name": "Snapgate",
                    "logo": f"{SITE_URL}/assets/brand/mark-512.png",
                },
            },
            breadcrumbs([
                ("Snapgate", f"{lang}/index.html"),
                (BLOG_INDEX[lang]["h1"], f"{lang}/blog/index.html"),
                (t["title"], path),
            ]),
        ],
    }
    return shell(lang, title=t["title"] + " · Snapgate", description=t["excerpt"],
                 body=body, path_depth=2, path=path, alts=alts,
                 og_type="article", jsonld=data)


def sitemap_xml():
    """Sitemap con las alternativas de idioma de cada URL."""
    entries = ""
    for path in sorted(SITEMAP):
        links = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{code}" href="{href}"/>'
            for code, href in hreflangs(SITEMAP[path])
        )
        entries += f"  <url>\n    <loc>{url(path)}</loc>{links}\n  </url>\n"
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{entries}</urlset>\n"
    )


def write(path, html):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    written = 0
    for lang in LANGS:
        base = os.path.join(ROOT, lang)
        shutil.rmtree(base, ignore_errors=True)

        write(os.path.join(base, "index.html"), landing_html(lang))
        write(os.path.join(base, "privacy.html"),
              page_html(lang, PRIVACY[lang], "privacy.html"))
        write(os.path.join(base, "terms.html"), page_html(lang, TERMS[lang], "terms.html"))
        write(os.path.join(base, "press.html"), page_html(lang, PRESS[lang], "press.html"))
        write(os.path.join(base, "blog", "index.html"), blog_index_html(lang))
        written += 5

        for post in POSTS:
            if lang in post["langs"]:
                write(os.path.join(base, "blog", post["slug"] + ".html"),
                      post_html(lang, post))
                written += 1

    # Raiz: reparte segun el idioma del navegador. Se hace en cliente porque
    # Pages no permite negociacion de contenido en el servidor.
    options = "".join(
        f'<li><a href="{code}/">{LANG_NAMES[code]}</a></li>' for code in LANGS
    )
    supported = ",".join(f'"{c}"' for c in LANGS)
    SITEMAP["index.html"] = same_page("index.html")
    write(os.path.join(ROOT, "index.html"), f"""<!doctype html>
<html lang="{DEFAULT_LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Snapgate · Choose which photos Google Photos backs up</title>
<script>
  var supported = [{supported}];
  var want = (navigator.language || "{DEFAULT_LANG}").slice(0, 2).toLowerCase();
  var go = supported.indexOf(want) >= 0 ? want : "{DEFAULT_LANG}";
  location.replace(go + "/" + location.hash);
</script>
<noscript><meta http-equiv="refresh" content="0; url={DEFAULT_LANG}/"></noscript>
<meta name="description" content="{ROOT_DESCRIPTION}">
<link rel="canonical" href="{SITE_URL}/">
<meta property="og:title" content="Snapgate · Choose which photos Google Photos backs up">
<meta property="og:description" content="{ROOT_DESCRIPTION}">
<meta property="og:url" content="{SITE_URL}/">
<meta property="og:image" content="{SITE_URL}/assets/brand/og/{DEFAULT_LANG}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{hreflang_links(same_page("index.html"))}
<link rel="icon" href="assets/icon.png">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<main class="wrap page prose">
  <h1>Snapgate</h1>
  <p>{ROOT_DESCRIPTION}</p>
  <p>Choose your language:</p>
  <ul>{options}</ul>
</main>
</body>
</html>
""")
    written += 1

    # 404 en la raiz, que es lo que sirve Pages ante una ruta desconocida.
    write(os.path.join(ROOT, "404.html"), f"""<!doctype html>
<html lang="{DEFAULT_LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Not found · Snapgate</title>
<link rel="icon" href="/assets/icon.png">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<div class="wrap page prose">
  <h1>404</h1>
  <p>That page does not exist. <a href="/">Back to Snapgate</a>.</p>
</div>
</body>
</html>
""")
    written += 1

    write(os.path.join(ROOT, "robots.txt"),
          f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    write(os.path.join(ROOT, "sitemap.xml"), sitemap_xml())
    print(f"{written} paginas generadas en {len(LANGS)} idiomas")


if __name__ == "__main__":
    main()
