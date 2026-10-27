#!/usr/bin/env python3
"""
Genera la marca de Snapgate: logotipo horizontal y gráfico de cabecera de Play.

    python3 tools/branding.py

Tipografía Inter (SIL Open Font License), en `assets/fonts`. Se usa la variable
seleccionando instancias con nombre, para no arrastrar un fichero por peso.
"""

import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(ROOT, "assets", "fonts", "Inter.ttf")
ICON = os.path.join(ROOT, "assets", "icon.png")
OUT = os.path.join(ROOT, "assets", "brand")

INK = (28, 32, 39)
INK_LIGHT = (232, 235, 240)
SOFT = (91, 100, 114)
SOFT_DARK = (150, 158, 170)
GREEN = (22, 163, 74)
GREEN_LIGHT = (52, 209, 124)


def face(instance, size):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_name(instance)
    return f


def text_size(draw, text, font, tracking=0):
    """PIL no ajusta el interletrado, asi que se mide sumando avances."""
    if not tracking:
        box = draw.textbbox((0, 0), text, font=font)
        return box[2] - box[0], box[3] - box[1]
    width = 0
    for ch in text:
        width += draw.textlength(ch, font=font) + tracking
    return width - tracking, draw.textbbox((0, 0), text, font=font)[3]


def draw_tracked(draw, xy, text, font, fill, tracking=0):
    """Dibuja letra a letra para poder cerrar el interletrado."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking


# Recorte del dibujo dentro del PNG de origen, sin azulejo ni sombra.
GLYPH_BOX = (32, 37, 176, 168)
TILE_BG = (252, 253, 254, 255)


def icon_at(size, shadow=True):
    """Compone el icono como lo hace Android: fondo liso mas dibujo.

    Reutilizar el PNG original dejaba visible su propio cuadrado redondeado
    dentro del recorte, con la sombra formando un marco fantasma. Componerlo
    aqui garantiza ademas que la marca y el icono instalado sean identicos.
    """
    glyph = Image.open(ICON).convert("RGBA").crop(GLYPH_BOX)
    tile = Image.new("RGBA", (size, size), TILE_BG)

    target = int(size * 0.58)
    gw, gh = glyph.size
    k = target / max(gw, gh)
    g = glyph.resize((max(1, int(gw * k)), max(1, int(gh * k))), Image.LANCZOS)
    tile.paste(g, ((size - g.width) // 2, (size - g.height) // 2), g)

    tile = rounded(tile)
    if not shadow:
        return tile

    # Sombra propia, suave y por debajo: la del PNG original iba pintada y no
    # encajaba con ningun fondo que no fuera blanco.
    pad = int(size * 0.10)
    out = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    blur = Image.new("RGBA", out.size, (0, 0, 0, 0))
    ImageDraw.Draw(blur).rounded_rectangle(
        (pad, pad + int(size * 0.035), pad + size, pad + size + int(size * 0.035)),
        radius=int(size * 0.225), fill=(20, 26, 34, 46),
    )
    out = Image.alpha_composite(out, blur.filter(ImageFilter.GaussianBlur(size * 0.045)))
    out.paste(tile, (pad, pad), tile)
    return out


def rounded(img, radius_ratio=0.225):
    """Recorta con la misma curva que usan los lanzadores, para que el logotipo
    y el icono instalado se reconozcan como la misma cosa."""
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, img.size[0] - 1, img.size[1] - 1),
        radius=int(img.size[0] * radius_ratio), fill=255,
    )
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def horizontal(dark=False, mark_size=200, pad=40):
    """Logotipo horizontal: icono y palabra. 'gate' en verde, que es donde esta
    la idea del producto — el portero."""
    wordmark = face("SemiBold", 132)
    tracking = -3.2

    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    w_snap = sum(tmp.textlength(c, font=wordmark) + tracking for c in "Snap")
    w_gate = sum(tmp.textlength(c, font=wordmark) + tracking for c in "gate")
    text_w = w_snap + w_gate

    gap = 34
    W = int(pad + mark_size + gap + text_w + pad)
    H = int(mark_size + pad * 2)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))

    mark = icon_at(mark_size)
    canvas.paste(mark, (pad - int(mark_size * 0.10), pad - int(mark_size * 0.10)), mark)

    d = ImageDraw.Draw(canvas)
    baseline = pad + mark_size // 2 - 78
    x = pad + mark_size + gap
    draw_tracked(d, (x, baseline), "Snap", wordmark,
                 INK_LIGHT if dark else INK, tracking)
    draw_tracked(d, (x + w_snap, baseline), "gate", wordmark,
                 GREEN_LIGHT if dark else GREEN, tracking)
    return canvas


def wordmark_only(dark=False):
    font = face("SemiBold", 132)
    tracking = -3.2
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    w_snap = sum(tmp.textlength(c, font=font) + tracking for c in "Snap")
    w_gate = sum(tmp.textlength(c, font=font) + tracking for c in "gate")
    W, H = int(w_snap + w_gate + 40), 200
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)
    draw_tracked(d, (20, 26), "Snap", font, INK_LIGHT if dark else INK, tracking)
    draw_tracked(d, (20 + w_snap, 26), "gate", font,
                 GREEN_LIGHT if dark else GREEN, tracking)
    return canvas


def consent_logo(size=120):
    """Marca cuadrada con el nombre, para la pantalla de consentimiento de Google.

    Se compone a 4x y se reduce al final: a 120 px el texto es de unos 15 px y
    dibujarlo directamente a ese tamano lo deja sucio.

    El nombre se mantiene dentro del circulo inscrito porque Google puede
    recortar el logotipo en redondo: a 35 px del centro el ancho disponible baja
    de 120 a unos 97, y un texto que use el ancho completo perderia las puntas.
    """
    S = size * 4
    canvas = Image.new("RGBA", (S, S), TILE_BG)
    d = ImageDraw.Draw(canvas)

    glyph = Image.open(ICON).convert("RGBA").crop(GLYPH_BOX)
    target = int(S * 0.50)
    gw, gh = glyph.size
    k = target / max(gw, gh)
    g = glyph.resize((max(1, int(gw * k)), max(1, int(gh * k))), Image.LANCZOS)
    canvas.paste(g, ((S - g.width) // 2, int(S * 0.13)), g)

    # El ancho util es el del circulo inscrito a la altura del texto, no el del
    # lienzo; de ahi que se busque el cuerpo por prueba en lugar de fijarlo.
    baseline = int(S * 0.735)
    dy = abs(baseline + S * 0.055 - S / 2)
    half = (max((S / 2) ** 2 - dy ** 2, 0.0)) ** 0.5
    usable = half * 2 * 0.88

    for pt in range(int(S * 0.16), int(S * 0.05), -2):
        font = face("SemiBold", pt)
        if d.textlength("Snapgate", font=font) <= usable:
            break
    width = d.textlength("Snapgate", font=font)
    d.text(((S - width) / 2, baseline), "Snapgate", font=font, fill=INK)

    return rounded(canvas, radius_ratio=0.225).resize((size, size), Image.LANCZOS)


# Los reclamos del grafico de cabecera, por idioma de la ficha. Play lo sirve
# por idioma igual que las capturas, asi que un grafico en espanol en la ficha
# inglesa desentona justo en lo primero que se ve.
FEATURE_TEXT = {
    "es": ("Decide qué fotos llegan a tu nube",
           "Pago único · Sin anuncios · Sin servidores"),
    "en": ("Decide which photos reach your cloud",
           "One-time purchase · No ads · No servers"),
    "pt": ("Decide que fotos chegam à tua nuvem",
           "Pagamento único · Sem anúncios · Sem servidores"),
    "fr": ("Choisissez les photos qui montent dans le cloud",
           "Achat unique · Sans publicité · Sans serveurs"),
    "de": ("Entscheide, welche Fotos in die Cloud kommen",
           "Einmalkauf · Keine Werbung · Keine Server"),
    "it": ("Decidi quali foto arrivano al tuo cloud",
           "Acquisto unico · Senza pubblicità · Senza server"),
}


def feature_graphic(lang="es"):
    """1024 x 500 exactos: es lo que exige la ficha de Google Play.

    Play recorta y superpone elementos en los bordes segun el dispositivo, asi
    que todo lo legible se mantiene lejos del margen.
    """
    W, H = 1024, 500
    canvas = Image.new("RGB", (W, H), (247, 250, 248))

    # Degradado muy suave en diagonal: da profundidad sin competir con el icono.
    grad = Image.new("RGB", (W, H))
    gd = ImageDraw.Draw(grad)
    for y in range(H):
        t = y / H
        gd.line([(0, y), (W, y)], fill=(
            int(250 - 12 * t), int(252 - 6 * t), int(250 - 8 * t)))
    canvas = grad

    d = ImageDraw.Draw(canvas)

    # Arco verde apenas perceptible en la esquina, como sello de marca.
    veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(veil).ellipse((W - 300, -220, W + 260, 250),
                                 fill=(22, 163, 74, 16))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), veil).convert("RGB")
    d = ImageDraw.Draw(canvas)

    mark_size = 208
    mark = icon_at(mark_size)
    mx, my = 88, (H - mark_size) // 2 - 18
    canvas.paste(mark, (mx, my), mark)

    name = face("SemiBold", 92)
    tag = face("Regular", 31)
    tracking = -2.4

    tx = mx + mark_size + 44
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    w_snap = sum(tmp.textlength(c, font=name) + tracking for c in "Snap")

    ty = my + 26
    draw_tracked(d, (tx, ty), "Snap", name, INK, tracking)
    draw_tracked(d, (tx + w_snap, ty), "gate", name, GREEN, tracking)

    claim, sub = FEATURE_TEXT[lang]

    # El reclamo se reduce si no cabe: en ingles es mas largo y se salia por el
    # borde sin avisar, que es como PIL trata cualquier texto que no entra.
    size = 31
    while size > 22 and d.textlength(claim, font=face("Regular", size)) > W - tx - 60:
        size -= 1
    d.text((tx + 3, ty + 122), claim, font=face("Regular", size), fill=SOFT)
    d.text((tx + 3, ty + 166), sub, font=face("Medium", 25), fill=(130, 139, 152))
    return canvas


# Tarjeta para compartir enlaces (og:image). El reclamo es el titulo de la
# portada, y la notificacion usa los textos reales de la app en cada idioma,
# los mismos que se ven en la primera captura de Play.
OG_TEXT = {
    "es": ("Elige qué fotos sube Google Fotos, una a una",
           "Android 11+ · Pago único · Sin servidores",
           ("10 fotos sin subir", "Elige cuáles suben", "Descartar", "Subir")),
    "en": ("Choose which photos Google Photos backs up",
           "Android 11+ · One-time purchase · No servers",
           ("10 photos not uploaded", "Choose which ones upload", "Discard", "Upload")),
    "pt": ("Escolhe as fotos que o Google Fotos guarda",
           "Android 11+ · Pagamento único · Sem servidores",
           ("10 fotos por enviar", "Escolhe quais são enviadas", "Descartar", "Enviar")),
    "fr": ("Choisissez les photos que Google Photos sauvegarde",
           "Android 11+ · Achat unique · Sans serveurs",
           ("10 photos non envoyées", "Choisissez lesquelles partent", "Écarter", "Envoyer")),
    "de": ("Entscheide, welche Fotos Google Fotos sichert",
           "Android 11+ · Einmalkauf · Keine Server",
           ("10 Fotos nicht hochgeladen", "Wähle aus, was hochlädt", "Verwerfen", "Hochladen")),
    "it": ("Scegli quali foto carica Google Foto, una a una",
           "Android 11+ · Acquisto unico · Senza server",
           ("10 foto non caricate", "Scegli quali caricare", "Scarta", "Carica")),
}


def wrap(draw, text, font, width):
    lines, line = [], ""
    for word in text.split():
        probe = f"{line} {word}".strip()
        if line and draw.textlength(probe, font=font) > width:
            lines.append(line)
            line = word
        else:
            line = probe
    return lines + [line]


def landscape(size, sky, hills, sun=None):
    """Miniatura de paisaje como las de las capturas: cielo, sol y dos colinas."""
    w, h = size
    img = Image.new("RGB", size, sky)
    d = ImageDraw.Draw(img)
    if sun:
        d.ellipse((w * 0.68, h * 0.10, w * 0.86, h * 0.28), fill=sun)
    d.ellipse((-w * 0.3, h * 0.55, w * 0.7, h * 1.5), fill=hills[0])
    d.ellipse((w * 0.35, h * 0.50, w * 1.35, h * 1.5), fill=hills[0])
    d.ellipse((-w * 0.1, h * 0.72, w * 1.1, h * 1.7), fill=hills[1])
    return img


def document(size):
    """Miniatura de un documento fotografiado: la clase de foto que sobra."""
    w, h = size
    img = Image.new("RGB", size, (250, 249, 244))
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, int(w * 0.07), h), fill=(52, 50, 48))
    d.rectangle((int(w * 0.93), 0, w, h), fill=(52, 50, 48))
    y = h * 0.12
    for i in range(9):
        d.rectangle((w * 0.16, y, w * (0.80 if i % 3 else 0.62), y + h * 0.025),
                    fill=(120, 120, 120))
        y += h * 0.075
    return img


def og_card(lang="es"):
    """1200 x 630, el tamano que esperan las vistas previas de enlaces.

    Se dibuja a 2x y se reduce al final para que el texto pequeno de la
    notificacion salga limpio.
    """
    K = 2
    W, H = 1200 * K, 630 * K
    claim, sub, (n_title, n_text, n_discard, n_upload) = OG_TEXT[lang]

    canvas = Image.new("RGB", (W, H))
    gd = ImageDraw.Draw(canvas)
    for y in range(H):
        t = y / H
        gd.line([(0, y), (W, y)], fill=(int(250 - 12 * t), int(252 - 6 * t), int(250 - 8 * t)))
    veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(veil).ellipse((W - 380 * K, -300 * K, W + 320 * K, 330 * K),
                                 fill=(22, 163, 74, 18))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), veil)
    d = ImageDraw.Draw(canvas)

    # Marca arriba a la izquierda.
    mark_size = 96 * K
    mark = icon_at(mark_size)
    x0, y0 = 72 * K, 64 * K
    canvas.paste(mark, (x0 - int(mark_size * 0.10), y0 - int(mark_size * 0.10)), mark)
    name = face("SemiBold", 54 * K)
    tracking = -1.4 * K
    w_snap = sum(d.textlength(c, font=name) + tracking for c in "Snap")
    tx, ty = x0 + mark_size + 26 * K, y0 + 12 * K
    draw_tracked(d, (tx, ty), "Snap", name, INK, tracking)
    draw_tracked(d, (tx + w_snap, ty), "gate", name, GREEN, tracking)

    # Reclamo: el cuerpo mas grande que quepa en tres lineas.
    col = 560 * K
    for pt in range(60, 40, -2):
        font = face("SemiBold", pt * K)
        lines = wrap(d, claim, font, col)
        if len(lines) <= 3:
            break
    lead = int(pt * K * 1.18)
    cy = 250 * K - (len(lines) - 3) * lead // 2
    for i, line in enumerate(lines):
        d.text((x0, cy + i * lead), line, font=font, fill=INK)

    d.text((x0, 540 * K), sub, font=face("Medium", 24 * K), fill=(118, 127, 140))

    # A la derecha, un trozo de la galeria con la notificacion encima.
    px, py, pw = 688 * K, 150 * K, 456 * K
    tile = (pw - 8 * K) // 3
    ph = 70 * K + tile * 2 + 4 * K
    screen = Image.new("RGB", (pw, ph), (250, 250, 250))
    thumbs = [
        landscape((tile, tile), (178, 210, 236), [(108, 150, 120), (70, 110, 84)]),
        landscape((tile, tile), (240, 200, 160), [(140, 110, 130), (90, 70, 96)]),
        document((tile, tile)),
        document((tile, tile)),
        landscape((tile, tile), (120, 160, 206), [(70, 110, 140), (50, 84, 112)], (252, 240, 200)),
        landscape((tile, tile), (238, 160, 130), [(110, 80, 100), (70, 52, 72)], (250, 214, 140)),
    ]
    for i, th in enumerate(thumbs):
        screen.paste(th, ((i % 3) * (tile + 4 * K), 70 * K + (i // 3) * (tile + 4 * K)))
    # La galeria se desvanece hacia abajo en transparencia, no hacia un color,
    # para que no se note el borde sobre el degradado del fondo.
    screen = rounded(screen.convert("RGBA"), radius_ratio=0.06)
    alpha = screen.getchannel("A")
    fade = Image.new("L", (pw, ph), 255)
    fd = ImageDraw.Draw(fade)
    for y in range(ph):
        fd.line([(0, y), (pw, y)], fill=int(255 * min(1, max(0, (ph - y) / (ph * 0.45)))))
    screen.putalpha(Image.composite(fade, Image.new("L", (pw, ph), 0), alpha))
    canvas.paste(screen, (px, py), screen)

    # Notificacion, con la sombra suave del resto de la marca.
    nx, ny, nw, nh = px - 34 * K, py - 40 * K, pw + 68 * K, 176 * K
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((nx, ny + 10 * K, nx + nw, ny + nh + 10 * K),
                                             radius=34 * K, fill=(20, 26, 34, 60))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(18 * K)))
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle((nx, ny, nx + nw, ny + nh), radius=34 * K, fill=(234, 233, 241))

    ix, iy, ir = nx + 30 * K, ny + 34 * K, 22 * K
    d.ellipse((ix, iy, ix + ir * 2, iy + ir * 2), fill=(62, 82, 140))
    cx, cyy = ix + ir, iy + ir
    d.rounded_rectangle((cx - 11 * K, cyy - 8 * K, cx + 11 * K, cyy + 9 * K), radius=3 * K,
                        fill=(255, 255, 255))
    d.polygon([(cx, cyy - 6 * K), (cx - 6 * K, cyy + 1 * K), (cx + 6 * K, cyy + 1 * K)],
              fill=(62, 82, 140))
    d.rectangle((cx - 2 * K, cyy, cx + 2 * K, cyy + 5 * K), fill=(62, 82, 140))

    # Los textos se reducen hasta caber antes de la miniatura: en frances y
    # aleman son bastante mas largos que en espanol.
    tx = ix + ir * 2 + 22 * K
    room = nw - (tx - nx) - 174 * K
    pt = 25
    while pt > 17 and max(d.textlength(n_title, font=face("Medium", pt * K)),
                          d.textlength(n_text, font=face("Regular", (pt - 2) * K))) > room:
        pt -= 1
    d.text((tx, ny + 28 * K), n_title, font=face("Medium", pt * K), fill=(30, 31, 38))
    d.text((tx, ny + 64 * K), n_text, font=face("Regular", (pt - 2) * K), fill=(72, 74, 86))

    th = landscape((76 * K, 76 * K), (178, 210, 236), [(108, 150, 120), (70, 110, 84)],
                   (244, 206, 90))
    th = rounded(th.convert("RGBA"), radius_ratio=0.14)
    canvas.paste(th, (nx + nw - 150 * K, ny + 24 * K), th)
    d = ImageDraw.Draw(canvas)
    ex, ey = nx + nw - 58 * K, ny + 46 * K
    d.ellipse((ex, ey, ex + 32 * K, ey + 32 * K), fill=(220, 219, 228))
    d.line([(ex + 9 * K, ey + 13 * K), (ex + 16 * K, ey + 20 * K), (ex + 23 * K, ey + 13 * K)],
           fill=(40, 40, 48), width=3 * K, joint="curve")

    btn = face("Medium", 23 * K)
    by = ny + 122 * K
    d.text((tx, by), n_discard, font=btn, fill=(70, 92, 160))
    d.text((tx + d.textlength(n_discard, font=btn) + 44 * K, by), n_upload, font=btn,
           fill=(70, 92, 160))

    return canvas.convert("RGB").resize((1200, 630), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    jobs = {
        "logo-horizontal.png": horizontal(),
        "logo-horizontal-dark.png": horizontal(dark=True),
        "wordmark.png": wordmark_only(),
        "wordmark-dark.png": wordmark_only(dark=True),
    }
    for name, img in jobs.items():
        img.save(os.path.join(OUT, name))

    features = os.path.join(ROOT, "assets", "store", "feature")
    os.makedirs(features, exist_ok=True)
    for lang in FEATURE_TEXT:
        feature_graphic(lang).save(os.path.join(features, f"{lang}.png"))

    og = os.path.join(OUT, "og")
    os.makedirs(og, exist_ok=True)
    for lang in OG_TEXT:
        og_card(lang).save(os.path.join(og, f"{lang}.png"), optimize=True)

    # Logotipo de la pantalla de consentimiento de OAuth: 120 x 120 exactos.
    # Google exige que identifique la marca sin ambiguedad y que sea el mismo que
    # se ve en la web, asi que es el icono cuadrado, no el logotipo horizontal:
    # un lockup con texto se reduce a un borron ilegible a ese tamano.
    consent = Image.new("RGB", (120, 120), (255, 255, 255))
    mark = consent_logo(120)
    consent.paste(mark, (0, 0), mark)
    consent.save(os.path.join(OUT, "oauth-consent-logo-120.png"))

    # El mismo diseno en grande, para la web y para cualquier otro sitio que
    # pida la marca con nombre.
    consent_logo(512).save(os.path.join(OUT, "mark-named-512.png"))

    # El mismo icono a 512 para la web, para que la pantalla de consentimiento y
    # la portada muestren exactamente la misma marca.
    site = icon_at(512, shadow=False)
    site.save(os.path.join(OUT, "mark-512.png"))

    # Icono de la ficha de Play: 512 x 512 exactos, sin transparencia.
    store = Image.new("RGB", (512, 512), (255, 255, 255))
    store.paste(icon_at(512, shadow=False).convert("RGB"), (0, 0),
                icon_at(512, shadow=False))
    store.save(os.path.join(OUT, "play-icon-512.png"))

    for f in sorted(os.listdir(OUT)):
        im = Image.open(os.path.join(OUT, f))
        print(f"  {f}  {im.size[0]}x{im.size[1]}")


if __name__ == "__main__":
    main()
