#!/usr/bin/env python3
"""
Copias ligeras de las capturas de Play para la portada.

Las de `assets/store/phone/` son las que se suben a Play: 1080 x 1920 y en PNG,
hasta 280 KB cada una. En la portada se ven a menos de 300 px de ancho, y
cuatro de esas por pagina pesaban casi un mega en un movil. Aqui salen a la
mitad y en WebP, que el navegador escala sin perder nada visible.

    python3 tools/web_shots.py

Escribe en `assets/web/shots/<idioma>/`. Los originales siguen enlazados desde
la pagina de prensa, que es donde alguien los quiere a resolucion completa.
"""

import glob
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "store", "phone")
DST = os.path.join(ROOT, "assets", "web", "shots")
SIZE = (540, 960)


def main():
    written = 0
    for path in sorted(glob.glob(os.path.join(SRC, "*", "*.png"))):
        lang = os.path.basename(os.path.dirname(path))
        name = os.path.splitext(os.path.basename(path))[0]
        out = os.path.join(DST, lang, name + ".webp")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        Image.open(path).convert("RGB").resize(SIZE, Image.LANCZOS).save(
            out, "WEBP", quality=82, method=6
        )
        written += 1
    print(f"{written} capturas escritas en {os.path.relpath(DST, ROOT)}")


if __name__ == "__main__":
    main()
