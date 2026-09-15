#!/usr/bin/env python3
"""
Compone las capturas de la ficha de Google Play a partir de capturas reales.

Play exige una relacion de aspecto entre 16:9 y 9:16; las pantallas modernas son
mas alargadas que eso, asi que la captura se monta sobre un lienzo 9:16 con un
rotulo encima. De paso el rotulo hace el trabajo de venta, porque en la ficha se
ven en miniatura y sin contexto.
"""

import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = os.path.join(ROOT, "assets", "fonts", "Inter.ttf")
OUT = os.path.join(ROOT, "assets", "store", "phone")
CAPS = "/tmp/claude-1000/-home-pepe-projects-testialo-backend/f2c56138-301a-4a2d-a094-db8b7434a34e/scratchpad/caps"

W, H = 1080, 1920
INK = (28, 32, 39)
SOFT = (99, 108, 122)

SHOTS = [
    ("phone-notif.png", "Decide desde la notificación", "Sin abrir la app."),
    ("phone-selection.png", "O repasa por tandas", "Diez fotos despachadas en segundos."),
    ("phone-features.png", "Reglas que deciden por ti", "Y modos temporales que caducan solos."),
    ("phone-onb1.png", "Tu nube deja de llenarse", "De tickets, facturas y pizarras."),
]


def face(instance, size):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_name(instance)
    return f


def wrap(draw, text, font, max_width):
    """Reparte el texto en lineas que quepan. PIL no ajusta solo: si el rotulo
    se pasa de ancho, lo dibuja igual y se sale del lienzo sin avisar."""
    words, lines, current = text.split(), [], ""
    for word in words:
        probe = (current + " " + word).strip()
        if draw.textlength(probe, font=font) <= max_width:
            current = probe
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def frame(shot_name, title, subtitle, index):
    canvas = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(canvas)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(
            int(247 - 10 * t), int(251 - 5 * t), int(248 - 7 * t)))

    veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(veil).ellipse((-240, -300, 620, 360), fill=(22, 163, 74, 18))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), veil).convert("RGB")
    d = ImageDraw.Draw(canvas)

    margin = 72
    title_font = face("SemiBold", 60)
    sub_font = face("Regular", 35)
    y = 108
    for line in wrap(d, title, title_font, W - margin * 2):
        d.text((margin, y), line, font=title_font, fill=INK)
        y += 72
    d.text((margin + 2, y + 6), subtitle, font=sub_font, fill=SOFT)

    shot = Image.open(os.path.join(CAPS, shot_name)).convert("RGB")
    top = 372
    target_h = H - top - 30
    scale = target_h / shot.height
    shot = shot.resize((int(shot.width * scale), target_h), Image.LANCZOS)

    # Esquinas redondeadas y sombra: separa la pantalla del fondo sin necesidad
    # de dibujar un marco de movil, que envejece mal y ocupa sitio.
    radius = 34
    mask = Image.new("L", shot.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, shot.width - 1, shot.height - 1),
                                           radius=radius, fill=255)
    x = (W - shot.width) // 2
    y = top

    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle(
        (x + 6, y + 16, x + shot.width - 6, y + shot.height),
        radius=radius, fill=(18, 24, 32, 60))
    canvas = Image.alpha_composite(
        canvas.convert("RGBA"), shadow.filter(ImageFilter.GaussianBlur(26))).convert("RGB")

    canvas.paste(shot, (x, y), mask)
    return canvas


def main():
    os.makedirs(OUT, exist_ok=True)
    for i, (name, title, sub) in enumerate(SHOTS, start=1):
        img = frame(name, title, sub, i)
        path = os.path.join(OUT, f"{i:02d}-{name.replace('phone-', '')}")
        img.save(path)
        print(f"  {os.path.basename(path)}  {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
