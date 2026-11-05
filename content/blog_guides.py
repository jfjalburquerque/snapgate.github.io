# -*- coding: utf-8 -*-
"""Guías prácticas del blog.

Responden a preguntas que la gente busca de verdad en Google, y las responden
primero con lo que ofrece Google Fotos. Snapgate aparece al final, como la
opción para quien quiere ir más allá: una guía que solo sirve para vender no
la enlaza nadie, y entonces Google tampoco la enseña.

Los nombres de los menús de Google Fotos cambian entre versiones; los textos lo
avisan en lugar de prometer una ruta exacta.
"""

PLAY = ("https://play.google.com/store/apps/details?id=com.snapgate.app"
        "&utm_source=blog&utm_medium=web&utm_campaign={slug}")


def cta(slug, text, button):
    return (f'<div class="callout"><p>{text}</p>'
            f'<p><a class="btn" href="{PLAY.format(slug=slug)}" rel="noopener">'
            f'{button}</a></p></div>')


GUIDES = [
    {
        "slug": "stop-google-photos-backing-up-screenshots",
        "date": "2026-11-05",
        "langs": {
            "es": {
                "title": "Cómo evitar que Google Fotos suba las capturas de pantalla",
                "date_label": "5 de noviembre de 2026",
                "excerpt": "Las capturas llenan la nube sin que nadie lo decida. Así "
                           "se apaga su copia en Android y se limpian las que ya subieron.",
                "body": """
<p>Una captura del código de una reserva, otra de un meme, otra de una conversación
que querías enseñar a alguien. Ninguna era para guardarla, pero si Google Fotos copia
la carpeta de capturas, todas acaban en tu cuenta ocupando los mismos 15 GB que tus
fotos de verdad.</p>

<h2>Apagar la copia de la carpeta de capturas</h2>

<p>En Android, Google Fotos decide qué se sube por carpetas. La de la cámara se copia
siempre que la copia de seguridad esté activa; las demás, solo si las activas.</p>

<ol>
  <li>Abre Google Fotos y toca tu foto de perfil, arriba a la derecha.</li>
  <li>Entra en <strong>Ajustes de Fotos → Copia de seguridad</strong>.</li>
  <li>Busca la opción de <strong>carpetas del dispositivo</strong> (el nombre exacto
  cambia un poco entre versiones).</li>
  <li>Desactiva <strong>Screenshots</strong> o <strong>Capturas de pantalla</strong>.</li>
</ol>

<p>Desde ese momento, las capturas nuevas se quedan solo en el móvil. Si en esa misma
pantalla tienes activada la opción de copiar <em>todas</em> las carpetas, apágala
también: si no, cualquier carpeta nueva que cree una app se subirá sola.</p>

<h2>Borrar las capturas que ya subieron</h2>

<p>Apagar la copia no borra nada de lo que ya está en la nube. Para encontrarlo, busca
<strong>«capturas de pantalla»</strong> en el buscador de Google Fotos: te las agrupa
todas. Selecciónalas y bórralas, y luego vacía la papelera, porque mientras estén ahí
siguen ocupando espacio.</p>

<p>Cuidado: si borras desde Google Fotos una captura que también está en el móvil, la
app puede borrarla de los dos sitios. Si quieres conservar la copia del teléfono,
bórrala desde la web <a href="https://photos.google.com">photos.google.com</a> después
de apagar la copia de esa carpeta.</p>

<h2>¿Y la captura que sí quieres guardar?</h2>

<p>Ese es el límite de decidir por carpetas: o subes todas las capturas o ninguna.
Puedes subir una suelta a mano (mantenla pulsada en Google Fotos y elige
<strong>Hacer copia de seguridad</strong>), pero tienes que acordarte de hacerlo.</p>

<p>Si prefieres que el móvil te lo pregunte en el momento, eso es lo que hace
<strong>Snapgate</strong>: al hacer una foto o una captura te llega un aviso con dos
botones, <em>Subir</em> o <em>Descartar</em>, y decides sin abrir nada. Lo que
descartas se queda en el móvil y nunca ocupa espacio en tu cuenta. También puedes
crear una regla para que las capturas no se suban nunca y te pregunte solo por las
fotos de la cámara.</p>
""" + cta("stop-google-photos-backing-up-screenshots",
           "Snapgate es una app para Android: 14 días de prueba y después un pago "
           "único, sin suscripción.", "Ver Snapgate en Google Play"),
            },
            "en": {
                "title": "How to stop Google Photos from backing up screenshots",
                "date_label": "5 November 2026",
                "excerpt": "Screenshots fill your cloud without anyone deciding to. "
                           "Here's how to stop them on Android and clear the ones "
                           "already uploaded.",
                "body": """
<p>A screenshot of a booking code, another of a meme, another of a chat you wanted
to show someone. None of them were meant to be kept, but if Google Photos backs up
your screenshots folder, they all end up in your account, eating the same 15 GB as
the photos you care about.</p>

<h2>Turn off backup for the screenshots folder</h2>

<p>On Android, Google Photos decides what to upload by folder. The camera folder is
backed up whenever backup is on; other folders only if you switch them on.</p>

<ol>
  <li>Open Google Photos and tap your profile picture, top right.</li>
  <li>Go to <strong>Photos settings → Backup</strong>.</li>
  <li>Find the <strong>device folders</strong> option (the exact name changes a
  little between versions).</li>
  <li>Switch off <strong>Screenshots</strong>.</li>
</ol>

<p>From then on, new screenshots stay on your phone only. If that same screen has
an option to back up <em>all</em> device folders, turn it off as well — otherwise
any new folder an app creates will start uploading on its own.</p>

<h2>Delete the screenshots that already uploaded</h2>

<p>Turning off backup doesn't delete anything already in the cloud. To find them,
search for <strong>"screenshots"</strong> in Google Photos: it groups them all.
Select them, delete them, then empty the trash — while they sit there, they still
count against your storage.</p>

<p>Careful: deleting a screenshot in the Google Photos app can remove it from your
phone too. If you want to keep the phone copy, delete from
<a href="https://photos.google.com">photos.google.com</a> after turning off backup
for that folder.</p>

<h2>What about the screenshot you do want to keep?</h2>

<p>That's the limit of deciding by folder: all screenshots or none. You can back up a
single one by hand (long-press it in Google Photos and choose <strong>Back up</strong>),
but you have to remember to do it.</p>

<p>If you'd rather your phone asked you at the moment you take it, that's what
<strong>Snapgate</strong> does: after each photo or screenshot you get a notification
with two buttons, <em>Upload</em> or <em>Discard</em>, and you decide without opening
anything. What you discard stays on your phone and never takes space in your account.
You can also set a rule so screenshots never upload and only camera photos ask.</p>
""" + cta("stop-google-photos-backing-up-screenshots",
           "Snapgate is an Android app: 14-day trial, then a one-time purchase, no "
           "subscription.", "See Snapgate on Google Play"),
            },
        },
    },
    {
        "slug": "google-photos-storage-full",
        "date": "2026-11-05",
        "langs": {
            "es": {
                "title": "Google Fotos lleno: cómo liberar espacio sin perder tus fotos",
                "date_label": "5 de noviembre de 2026",
                "excerpt": "Cuando se llenan los 15 GB, Google deja de hacer copia de "
                           "seguridad. Qué ocupa el espacio, cómo recuperarlo y cómo "
                           "evitar que vuelva a pasar.",
                "body": """
<p>Los 15 GB gratuitos de Google no son solo para fotos: los comparten Google Fotos,
Gmail y Google Drive. Cuando se llenan, la copia de seguridad de fotos se detiene, y
en Gmail pueden dejar de llegarte correos. Antes de pagar por más espacio, merece la
pena ver qué lo está ocupando.</p>

<h2>1. Mira qué ocupa el espacio</h2>

<p>En Google Fotos, toca tu foto de perfil y entra en <strong>Ajustes de Fotos →
Gestionar almacenamiento</strong> (o abre <a href="https://one.google.com/storage">
one.google.com/storage</a>). Verás cuánto gasta cada servicio y, en Fotos, una
herramienta que agrupa lo que más se suele poder borrar: <strong>fotos borrosas,
capturas de pantalla y vídeos grandes</strong>.</p>

<h2>2. Empieza por los vídeos grandes</h2>

<p>Un minuto de vídeo en 4K ocupa lo mismo que cientos de fotos. Revisar la lista de
vídeos grandes y borrar tres o cuatro que no necesitas suele liberar varios gigas de
golpe, mucho más que borrar fotos sueltas.</p>

<h2>3. Capturas y fotos que eran solo para un momento</h2>

<p>Capturas de pantalla, tickets, la plaza del parking, la pizarra de una reunión.
Busca <strong>«capturas de pantalla»</strong> o <strong>«recibos»</strong> en el
buscador de Google Fotos: los agrupa solo. Bórralos y <strong>vacía la
papelera</strong>, que si no siguen contando durante 60 días.</p>

<h2>4. Comprueba la calidad de la copia</h2>

<p>En <strong>Ajustes de Fotos → Copia de seguridad → Calidad de la copia</strong>
puedes elegir <strong>Ahorro de espacio</strong> en lugar de <em>Calidad original</em>.
Las fotos se comprimen un poco y los vídeos se reducen a 1080p; para fotos del móvil
la diferencia apenas se nota. Ojo: solo afecta a lo que subas a partir de ahora.</p>

<h2>5. Que no se vuelva a llenar</h2>

<p>Liberar espacio funciona, pero si todo se sigue subiendo solo, en unos meses
estarás igual. El problema de fondo es que la copia de Google Fotos es todo o nada:
sube cada foto de la cámara, también las que solo querías para diez minutos.</p>

<p>Para eso hicimos <strong>Snapgate</strong>. Con la copia de Google Fotos apagada
para la cámara, la app te avisa en cuanto haces una foto o un vídeo y eliges
<em>Subir</em> o <em>Descartar</em> desde la propia notificación. Lo que descartas se
queda en el móvil y nunca llega a ocupar espacio en tu cuenta. Y si quieres, comprime
las fotos antes de subirlas, como el ahorro de espacio de Google.</p>
""" + cta("google-photos-storage-full",
           "Snapgate es una app para Android: 14 días de prueba y después un pago "
           "único, sin suscripción.", "Ver Snapgate en Google Play"),
            },
            "en": {
                "title": "Google Photos storage full? How to free up space without losing photos",
                "date_label": "5 November 2026",
                "excerpt": "When the 15 GB fill up, Google stops backing up. What's "
                           "taking the space, how to get it back, and how to keep it "
                           "from happening again.",
                "body": """
<p>Google's free 15 GB aren't just for photos: Google Photos, Gmail and Google Drive
share them. When they fill up, photo backup stops, and Gmail may stop receiving
email. Before paying for more storage, it's worth seeing what's actually using it.</p>

<h2>1. See what's taking the space</h2>

<p>In Google Photos, tap your profile picture and go to <strong>Photos settings →
Manage storage</strong> (or open <a href="https://one.google.com/storage">
one.google.com/storage</a>). You'll see how much each service uses and, in Photos, a
tool that groups what's usually safe to delete: <strong>blurry photos, screenshots
and large videos</strong>.</p>

<h2>2. Start with large videos</h2>

<p>One minute of 4K video takes as much space as hundreds of photos. Going through
the large videos list and deleting three or four you don't need often frees several
gigabytes at once — far more than deleting photos one by one.</p>

<h2>3. Screenshots and photos that were only for a moment</h2>

<p>Screenshots, receipts, where you parked, a meeting whiteboard. Search for
<strong>"screenshots"</strong> or <strong>"receipts"</strong> in Google Photos: it
groups them for you. Delete them and <strong>empty the trash</strong>, or they keep
counting for 60 days.</p>

<h2>4. Check your backup quality</h2>

<p>Under <strong>Photos settings → Backup → Backup quality</strong> you can pick
<strong>Storage saver</strong> instead of <em>Original quality</em>. Photos are
slightly compressed and videos reduced to 1080p; for phone photos the difference is
barely visible. Note that it only applies to what you upload from now on.</p>

<h2>5. Keep it from filling up again</h2>

<p>Freeing space works, but if everything keeps uploading on its own, you'll be back
here in a few months. The underlying problem is that Google Photos backup is all or
nothing: it uploads every camera photo, including the ones you only needed for ten
minutes.</p>

<p>That's why we built <strong>Snapgate</strong>. With Google Photos backup turned off
for the camera, the app notifies you as soon as you take a photo or video, and you
choose <em>Upload</em> or <em>Discard</em> right from the notification. What you
discard stays on your phone and never takes space in your account. And if you like,
it shrinks photos before uploading, like Google's storage saver.</p>
""" + cta("google-photos-storage-full",
           "Snapgate is an Android app: 14-day trial, then a one-time purchase, no "
           "subscription.", "See Snapgate on Google Play"),
            },
        },
    },
    {
        "slug": "back-up-only-some-photos-google-photos",
        "date": "2026-11-05",
        "langs": {
            "es": {
                "title": "Cómo subir solo algunas fotos a Google Fotos (y no todas)",
                "date_label": "5 de noviembre de 2026",
                "excerpt": "La copia de Google Fotos sube todo o nada. Tres formas de "
                           "elegir qué fotos llegan a la nube, de la más manual a la "
                           "más cómoda.",
                "body": """
<p>La copia de seguridad de Google Fotos tiene dos posiciones: activada, y sube cada
foto de la cámara; desactivada, y no sube ninguna. No hay término medio para decir
«esta sí, esta no». Pero hay formas de conseguirlo.</p>

<h2>Opción 1: apagar la copia y subir a mano</h2>

<p>Desactiva la copia en <strong>Ajustes de Fotos → Copia de seguridad</strong>. Las
fotos seguirán apareciendo en Google Fotos, pero solo en el móvil. Cuando quieras
guardar una en la nube, mantenla pulsada, selecciona las que quieras y toca
<strong>Hacer copia de seguridad</strong>.</p>

<p><strong>Bien:</strong> control total y gratis. <strong>Mal:</strong> tienes que
acordarte. Si un día no lo haces y pierdes el móvil, esas fotos se pierden con él.</p>

<h2>Opción 2: decidir por carpetas</h2>

<p>En <strong>Ajustes de Fotos → Copia de seguridad</strong>, en la parte de carpetas
del dispositivo, puedes elegir qué carpetas se copian: la cámara sí, las capturas o
las fotos de WhatsApp no.</p>

<p><strong>Bien:</strong> automático. <strong>Mal:</strong> dentro de la carpeta de la
cámara sigue siendo todo o nada. El ticket de la compra y la foto de tu hija están en
la misma carpeta.</p>

<h2>Opción 3: que el móvil te pregunte en cada foto</h2>

<p>Es lo que hace <strong>Snapgate</strong>, una app que creamos justo por esto. Se
apaga la copia de Google Fotos para la carpeta de la cámara y, a partir de ahí, cada
vez que haces una foto o un vídeo te llega un aviso con dos botones:
<em>Subir</em> o <em>Descartar</em>. Decides en el momento, cuando todavía sabes para
qué la hiciste, y sin abrir ninguna app.</p>

<ul>
  <li>Lo que descartas <strong>no se borra</strong>: se queda en el móvil.</li>
  <li>Puedes revisar varias de golpe, a pantalla completa, si haces una ráfaga.</li>
  <li>Reglas automáticas: por ejemplo, que las capturas no se suban nunca o que lo
  que hagas en horario de trabajo no vaya a tu cuenta personal.</li>
  <li>Modos temporales: «sube todo durante el viaje» o «no subas nada esta tarde», y
  se apagan solos.</li>
</ul>

<p>Google está probando una copia solo de las fotos que marcas como favoritas, que
puede ayudar a algunos usuarios. La diferencia es el momento: con favoritos tienes
que entrar después a marcar cada foto; con Snapgate decides al hacerla, desde la
notificación.</p>
""" + cta("back-up-only-some-photos-google-photos",
           "Snapgate es una app para Android: 14 días de prueba y después un pago "
           "único, sin suscripción.", "Ver Snapgate en Google Play"),
            },
            "en": {
                "title": "How to back up only some photos to Google Photos (not all of them)",
                "date_label": "5 November 2026",
                "excerpt": "Google Photos backup is all or nothing. Three ways to choose "
                           "which photos reach the cloud, from fully manual to "
                           "effortless.",
                "body": """
<p>Google Photos backup has two positions: on, and it uploads every camera photo; off,
and it uploads none. There's no middle ground for saying "this one yes, this one no".
But there are ways to get there.</p>

<h2>Option 1: turn backup off and upload by hand</h2>

<p>Turn off backup under <strong>Photos settings → Backup</strong>. Your photos still
show up in Google Photos, but only on the phone. When you want one in the cloud,
long-press it, select the ones you want and tap <strong>Back up</strong>.</p>

<p><strong>Good:</strong> full control, and free. <strong>Bad:</strong> you have to
remember. If you forget one day and lose your phone, those photos go with it.</p>

<h2>Option 2: decide by folder</h2>

<p>Under <strong>Photos settings → Backup</strong>, in the device folders section, you
can choose which folders are backed up: the camera yes, screenshots or WhatsApp
images no.</p>

<p><strong>Good:</strong> automatic. <strong>Bad:</strong> inside the camera folder
it's still all or nothing. The shopping receipt and the photo of your kid live in the
same folder.</p>

<h2>Option 3: have your phone ask you for each photo</h2>

<p>That's what <strong>Snapgate</strong> does — an app we built for exactly this.
You turn off Google Photos backup for the camera folder and, from then on, every time
you take a photo or video you get a notification with two buttons: <em>Upload</em> or
<em>Discard</em>. You decide in the moment, while you still know why you took it,
without opening any app.</p>

<ul>
  <li>What you discard is <strong>not deleted</strong>: it stays on your phone.</li>
  <li>Review a burst all at once, full screen.</li>
  <li>Automatic rules: for example, screenshots never upload, or photos taken during
  work hours don't go to your personal account.</li>
  <li>Temporary modes: "upload everything during the trip" or "upload nothing this
  afternoon", and they switch off on their own.</li>
</ul>

<p>Google is testing a backup of only the photos you mark as favourites, which may help
some people. The difference is timing: with favourites you go back later and mark each
photo; with Snapgate you decide when you take it, from the notification.</p>
""" + cta("back-up-only-some-photos-google-photos",
           "Snapgate is an Android app: 14-day trial, then a one-time purchase, no "
           "subscription.", "See Snapgate on Google Play"),
            },
        },
    },
]
