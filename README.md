# snapgate.app

Sitio de [Snapgate](https://github.com/jfjalburquerque/snapgate), la app que te
deja decidir qué fotos llegan a tu nube.

Sitio estático puro: sin framework, sin dependencias en tiempo de ejecución y sin
nada que se descargue de terceros. Se publica con GitHub Pages directamente desde
la rama `main`.

## Generar

```
python3 build.py
```

Escribe un directorio por idioma en la raíz. **El HTML generado se versiona**: es
lo que Pages sirve, y así el repositorio es desplegable sin ningún paso de
compilación.

## Estructura

```
build.py            Plantillas y recorrido de ficheros
content/site.py     Cabecera, pie y portada, por idioma
content/legal.py    Privacidad y términos, por idioma
content/blog.py     Artículos
tools/branding.py   Genera el logotipo y los recursos de Play
assets/             Hoja de estilos, icono, tipografía y marca
```

Idiomas: español, inglés, portugués, francés, alemán e italiano. La portada y las
páginas legales están en los seis; los artículos del blog, de momento, en español
e inglés — el generador ya contempla el resto y el índice avisa al lector.

## Marca

```
python3 tools/branding.py
```

Produce en `assets/brand/`:

| Fichero | Uso |
|---|---|
| `logo-horizontal.png` | Logotipo principal, fondo claro |
| `logo-horizontal-dark.png` | Igual, para fondos oscuros |
| `wordmark.png` / `-dark.png` | Solo la palabra |
| `../store/feature/<idioma>.png` | Gráfico de cabecera de Play, 1024 × 500, uno por idioma |
| `play-icon-512.png` | Icono de la ficha de Play, 512 × 512 |

Tipografía [Inter](https://rsms.me/inter/), con licencia SIL Open Font.

El icono se compone aquí a partir del dibujo y un fondo liso, igual que hace
Android con el icono adaptativo. Reutilizar el PNG original dejaba visible su
propio cuadrado redondeado dentro del recorte.

## Pendiente

- La fuente del icono es de 192 px. Con el original en alta resolución, estos
  recursos ganarían nitidez, sobre todo el de 512.
- El dominio propio es `snapgate.app`, declarado en `CNAME` y en `SITE_URL`
  dentro de `build.py`. Si alguna vez cambia, hay que tocar los dos y regenerar.
- Correo de contacto real en `content/legal.py`.

## Publicar

En los ajustes del repositorio, **Pages → Source: Deploy from a branch → `main`
/ (root)**. El fichero `.nojekyll` evita que Jekyll procese la salida.
