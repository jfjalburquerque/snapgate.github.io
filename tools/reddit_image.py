#!/usr/bin/env python3
"""
Imagen promocional para Reddit.

No es un banner: en esos foros un cartel publicitario rinde peor que ver el
producto funcionando. El protagonista es la notificacion recortada y grande,
porque es la aplicacion entera en un vistazo, y al lado la pantalla de revision
para que se entienda que hay algo mas detras.
"""

import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(ROOT, "assets", "fonts", "Inter.ttf")
CAPS = "/tmp/claude-1000/-home-pepe-projects-testialo-backend/f2c56138-301a-4a2d-a094-db8b7434a34e/scratchpad/caps"
OUT = os.path.join(ROOT, "assets", "store", "social")

W, H = 1600, 900
INK = (28, 32, 39)
SOFT = (99, 108, 122)
GREEN = (22, 163, 74)


def face(instance, size):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_name(instance)
    return f


def rounded(img, radius):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, img.size[0] - 1, img.size[1] - 1), radius=radius, fill=255)
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def drop(canvas, box, radius, blur=30, alpha=58):
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(box, radius=radius, fill=(18, 24, 32, alpha))
    return Image.alpha_composite(canvas.convert("RGBA"),
                                 shadow.filter(ImageFilter.GaussianBlur(blur))).convert("RGB")


def wrap(draw, text, font, max_width):
    """Reparte en lineas que quepan. PIL dibuja fuera del lienzo sin avisar."""
    words, lines, cur = text.split(), [], ""
    for wd in words:
        probe = (cur + " " + wd).strip()
        if draw.textlength(probe, font=font) <= max_width:
            cur = probe
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def build():
    canvas = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(canvas)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(int(246 - 8 * t), int(250 - 4 * t), int(247 - 6 * t)))

    veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(veil).ellipse((W - 420, -300, W + 320, 330), fill=(22, 163, 74, 16))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), veil).convert("RGB")
    d = ImageDraw.Draw(canvas)

    shot = Image.open(os.path.join(CAPS, "en-notif.png")).convert("RGB")

    # Limites exactos de la tarjeta, medidos sobre la captura. Recortar a ojo
    # arrastraba una tira de la rejilla de debajo y parecia un defecto.
    notif = shot.crop((48, 90, 1032, 415))
    scale = 880 / notif.width
    notif = notif.resize((880, int(notif.height * scale)), Image.LANCZOS)
    nx, ny = 80, 356
    # El radio de recorte va por encima del que trae la tarjeta en la captura:
    # si coincide justo, por la esquina asoma la foto que hay detras.
    card = rounded(notif.convert("RGBA"), 46)
    canvas = drop(canvas, (nx + 8, ny + 18, nx + notif.width - 8, ny + notif.height + 6), 46)
    canvas.paste(card, (nx, ny), card)
    d = ImageDraw.Draw(canvas)

    # La pantalla de revision, entera y mas pequena: contexto, no protagonista.
    grid = Image.open(os.path.join(CAPS, "en-selection.png")).convert("RGB")
    gh = 690
    grid = grid.resize((int(grid.width * gh / grid.height), gh), Image.LANCZOS)
    gx, gy = W - grid.width - 110, 150
    canvas = drop(canvas, (gx + 8, gy + 16, gx + grid.width - 8, gy + grid.height), 22)
    canvas.paste(rounded(grid.convert("RGBA"), 22), (gx, gy), rounded(grid.convert("RGBA"), 22))
    d = ImageDraw.Draw(canvas)

    # El titular se ajusta a la columna izquierda, sin invadir la del movil.
    column = gx - 150
    head = face("SemiBold", 48)
    y = 110
    d.text((80, y), "You take a photo.", font=head, fill=INK)
    y += 62
    for line in wrap(d, "Snapgate asks before it reaches the cloud.", head, column):
        d.text((80, y), line, font=head, fill=GREEN)
        y += 62
    d.text((82, y + 14), "Answer from the notification. Never open the app.",
           font=face("Regular", 29), fill=SOFT)

    d.text((82, ny + notif.height + 42),
           "Discarded photos stay on your phone. Nothing is ever deleted.",
           font=face("Medium", 27), fill=SOFT)
    return canvas


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    img = build()
    path = os.path.join(OUT, "reddit-en.png")
    img.save(path)
    print(f"  {os.path.basename(path)}  {img.size[0]}x{img.size[1]}")
