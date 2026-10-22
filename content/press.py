# -*- coding: utf-8 -*-
"""
Pagina de prensa. Solo en ingles: la leen redacciones y canales de cualquier
pais, y una version por idioma seria una cosa mas que mantener al dia. Los
pies de pagina de todos los idiomas enlazan aqui.

Todo lo que hay aqui tiene que poder copiarse tal cual en un articulo: frases
completas, datos que no caducan y enlaces directos a los ficheros.
"""

from content.legal import CONTACT

PLAY_URL = "https://play.google.com/store/apps/details?id=com.snapgate.app"
LANGS = ["en", "es", "pt", "fr", "de", "it"]
SHOTS = [
    ("01-notif", "Decide from the notification"),
    ("02-selection", "Or review in batches"),
    ("03-features", "Rules that decide for you"),
    ("04-onb1", "Your cloud stops filling up"),
]


def _gallery():
    items = "".join(
        f'<a href="../assets/store/phone/en/{name}.png">'
        f'<img src="../assets/web/shots/en/{name}.webp" width="540" height="960" '
        f'loading="lazy" alt="{alt}"></a>'
        for name, alt in SHOTS
    )
    return f'<div class="shots">{items}</div>'


def _localized():
    rows = "".join(
        f"<tr><td>{lang.upper()}</td>"
        + "".join(
            f'<td><a href="../assets/store/phone/{lang}/{name}.png">{i}</a></td>'
            for i, (name, _) in enumerate(SHOTS, 1)
        )
        + "</tr>"
        for lang in LANGS
    )
    return f"<table><tr><th>Language</th><th colspan=\"4\">Screenshots (1080 × 1920 PNG)</th></tr>{rows}</table>"


PRESS = {
    "title": "Press kit · Snapgate",
    "description": "Facts, screenshots, logos and contact for writing about Snapgate, "
                   "the Android app that asks before each photo goes to Google Photos.",
    "h1": "Press kit",
    "meta": "Everything you need to write about Snapgate. Use any of it freely.",
    "body": f"""
<h2>In one line</h2>
<p>Snapgate asks you, right from the notification, whether each new photo should
back up to Google Photos.</p>

<h2>In a paragraph</h2>
<p>Google Photos backup has two settings: everything or nothing. So receipts,
parking spots, screenshots and meeting whiteboards end up in the cloud next to
the photos that matter, eating into the free 15 GB. Snapgate adds a third
option. Seconds after you take a photo, a notification shows a thumbnail with
two buttons, Upload and Discard. Discarded photos stay on the phone untouched.
Temporary modes and rules by time, day or folder handle the moments when you
don't want to be asked. There are no servers, no ads and no analytics, and the
Google permission it uses can only add photos, never read or delete them.</p>

<h2>Fact sheet</h2>
<table>
<tr><th>App</th><td>Snapgate: selective backup</td></tr>
<tr><th>Developer</th><td>jfjalburquerque (visionatec), independent developer based in Spain</td></tr>
<tr><th>Platform</th><td>Android 11 or later</td></tr>
<tr><th>Price</th><td>Free 14-day trial, then a one-time purchase of €4.99 (local prices vary). No subscription.</td></tr>
<tr><th>Privacy</th><td>No servers, no ads, no analytics. Photos only leave the phone to the user's own Google Photos library, and only when approved.</td></tr>
<tr><th>Languages</th><td>English, Spanish, Portuguese, French, German, Italian</td></tr>
<tr><th>Released</th><td>September 2026</td></tr>
<tr><th>Download</th><td><a href="{PLAY_URL}">Google Play</a></td></tr>
</table>

<h2>Screenshots</h2>
<p>Click any image for the full-resolution PNG.</p>
{_gallery()}
<p>The same four screenshots in every language the app supports:</p>
{_localized()}

<h2>Logos and graphics</h2>
<ul>
<li><a href="../assets/brand/play-icon-512.png">App icon</a>, 512 × 512 PNG</li>
<li><a href="../assets/brand/logo-horizontal.png">Logo for light backgrounds</a>, PNG</li>
<li><a href="../assets/brand/logo-horizontal-dark.png">Logo for dark backgrounds</a>, PNG</li>
<li><a href="../assets/store/feature/en.png">Feature graphic</a>, 1024 × 500 PNG</li>
</ul>

<h2>Coverage</h2>
<ul>
<li><a href="https://www.youtube.com/watch?v=TYNzg59ke30&amp;t=61s">HowToMen: Top 15 Best Android Apps, October 2026</a> (YouTube)</li>
<li><a href="https://www.bug.hr/appdana/snapgate-omogucuje-biranje-koje-ce-fotografije-zavrsiti-u-google-photosu-63479">Bug.hr: App of the Day</a> (Croatia)</li>
</ul>

<h2>Contact</h2>
<p>Questions, interviews or a free unlock code for review:
<a href="mailto:{CONTACT}">{CONTACT}</a>. I usually answer within a day.</p>
""",
}
