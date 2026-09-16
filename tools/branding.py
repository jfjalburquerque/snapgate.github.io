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


def feature_graphic():
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

    d.text((tx + 3, ty + 122), "Decide qué fotos llegan a tu nube", font=tag, fill=SOFT)
    d.text((tx + 3, ty + 166), "Pago único · Sin anuncios · Sin servidores",
           font=face("Medium", 25), fill=(130, 139, 152))
    return canvas


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

    feature_graphic().save(os.path.join(OUT, "play-feature-graphic.png"))

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
