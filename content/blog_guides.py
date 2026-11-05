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


# --- Traducciones ---------------------------------------------------------
# Mismo contenido que en español e inglés. Portugués de Portugal y con «tu»,
# francés con «vous», alemán con «du»: igual que la app.

_CTA = {
    "pt": ("O Snapgate é uma app para Android: 14 dias de teste e depois um "
           "pagamento único, sem subscrição.", "Ver o Snapgate no Google Play"),
    "fr": ("Snapgate est une app Android : 14 jours d’essai, puis un achat "
           "unique, sans abonnement.", "Voir Snapgate sur Google Play"),
    "de": ("Snapgate ist eine Android-App: 14 Tage testen, danach ein einmaliger "
           "Kauf, kein Abo.", "Snapgate bei Google Play ansehen"),
    "it": ("Snapgate è un’app per Android: 14 giorni di prova e poi un acquisto "
           "unico, senza abbonamento.", "Vedi Snapgate su Google Play"),
}

_DATE = {"pt": "5 de novembro de 2026", "fr": "5 novembre 2026",
         "de": "5. November 2026", "it": "5 novembre 2026"}

_T = {
    "stop-google-photos-backing-up-screenshots": {
        "pt": {
            "title": "Como impedir que o Google Fotos carregue as capturas de ecrã",
            "excerpt": "As capturas enchem a nuvem sem ninguém decidir. Como desligar "
                       "a cópia delas no Android e limpar as que já foram carregadas.",
            "body": """
<p>Uma captura do código de uma reserva, outra de um meme, outra de uma conversa que
querias mostrar a alguém. Nenhuma era para guardar, mas se o Google Fotos faz cópia
da pasta de capturas, todas acabam na tua conta a ocupar os mesmos 15 GB que as tuas
fotos a sério.</p>

<h2>Desligar a cópia da pasta de capturas</h2>

<p>No Android, o Google Fotos decide o que carregar por pastas. A da câmara é copiada
sempre que a cópia de segurança está ativa; as outras, só se as ativares.</p>

<ol>
  <li>Abre o Google Fotos e toca na tua foto de perfil, no canto superior direito.</li>
  <li>Entra em <strong>Definições do Fotos → Cópia de segurança</strong>.</li>
  <li>Procura a opção de <strong>pastas do dispositivo</strong> (o nome exato muda um
  pouco entre versões).</li>
  <li>Desativa <strong>Screenshots</strong> ou <strong>Capturas de ecrã</strong>.</li>
</ol>

<p>A partir daí, as capturas novas ficam só no telemóvel. Se nesse mesmo ecrã tiveres
ativa a opção de copiar <em>todas</em> as pastas, desliga-a também: caso contrário,
qualquer pasta nova criada por uma app começa a ser carregada sozinha.</p>

<h2>Apagar as capturas que já foram carregadas</h2>

<p>Desligar a cópia não apaga nada do que já está na nuvem. Para as encontrar, pesquisa
<strong>«capturas de ecrã»</strong> no Google Fotos: ele agrupa-as todas. Seleciona-as,
apaga-as e depois esvazia o caixote do lixo, porque enquanto lá estiverem continuam a
ocupar espaço.</p>

<p>Atenção: apagar uma captura na app Google Fotos pode apagá-la também do telemóvel.
Se quiseres manter a cópia do telemóvel, apaga-a em
<a href="https://photos.google.com">photos.google.com</a> depois de desligares a cópia
dessa pasta.</p>

<h2>E a captura que queres mesmo guardar?</h2>

<p>É o limite de decidir por pastas: ou carregas todas as capturas ou nenhuma. Podes
carregar uma à mão (mantém-na premida no Google Fotos e escolhe <strong>Fazer cópia de
segurança</strong>), mas tens de te lembrar.</p>

<p>Se preferes que o telemóvel te pergunte no momento, é isso que faz o
<strong>Snapgate</strong>: depois de cada foto ou captura recebes uma notificação com
dois botões, <em>Carregar</em> ou <em>Descartar</em>, e decides sem abrir nada. O que
descartas fica no telemóvel e nunca ocupa espaço na tua conta. Também podes criar uma
regra para que as capturas nunca sejam carregadas e só as fotos da câmara perguntem.</p>
""",
        },
        "fr": {
            "title": "Comment empêcher Google Photos de sauvegarder les captures d’écran",
            "excerpt": "Les captures remplissent le cloud sans que personne ne le "
                       "décide. Comment couper leur sauvegarde sur Android et nettoyer "
                       "celles déjà envoyées.",
            "body": """
<p>Une capture d’un code de réservation, une autre d’un mème, une autre d’une
conversation que vous vouliez montrer. Aucune n’était faite pour être gardée, mais si
Google Photos sauvegarde le dossier des captures, elles finissent toutes dans votre
compte, sur les mêmes 15 Go que vos vraies photos.</p>

<h2>Couper la sauvegarde du dossier des captures</h2>

<p>Sur Android, Google Photos décide quoi envoyer dossier par dossier. Celui de
l’appareil photo est sauvegardé dès que la sauvegarde est active ; les autres,
seulement si vous les activez.</p>

<ol>
  <li>Ouvrez Google Photos et touchez votre photo de profil, en haut à droite.</li>
  <li>Allez dans <strong>Paramètres de Photos → Sauvegarde</strong>.</li>
  <li>Cherchez l’option des <strong>dossiers de l’appareil</strong> (le nom exact
  change un peu selon les versions).</li>
  <li>Désactivez <strong>Screenshots</strong> ou <strong>Captures d’écran</strong>.</li>
</ol>

<p>Dès lors, les nouvelles captures restent uniquement sur le téléphone. Si ce même
écran propose de sauvegarder <em>tous</em> les dossiers, désactivez-le aussi : sinon,
tout nouveau dossier créé par une app sera envoyé automatiquement.</p>

<h2>Supprimer les captures déjà envoyées</h2>

<p>Couper la sauvegarde ne supprime rien de ce qui est déjà dans le cloud. Pour les
retrouver, cherchez <strong>« captures d’écran »</strong> dans Google Photos : il les
regroupe toutes. Sélectionnez-les, supprimez-les, puis videz la corbeille — tant
qu’elles y sont, elles occupent encore de l’espace.</p>

<p>Attention : supprimer une capture dans l’app Google Photos peut aussi l’effacer du
téléphone. Pour garder la copie du téléphone, supprimez-la depuis
<a href="https://photos.google.com">photos.google.com</a> après avoir coupé la
sauvegarde de ce dossier.</p>

<h2>Et la capture que vous voulez vraiment garder ?</h2>

<p>C’est la limite des dossiers : toutes les captures ou aucune. Vous pouvez en
sauvegarder une à la main (appui long dans Google Photos, puis
<strong>Sauvegarder</strong>), mais il faut y penser.</p>

<p>Si vous préférez que le téléphone vous pose la question sur le moment, c’est ce que
fait <strong>Snapgate</strong> : après chaque photo ou capture, une notification
apparaît avec deux boutons, <em>Envoyer</em> ou <em>Écarter</em>, et vous décidez sans
rien ouvrir. Ce que vous écartez reste sur le téléphone et n’occupe jamais d’espace
dans votre compte. Vous pouvez aussi créer une règle pour que les captures ne soient
jamais envoyées et que seules les photos de l’appareil photo vous demandent.</p>
""",
        },
        "de": {
            "title": "So verhinderst du, dass Google Fotos Screenshots sichert",
            "excerpt": "Screenshots füllen die Cloud, ohne dass jemand das entscheidet. "
                       "So schaltest du ihre Sicherung unter Android ab und räumst "
                       "die bereits hochgeladenen auf.",
            "body": """
<p>Ein Screenshot eines Buchungscodes, einer von einem Meme, einer von einem Chat, den
du jemandem zeigen wolltest. Keiner davon war zum Aufheben gedacht, aber wenn Google
Fotos den Screenshot-Ordner sichert, landen alle in deinem Konto – auf denselben 15 GB
wie deine echten Fotos.</p>

<h2>Sicherung des Screenshot-Ordners abschalten</h2>

<p>Unter Android entscheidet Google Fotos ordnerweise, was hochgeladen wird. Der
Kameraordner wird gesichert, sobald die Sicherung an ist; andere Ordner nur, wenn du
sie einschaltest.</p>

<ol>
  <li>Öffne Google Fotos und tippe oben rechts auf dein Profilbild.</li>
  <li>Gehe zu <strong>Fotos-Einstellungen → Sicherung</strong>.</li>
  <li>Suche die Option für <strong>Geräteordner</strong> (der genaue Name ändert sich
  je nach Version etwas).</li>
  <li>Schalte <strong>Screenshots</strong> aus.</li>
</ol>

<p>Ab dann bleiben neue Screenshots nur auf dem Handy. Gibt es auf derselben Seite die
Option, <em>alle</em> Geräteordner zu sichern, schalte sie auch aus – sonst wird jeder
neue Ordner, den eine App anlegt, von selbst hochgeladen.</p>

<h2>Bereits hochgeladene Screenshots löschen</h2>

<p>Das Abschalten löscht nichts, was schon in der Cloud liegt. Suche in Google Fotos
nach <strong>„Screenshots“</strong>: Die App gruppiert sie alle. Wähle sie aus,
lösche sie und leere danach den Papierkorb – solange sie dort liegen, belegen sie
weiter Speicherplatz.</p>

<p>Vorsicht: Wenn du einen Screenshot in der Google-Fotos-App löschst, kann er auch vom
Handy verschwinden. Willst du die Kopie auf dem Handy behalten, lösche ihn über
<a href="https://photos.google.com">photos.google.com</a>, nachdem du die Sicherung
für diesen Ordner abgeschaltet hast.</p>

<h2>Und der Screenshot, den du wirklich behalten willst?</h2>

<p>Das ist die Grenze der Ordner-Logik: alle Screenshots oder keiner. Du kannst einen
einzelnen von Hand sichern (in Google Fotos lange drücken und
<strong>Sichern</strong> wählen), musst aber daran denken.</p>

<p>Wenn dich dein Handy lieber im Moment selbst fragen soll, macht das
<strong>Snapgate</strong>: Nach jedem Foto oder Screenshot kommt eine Benachrichtigung
mit zwei Knöpfen, <em>Hochladen</em> oder <em>Verwerfen</em>, und du entscheidest,
ohne etwas zu öffnen. Was du verwirfst, bleibt auf dem Handy und belegt nie Platz in
deinem Konto. Du kannst auch eine Regel anlegen, damit Screenshots nie hochgeladen
werden und nur Kamerafotos nachfragen.</p>
""",
        },
        "it": {
            "title": "Come impedire a Google Foto di caricare gli screenshot",
            "excerpt": "Gli screenshot riempiono il cloud senza che nessuno lo decida. "
                       "Come disattivarne il backup su Android e pulire quelli già "
                       "caricati.",
            "body": """
<p>Uno screenshot del codice di una prenotazione, uno di un meme, uno di una chat che
volevi mostrare a qualcuno. Nessuno era da tenere, ma se Google Foto fa il backup della
cartella degli screenshot, finiscono tutti nel tuo account, negli stessi 15 GB delle
tue foto vere.</p>

<h2>Disattivare il backup della cartella degli screenshot</h2>

<p>Su Android, Google Foto decide cosa caricare per cartelle. Quella della fotocamera
viene copiata ogni volta che il backup è attivo; le altre, solo se le attivi.</p>

<ol>
  <li>Apri Google Foto e tocca la tua foto del profilo, in alto a destra.</li>
  <li>Vai in <strong>Impostazioni di Foto → Backup</strong>.</li>
  <li>Cerca l’opzione delle <strong>cartelle del dispositivo</strong> (il nome esatto
  cambia un po’ tra le versioni).</li>
  <li>Disattiva <strong>Screenshots</strong> o <strong>Screenshot</strong>.</li>
</ol>

<p>Da quel momento, i nuovi screenshot restano solo sul telefono. Se nella stessa
schermata è attiva l’opzione per copiare <em>tutte</em> le cartelle, disattivala
anche: altrimenti ogni nuova cartella creata da un’app verrà caricata da sola.</p>

<h2>Eliminare gli screenshot già caricati</h2>

<p>Disattivare il backup non elimina nulla di ciò che è già nel cloud. Per trovarli,
cerca <strong>«screenshot»</strong> in Google Foto: li raggruppa tutti. Selezionali,
eliminali e poi svuota il cestino, perché finché restano lì occupano ancora spazio.</p>

<p>Attenzione: eliminare uno screenshot dall’app Google Foto può cancellarlo anche dal
telefono. Se vuoi conservare la copia sul telefono, eliminalo da
<a href="https://photos.google.com">photos.google.com</a> dopo aver disattivato il
backup di quella cartella.</p>

<h2>E lo screenshot che vuoi davvero tenere?</h2>

<p>È il limite delle cartelle: o tutti gli screenshot o nessuno. Puoi caricarne uno a
mano (tienilo premuto in Google Foto e scegli <strong>Esegui backup</strong>), ma devi
ricordartene.</p>

<p>Se preferisci che sia il telefono a chiedertelo sul momento, è quello che fa
<strong>Snapgate</strong>: dopo ogni foto o screenshot ricevi una notifica con due
pulsanti, <em>Carica</em> o <em>Scarta</em>, e decidi senza aprire nulla. Ciò che
scarti resta sul telefono e non occupa mai spazio nel tuo account. Puoi anche creare
una regola perché gli screenshot non vengano mai caricati e solo le foto della
fotocamera ti facciano la domanda.</p>
""",
        },
    },
    "google-photos-storage-full": {
        "pt": {
            "title": "Google Fotos cheio: como libertar espaço sem perder as tuas fotos",
            "excerpt": "Quando os 15 GB enchem, o Google deixa de fazer cópia de "
                       "segurança. O que ocupa o espaço, como o recuperar e como "
                       "evitar que volte a acontecer.",
            "body": """
<p>Os 15 GB gratuitos do Google não são só para fotos: são partilhados pelo Google
Fotos, Gmail e Google Drive. Quando enchem, a cópia de segurança das fotos para, e no
Gmail podes deixar de receber emails. Antes de pagar por mais espaço, vale a pena ver
o que o está a ocupar.</p>

<h2>1. Vê o que ocupa o espaço</h2>

<p>No Google Fotos, toca na tua foto de perfil e entra em <strong>Definições do Fotos
→ Gerir armazenamento</strong> (ou abre <a href="https://one.google.com/storage">
one.google.com/storage</a>). Vês quanto gasta cada serviço e, no Fotos, uma ferramenta
que agrupa o que normalmente se pode apagar: <strong>fotos desfocadas, capturas de ecrã
e vídeos grandes</strong>.</p>

<h2>2. Começa pelos vídeos grandes</h2>

<p>Um minuto de vídeo em 4K ocupa tanto como centenas de fotos. Rever a lista de vídeos
grandes e apagar três ou quatro de que não precisas costuma libertar vários gigas de
uma vez, muito mais do que apagar fotos soltas.</p>

<h2>3. Capturas e fotos que eram só para um momento</h2>

<p>Capturas de ecrã, talões, o lugar do estacionamento, o quadro de uma reunião.
Pesquisa <strong>«capturas de ecrã»</strong> ou <strong>«recibos»</strong> no Google
Fotos: ele agrupa-os sozinho. Apaga-os e <strong>esvazia o caixote do lixo</strong>,
senão continuam a contar durante 60 dias.</p>

<h2>4. Verifica a qualidade da cópia</h2>

<p>Em <strong>Definições do Fotos → Cópia de segurança → Qualidade da cópia</strong>
podes escolher <strong>Poupança de espaço</strong> em vez de <em>Qualidade
original</em>. As fotos são ligeiramente comprimidas e os vídeos reduzidos a 1080p;
em fotos do telemóvel a diferença mal se nota. Atenção: só afeta o que carregares a
partir de agora.</p>

<h2>5. Que não volte a encher</h2>

<p>Libertar espaço funciona, mas se tudo continuar a ser carregado sozinho, daqui a uns
meses estás igual. O problema de fundo é que a cópia do Google Fotos é tudo ou nada:
carrega todas as fotos da câmara, também as que só querias para dez minutos.</p>

<p>Foi para isso que fizemos o <strong>Snapgate</strong>. Com a cópia do Google Fotos
desligada para a câmara, a app avisa-te assim que tiras uma foto ou fazes um vídeo e
escolhes <em>Carregar</em> ou <em>Descartar</em> na própria notificação. O que
descartas fica no telemóvel e nunca ocupa espaço na tua conta. E, se quiseres, comprime
as fotos antes de as carregar, como a poupança de espaço do Google.</p>
""",
        },
        "fr": {
            "title": "Stockage Google Photos plein : libérer de l’espace sans perdre vos photos",
            "excerpt": "Quand les 15 Go sont pleins, Google arrête la sauvegarde. Ce "
                       "qui occupe l’espace, comment le récupérer et comment éviter "
                       "que cela recommence.",
            "body": """
<p>Les 15 Go gratuits de Google ne servent pas qu’aux photos : Google Photos, Gmail et
Google Drive les partagent. Quand ils sont pleins, la sauvegarde des photos s’arrête,
et Gmail peut ne plus recevoir d’e-mails. Avant de payer pour plus d’espace, mieux
vaut voir ce qui l’occupe vraiment.</p>

<h2>1. Voir ce qui occupe l’espace</h2>

<p>Dans Google Photos, touchez votre photo de profil puis <strong>Paramètres de Photos
→ Gérer l’espace de stockage</strong> (ou ouvrez
<a href="https://one.google.com/storage">one.google.com/storage</a>). Vous verrez la
part de chaque service et, dans Photos, un outil qui regroupe ce qu’on peut
généralement supprimer : <strong>photos floues, captures d’écran et vidéos
volumineuses</strong>.</p>

<h2>2. Commencer par les grosses vidéos</h2>

<p>Une minute de vidéo en 4K occupe autant que des centaines de photos. Parcourir la
liste des vidéos volumineuses et en supprimer trois ou quatre inutiles libère souvent
plusieurs gigaoctets d’un coup, bien plus que supprimer des photos une par une.</p>

<h2>3. Captures et photos qui ne servaient qu’un instant</h2>

<p>Captures d’écran, tickets de caisse, la place de parking, le tableau d’une réunion.
Cherchez <strong>« captures d’écran »</strong> ou <strong>« reçus »</strong> dans
Google Photos : il les regroupe tout seul. Supprimez-les et <strong>videz la
corbeille</strong>, sinon elles comptent encore pendant 60 jours.</p>

<h2>4. Vérifier la qualité de sauvegarde</h2>

<p>Dans <strong>Paramètres de Photos → Sauvegarde → Qualité de la sauvegarde</strong>,
vous pouvez choisir <strong>Économiseur d’espace</strong> au lieu de <em>Qualité
d’origine</em>. Les photos sont légèrement compressées et les vidéos réduites en
1080p ; pour des photos de téléphone, la différence se voit à peine. Cela ne
s’applique qu’à ce que vous envoyez à partir de maintenant.</p>

<h2>5. Éviter que cela se remplisse à nouveau</h2>

<p>Libérer de l’espace fonctionne, mais si tout continue de partir automatiquement,
vous en serez au même point dans quelques mois. Le vrai problème, c’est que la
sauvegarde de Google Photos est tout ou rien : elle envoie chaque photo de l’appareil,
y compris celles qui ne vous servaient que dix minutes.</p>

<p>C’est pour cela que nous avons créé <strong>Snapgate</strong>. Avec la sauvegarde
Google Photos coupée pour l’appareil photo, l’app vous prévient dès que vous prenez
une photo ou une vidéo, et vous choisissez <em>Envoyer</em> ou <em>Écarter</em>
directement depuis la notification. Ce que vous écartez reste sur le téléphone et
n’occupe jamais d’espace dans votre compte. Et si vous le souhaitez, elle compresse
les photos avant l’envoi, comme l’économiseur d’espace de Google.</p>
""",
        },
        "de": {
            "title": "Google-Fotos-Speicher voll? So schaffst du Platz, ohne Fotos zu verlieren",
            "excerpt": "Wenn die 15 GB voll sind, stoppt Google die Sicherung. Was den "
                       "Platz belegt, wie du ihn zurückholst und wie du verhinderst, "
                       "dass es wieder passiert.",
            "body": """
<p>Die kostenlosen 15 GB von Google sind nicht nur für Fotos: Google Fotos, Gmail und
Google Drive teilen sie sich. Sind sie voll, stoppt die Fotosicherung, und Gmail
empfängt unter Umständen keine E-Mails mehr. Bevor du für mehr Speicher zahlst, lohnt
sich ein Blick darauf, was ihn eigentlich belegt.</p>

<h2>1. Schau nach, was den Platz belegt</h2>

<p>Tippe in Google Fotos auf dein Profilbild und gehe zu <strong>Fotos-Einstellungen →
Speicherplatz verwalten</strong> (oder öffne
<a href="https://one.google.com/storage">one.google.com/storage</a>). Du siehst, wie
viel jeder Dienst belegt, und in Fotos ein Werkzeug, das zusammenfasst, was sich meist
löschen lässt: <strong>unscharfe Fotos, Screenshots und große Videos</strong>.</p>

<h2>2. Fang mit den großen Videos an</h2>

<p>Eine Minute 4K-Video belegt so viel wie Hunderte Fotos. Die Liste großer Videos
durchzugehen und drei oder vier unnötige zu löschen, schafft oft mehrere Gigabyte auf
einmal – viel mehr als einzelne Fotos zu löschen.</p>

<h2>3. Screenshots und Fotos, die nur für einen Moment waren</h2>

<p>Screenshots, Kassenbons, der Parkplatz, das Whiteboard aus einem Meeting. Suche in
Google Fotos nach <strong>„Screenshots“</strong> oder <strong>„Belege“</strong>: Die
App gruppiert sie von selbst. Lösche sie und <strong>leere den Papierkorb</strong>,
sonst zählen sie noch 60 Tage mit.</p>

<h2>4. Prüfe die Sicherungsqualität</h2>

<p>Unter <strong>Fotos-Einstellungen → Sicherung → Sicherungsqualität</strong> kannst
du <strong>Speicherplatz sparen</strong> statt <em>Originalqualität</em> wählen. Fotos
werden leicht komprimiert und Videos auf 1080p verkleinert; bei Handyfotos sieht man
den Unterschied kaum. Achtung: Das gilt nur für alles, was du ab jetzt hochlädst.</p>

<h2>5. Damit er nicht wieder vollläuft</h2>

<p>Platz schaffen funktioniert, aber wenn weiter alles von selbst hochgeladen wird,
stehst du in ein paar Monaten wieder hier. Das eigentliche Problem: Die Sicherung von
Google Fotos ist alles oder nichts. Sie lädt jedes Kamerafoto hoch, auch die, die du
nur für zehn Minuten brauchtest.</p>

<p>Deshalb haben wir <strong>Snapgate</strong> gebaut. Ist die Google-Fotos-Sicherung
für die Kamera ausgeschaltet, meldet sich die App, sobald du ein Foto oder Video
machst, und du wählst direkt in der Benachrichtigung <em>Hochladen</em> oder
<em>Verwerfen</em>. Was du verwirfst, bleibt auf dem Handy und belegt nie Platz in
deinem Konto. Und wenn du willst, verkleinert sie Fotos vor dem Hochladen, wie das
Speicherplatz-Sparen von Google.</p>
""",
        },
        "it": {
            "title": "Spazio Google Foto pieno: come liberarlo senza perdere le tue foto",
            "excerpt": "Quando i 15 GB sono pieni, Google smette di fare il backup. "
                       "Cosa occupa lo spazio, come recuperarlo e come evitare che "
                       "succeda di nuovo.",
            "body": """
<p>I 15 GB gratuiti di Google non sono solo per le foto: li condividono Google Foto,
Gmail e Google Drive. Quando si riempiono, il backup delle foto si ferma e Gmail può
smettere di ricevere email. Prima di pagare per altro spazio, conviene vedere cosa lo
sta occupando.</p>

<h2>1. Guarda cosa occupa lo spazio</h2>

<p>In Google Foto, tocca la tua foto del profilo e vai in <strong>Impostazioni di Foto
→ Gestisci spazio di archiviazione</strong> (oppure apri
<a href="https://one.google.com/storage">one.google.com/storage</a>). Vedrai quanto usa
ogni servizio e, in Foto, uno strumento che raggruppa ciò che di solito si può
eliminare: <strong>foto sfocate, screenshot e video di grandi dimensioni</strong>.</p>

<h2>2. Inizia dai video grandi</h2>

<p>Un minuto di video in 4K occupa quanto centinaia di foto. Scorrere l’elenco dei
video grandi ed eliminarne tre o quattro che non ti servono libera spesso diversi
gigabyte in un colpo, molto più che eliminare foto singole.</p>

<h2>3. Screenshot e foto che servivano solo per un momento</h2>

<p>Screenshot, scontrini, il posto del parcheggio, la lavagna di una riunione. Cerca
<strong>«screenshot»</strong> o <strong>«ricevute»</strong> in Google Foto: li
raggruppa da solo. Eliminali e <strong>svuota il cestino</strong>, altrimenti
continuano a contare per 60 giorni.</p>

<h2>4. Controlla la qualità del backup</h2>

<p>In <strong>Impostazioni di Foto → Backup → Qualità del backup</strong> puoi scegliere
<strong>Risparmio spazio</strong> invece di <em>Qualità originale</em>. Le foto vengono
leggermente compresse e i video ridotti a 1080p; per le foto del telefono la differenza
si nota appena. Attenzione: vale solo per ciò che carichi da adesso in poi.</p>

<h2>5. Perché non si riempia di nuovo</h2>

<p>Liberare spazio funziona, ma se tutto continua a caricarsi da solo, tra qualche mese
sarai di nuovo qui. Il problema di fondo è che il backup di Google Foto è tutto o
niente: carica ogni foto della fotocamera, anche quelle che ti servivano per dieci
minuti.</p>

<p>Per questo abbiamo creato <strong>Snapgate</strong>. Con il backup di Google Foto
disattivato per la fotocamera, l’app ti avvisa appena scatti una foto o giri un video
e scegli <em>Carica</em> o <em>Scarta</em> direttamente dalla notifica. Ciò che scarti
resta sul telefono e non occupa mai spazio nel tuo account. E, se vuoi, comprime le foto
prima di caricarle, come il risparmio spazio di Google.</p>
""",
        },
    },
    "back-up-only-some-photos-google-photos": {
        "pt": {
            "title": "Como carregar só algumas fotos para o Google Fotos (e não todas)",
            "excerpt": "A cópia do Google Fotos é tudo ou nada. Três formas de escolher "
                       "que fotos chegam à nuvem, da mais manual à mais cómoda.",
            "body": """
<p>A cópia de segurança do Google Fotos tem duas posições: ativa, e carrega todas as
fotos da câmara; desativada, e não carrega nenhuma. Não há meio-termo para dizer
«esta sim, esta não». Mas há formas de lá chegar.</p>

<h2>Opção 1: desligar a cópia e carregar à mão</h2>

<p>Desativa a cópia em <strong>Definições do Fotos → Cópia de segurança</strong>. As
fotos continuam a aparecer no Google Fotos, mas só no telemóvel. Quando quiseres
guardar uma na nuvem, mantém-na premida, seleciona as que quiseres e toca em
<strong>Fazer cópia de segurança</strong>.</p>

<p><strong>Bom:</strong> controlo total e gratuito. <strong>Mau:</strong> tens de te
lembrar. Se um dia não o fizeres e perderes o telemóvel, essas fotos perdem-se com
ele.</p>

<h2>Opção 2: decidir por pastas</h2>

<p>Em <strong>Definições do Fotos → Cópia de segurança</strong>, na parte das pastas do
dispositivo, podes escolher que pastas são copiadas: a câmara sim, as capturas ou as
fotos do WhatsApp não.</p>

<p><strong>Bom:</strong> automático. <strong>Mau:</strong> dentro da pasta da câmara
continua a ser tudo ou nada. O talão das compras e a foto da tua filha estão na mesma
pasta.</p>

<h2>Opção 3: o telemóvel pergunta-te em cada foto</h2>

<p>É o que faz o <strong>Snapgate</strong>, uma app que criámos precisamente para isto.
Desliga-se a cópia do Google Fotos para a pasta da câmara e, a partir daí, sempre que
tiras uma foto ou fazes um vídeo recebes uma notificação com dois botões:
<em>Carregar</em> ou <em>Descartar</em>. Decides no momento, quando ainda sabes para
que a tiraste, sem abrir nenhuma app.</p>

<ul>
  <li>O que descartas <strong>não é apagado</strong>: fica no telemóvel.</li>
  <li>Podes rever várias de uma vez, em ecrã inteiro, se tirares uma rajada.</li>
  <li>Regras automáticas: por exemplo, que as capturas nunca sejam carregadas ou que o
  que fazes em horário de trabalho não vá para a tua conta pessoal.</li>
  <li>Modos temporários: «carrega tudo durante a viagem» ou «não carregues nada esta
  tarde», e desligam-se sozinhos.</li>
</ul>

<p>O Google está a testar uma cópia só das fotos que marcas como favoritas, que pode
ajudar algumas pessoas. A diferença é o momento: com favoritos tens de ir depois marcar
cada foto; com o Snapgate decides ao tirá-la, na notificação.</p>
""",
        },
        "fr": {
            "title": "Comment sauvegarder seulement certaines photos sur Google Photos",
            "excerpt": "La sauvegarde de Google Photos, c’est tout ou rien. Trois façons "
                       "de choisir quelles photos partent dans le cloud, de la plus "
                       "manuelle à la plus simple.",
            "body": """
<p>La sauvegarde de Google Photos a deux positions : activée, elle envoie chaque photo
de l’appareil ; désactivée, elle n’en envoie aucune. Pas de juste milieu pour dire
« celle-ci oui, celle-là non ». Mais il existe des moyens d’y arriver.</p>

<h2>Option 1 : couper la sauvegarde et envoyer à la main</h2>

<p>Désactivez la sauvegarde dans <strong>Paramètres de Photos → Sauvegarde</strong>.
Vos photos apparaissent toujours dans Google Photos, mais uniquement sur le téléphone.
Quand vous voulez en mettre une dans le cloud, faites un appui long, sélectionnez celles
que vous voulez et touchez <strong>Sauvegarder</strong>.</p>

<p><strong>Avantage :</strong> contrôle total, et gratuit. <strong>Inconvénient :</strong>
il faut y penser. Si vous oubliez un jour et perdez votre téléphone, ces photos
disparaissent avec lui.</p>

<h2>Option 2 : décider par dossier</h2>

<p>Dans <strong>Paramètres de Photos → Sauvegarde</strong>, dans la partie des dossiers
de l’appareil, vous pouvez choisir les dossiers sauvegardés : l’appareil photo oui,
les captures d’écran ou les images WhatsApp non.</p>

<p><strong>Avantage :</strong> automatique. <strong>Inconvénient :</strong> dans le
dossier de l’appareil photo, c’est toujours tout ou rien. Le ticket de caisse et la
photo de votre enfant sont dans le même dossier.</p>

<h2>Option 3 : le téléphone vous demande à chaque photo</h2>

<p>C’est ce que fait <strong>Snapgate</strong>, une app que nous avons créée exactement
pour cela. On coupe la sauvegarde Google Photos du dossier de l’appareil photo et,
ensuite, à chaque photo ou vidéo, une notification apparaît avec deux boutons :
<em>Envoyer</em> ou <em>Écarter</em>. Vous décidez sur le moment, quand vous savez
encore pourquoi vous l’avez prise, sans ouvrir aucune app.</p>

<ul>
  <li>Ce que vous écartez <strong>n’est pas supprimé</strong> : il reste sur le
  téléphone.</li>
  <li>Revoyez une rafale d’un coup, en plein écran.</li>
  <li>Règles automatiques : par exemple, les captures d’écran ne partent jamais, ou
  les photos prises pendant les heures de travail ne vont pas sur votre compte
  personnel.</li>
  <li>Modes temporaires : « tout envoyer pendant le voyage » ou « ne rien envoyer cet
  après-midi », qui s’arrêtent d’eux-mêmes.</li>
</ul>

<p>Google teste une sauvegarde des seules photos marquées comme favorites, qui peut
aider certaines personnes. La différence, c’est le moment : avec les favoris, il faut
revenir plus tard marquer chaque photo ; avec Snapgate, vous décidez en la prenant,
depuis la notification.</p>
""",
        },
        "de": {
            "title": "Nur bestimmte Fotos in Google Fotos sichern (statt aller)",
            "excerpt": "Die Sicherung von Google Fotos ist alles oder nichts. Drei Wege, "
                       "selbst zu wählen, welche Fotos in die Cloud kommen – von ganz "
                       "manuell bis mühelos.",
            "body": """
<p>Die Sicherung von Google Fotos kennt zwei Stellungen: an, und sie lädt jedes
Kamerafoto hoch; aus, und sie lädt keines hoch. Einen Mittelweg für „dieses ja, dieses
nein“ gibt es nicht. Aber man kann trotzdem dorthin kommen.</p>

<h2>Option 1: Sicherung aus und von Hand hochladen</h2>

<p>Schalte die Sicherung unter <strong>Fotos-Einstellungen → Sicherung</strong> aus.
Deine Fotos erscheinen weiter in Google Fotos, aber nur auf dem Handy. Willst du eines
in der Cloud haben, drücke lange darauf, wähle die gewünschten aus und tippe auf
<strong>Sichern</strong>.</p>

<p><strong>Gut:</strong> volle Kontrolle, kostenlos. <strong>Schlecht:</strong> Du
musst daran denken. Vergisst du es einmal und verlierst das Handy, sind diese Fotos mit
weg.</p>

<h2>Option 2: nach Ordnern entscheiden</h2>

<p>Unter <strong>Fotos-Einstellungen → Sicherung</strong> kannst du bei den
Geräteordnern wählen, welche gesichert werden: die Kamera ja, Screenshots oder
WhatsApp-Bilder nein.</p>

<p><strong>Gut:</strong> automatisch. <strong>Schlecht:</strong> Innerhalb des
Kameraordners bleibt es alles oder nichts. Der Kassenbon und das Foto deiner Tochter
liegen im selben Ordner.</p>

<h2>Option 3: Das Handy fragt dich bei jedem Foto</h2>

<p>Genau das macht <strong>Snapgate</strong>, eine App, die wir genau dafür gebaut
haben. Die Google-Fotos-Sicherung wird für den Kameraordner ausgeschaltet, und danach
bekommst du bei jedem Foto oder Video eine Benachrichtigung mit zwei Knöpfen:
<em>Hochladen</em> oder <em>Verwerfen</em>. Du entscheidest im Moment, solange du noch
weißt, warum du es gemacht hast – ohne eine App zu öffnen.</p>

<ul>
  <li>Was du verwirfst, wird <strong>nicht gelöscht</strong>: Es bleibt auf dem
  Handy.</li>
  <li>Serienbilder kannst du gesammelt im Vollbild durchgehen.</li>
  <li>Automatische Regeln: zum Beispiel, dass Screenshots nie hochgeladen werden oder
  Fotos aus der Arbeitszeit nicht in dein privates Konto gehen.</li>
  <li>Zeitlich begrenzte Modi: „auf der Reise alles hochladen“ oder „heute Nachmittag
  nichts hochladen“, und sie schalten sich von selbst ab.</li>
</ul>

<p>Google testet eine Sicherung nur der Fotos, die du als Favoriten markierst; das kann
manchen helfen. Der Unterschied ist der Zeitpunkt: Bei Favoriten markierst du später
jedes Foto einzeln; mit Snapgate entscheidest du beim Fotografieren, direkt in der
Benachrichtigung.</p>
""",
        },
        "it": {
            "title": "Come caricare solo alcune foto su Google Foto (e non tutte)",
            "excerpt": "Il backup di Google Foto è tutto o niente. Tre modi per scegliere "
                       "quali foto arrivano nel cloud, dal più manuale al più comodo.",
            "body": """
<p>Il backup di Google Foto ha due posizioni: attivo, e carica ogni foto della
fotocamera; disattivo, e non ne carica nessuna. Non c’è una via di mezzo per dire
«questa sì, questa no». Ma ci sono modi per arrivarci.</p>

<h2>Opzione 1: disattivare il backup e caricare a mano</h2>

<p>Disattiva il backup in <strong>Impostazioni di Foto → Backup</strong>. Le foto
continuano ad apparire in Google Foto, ma solo sul telefono. Quando ne vuoi una nel
cloud, tienila premuta, seleziona quelle che vuoi e tocca <strong>Esegui
backup</strong>.</p>

<p><strong>Pro:</strong> controllo totale, gratis. <strong>Contro:</strong> devi
ricordartene. Se un giorno te ne dimentichi e perdi il telefono, quelle foto se ne vanno
con lui.</p>

<h2>Opzione 2: decidere per cartelle</h2>

<p>In <strong>Impostazioni di Foto → Backup</strong>, nella parte delle cartelle del
dispositivo, puoi scegliere quali cartelle copiare: la fotocamera sì, gli screenshot o
le immagini di WhatsApp no.</p>

<p><strong>Pro:</strong> automatico. <strong>Contro:</strong> dentro la cartella della
fotocamera resta tutto o niente. Lo scontrino della spesa e la foto di tua figlia sono
nella stessa cartella.</p>

<h2>Opzione 3: il telefono ti chiede per ogni foto</h2>

<p>È quello che fa <strong>Snapgate</strong>, un’app che abbiamo creato proprio per
questo. Si disattiva il backup di Google Foto per la cartella della fotocamera e, da
lì in poi, ogni volta che scatti una foto o giri un video ricevi una notifica con due
pulsanti: <em>Carica</em> o <em>Scarta</em>. Decidi sul momento, quando sai ancora
perché l’hai scattata, senza aprire nessuna app.</p>

<ul>
  <li>Ciò che scarti <strong>non viene eliminato</strong>: resta sul telefono.</li>
  <li>Puoi rivedere una raffica tutta insieme, a schermo intero.</li>
  <li>Regole automatiche: per esempio, che gli screenshot non vengano mai caricati o
  che ciò che scatti in orario di lavoro non finisca nel tuo account personale.</li>
  <li>Modalità temporanee: «carica tutto durante il viaggio» o «non caricare niente
  oggi pomeriggio», e si spengono da sole.</li>
</ul>

<p>Google sta testando un backup delle sole foto che segni come preferite, che può
aiutare alcune persone. La differenza è il momento: con i preferiti devi tornare dopo
a segnare ogni foto; con Snapgate decidi quando la scatti, dalla notifica.</p>
""",
        },
    },
}

for _guide in GUIDES:
    for _lang, _t in _T[_guide["slug"]].items():
        _text, _button = _CTA[_lang]
        _guide["langs"][_lang] = {
            "title": _t["title"],
            "date_label": _DATE[_lang],
            "excerpt": _t["excerpt"],
            "body": _t["body"] + cta(_guide["slug"], _text, _button),
        }
