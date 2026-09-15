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

import os
import shutil

from content.site import LANGS, LANG_NAMES, UI, LANDING
from content.legal import PRIVACY, TERMS
from content.blog import POSTS, BLOG_INDEX

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFAULT_LANG = "en"

# Dominio publico del sitio, usado en las etiquetas hreflang. Por defecto apunta
# a la URL que da GitHub Pages; si se configura un dominio propio hay que
# cambiarlo aqui y volver a generar, porque un hreflang que apunta a un dominio
# que no existe es peor que no ponerlo.
SITE_URL = "https://snapgate.app"


def shell(lang, *, title, description, body, path_depth=1, active=""):
    """Envoltura comun: cabecera, contenido y pie."""
    ui = UI[lang]
    up = "../" * path_depth
    year = 2026

    def nav_link(key, href, label, extra=""):
        cls = ' class="' + extra + '"' if extra else ""
        return f'<a href="{href}"{cls}>{label}</a>'

    langs = "".join(
        f'<li><a href="{"../" * path_depth}{code}/" hreflang="{code}">{LANG_NAMES[code]}</a></li>'
        for code in LANGS
    )

    alternates = "".join(
        f'<link rel="alternate" hreflang="{code}" href="{SITE_URL}/{code}/">'
        for code in LANGS
    )

    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:image" content="{up}assets/icon.png">
<meta name="theme-color" content="#16a34a">
<link rel="icon" href="{up}assets/icon.png">
<link rel="stylesheet" href="{up}assets/style.css">
{alternates}
</head>
<body>

<header class="site">
  <div class="wrap">
    <a class="brand" href="{up}{lang}/">
      <img src="{up}assets/icon.png" alt="">
      <span>Snapgate</span>
    </a>
    <nav class="main">
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

{body}

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
      <a href="https://github.com/jfjalburquerque/snapgate">GitHub</a>
    </div>
  </div>
</footer>

</body>
</html>
"""


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

    body = f"""
<div class="wrap hero">
  <img class="app-icon" src="../assets/icon.png" alt="Snapgate">
  <h1>{c["h1"]}</h1>
  <p class="lede">{c["lede"]}</p>
  <div class="cta">
    <a class="btn" href="#how">{c["cta_primary"]}</a>
    <a class="btn ghost" href="blog/">{c["cta_secondary"]}</a>
  </div>
  <p class="note">{c["note"]}</p>
</div>

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
    return shell(lang, title=c["title"], description=c["description"], body=body)


def page_html(lang, doc, depth=1):
    body = f"""
<div class="wrap page prose">
  <h1>{doc["h1"]}</h1>
  <p class="meta">{doc["meta"]}</p>
  {doc["body"]}
</div>
"""
    return shell(lang, title=doc["title"], description=doc["description"],
                 body=body, path_depth=depth)


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
    return shell(lang, title=c["title"], description=c["lede"], body=body, path_depth=2)


def post_html(lang, post):
    t = post["langs"][lang]
    body = f"""
<div class="wrap page prose">
  <h1>{t["title"]}</h1>
  <p class="meta">{t["date_label"]}</p>
  {t["body"]}
</div>
"""
    return shell(lang, title=t["title"] + " · Snapgate", description=t["excerpt"],
                 body=body, path_depth=2)


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
        write(os.path.join(base, "privacy.html"), page_html(lang, PRIVACY[lang]))
        write(os.path.join(base, "terms.html"), page_html(lang, TERMS[lang]))
        write(os.path.join(base, "blog", "index.html"), blog_index_html(lang))
        written += 4

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
    write(os.path.join(ROOT, "index.html"), f"""<!doctype html>
<html lang="{DEFAULT_LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Snapgate</title>
<meta name="description" content="Decide which photos reach your cloud.">
<link rel="icon" href="assets/icon.png">
<link rel="stylesheet" href="assets/style.css">
<script>
  var supported = [{supported}];
  var want = (navigator.language || "{DEFAULT_LANG}").slice(0, 2).toLowerCase();
  var go = supported.indexOf(want) >= 0 ? want : "{DEFAULT_LANG}";
  location.replace(go + "/" + location.hash);
</script>
</head>
<body>
<div class="wrap page prose">
  <h1>Snapgate</h1>
  <p>Choose your language:</p>
  <ul>{options}</ul>
</div>
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
    print(f"{written} paginas generadas en {len(LANGS)} idiomas")


if __name__ == "__main__":
    main()
