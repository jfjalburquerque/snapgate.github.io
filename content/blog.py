# -*- coding: utf-8 -*-
"""Artículos del blog.

Cada entrada declara en qué idiomas existe. El generador solo la publica en esos,
y el índice de los demás idiomas muestra un aviso en lugar de una lista vacía.
"""

BLOG_INDEX = {
    "es": {
        "title": "Blog · Snapgate",
        "h1": "Blog",
        "lede": "Por qué existe esta app, cómo se tomaron las decisiones y qué "
                "aprendimos peleándonos con Android.",
        "empty": "Todavía no hay artículos en este idioma.",
    },
    "en": {
        "title": "Blog · Snapgate",
        "h1": "Blog",
        "lede": "Why this app exists, how the decisions were made, and what we "
                "learned fighting Android.",
        "empty": "No posts in this language yet.",
    },
    "pt": {
        "title": "Blog · Snapgate",
        "h1": "Blog",
        "lede": "Porque existe esta app e o que aprendemos a construí-la.",
        "empty": "Ainda não há artigos neste idioma. Estão disponíveis em "
                 "<a href=\"../../es/blog/\">espanhol</a> e "
                 "<a href=\"../../en/blog/\">inglês</a>.",
    },
    "fr": {
        "title": "Blog · Snapgate",
        "h1": "Blog",
        "lede": "Pourquoi cette app existe et ce que nous avons appris en la construisant.",
        "empty": "Pas encore d'articles dans cette langue. Ils sont disponibles en "
                 "<a href=\"../../es/blog/\">espagnol</a> et en "
                 "<a href=\"../../en/blog/\">anglais</a>.",
    },
    "de": {
        "title": "Blog · Snapgate",
        "h1": "Blog",
        "lede": "Warum es diese App gibt und was wir beim Bauen gelernt haben.",
        "empty": "Noch keine Beiträge in dieser Sprache. Verfügbar auf "
                 "<a href=\"../../es/blog/\">Spanisch</a> und "
                 "<a href=\"../../en/blog/\">Englisch</a>.",
    },
    "it": {
        "title": "Blog · Snapgate",
        "h1": "Blog",
        "lede": "Perché esiste questa app e cosa abbiamo imparato costruendola.",
        "empty": "Ancora nessun articolo in questa lingua. Disponibili in "
                 "<a href=\"../../es/blog/\">spagnolo</a> e "
                 "<a href=\"../../en/blog/\">inglese</a>.",
    },
}

POSTS = [
    {
        "slug": "why-snapgate",
        "date": "2026-09-14",
        "langs": {
            "es": {
                "title": "Por qué existe Snapgate",
                "date_label": "14 de septiembre de 2026",
                "excerpt": "Casi todas las fotos que llenan mi nube son documentos "
                           "que fotografié para mirarlos diez minutos.",
                "body": """
<p>Un día miré por qué se me había llenado el almacenamiento de Google y la respuesta
me dio un poco de vergüenza. No eran vacaciones ni cumpleaños. Eran tickets de
parking, facturas, la matrícula del coche en la planta 3 del aeropuerto, el wifi de
un hotel, la talla de una camisa, la pizarra de una reunión que terminó hace año y
medio.</p>

<p>Fotos que hice para mirarlas diez minutos y que llevan años pagando alquiler en
mi cuenta.</p>

<h2>El problema no es la cámara, es el todo o nada</h2>

<p>La copia de seguridad de Google Fotos tiene exactamente dos estados: encendida
para una carpeta entera, o apagada. No hay término medio. O sube todo tu carrete, o
no sube nada y asumes el riesgo de perder las fotos que sí importan.</p>

<p>Como no hay matiz posible, la inmensa mayoría de la gente lo deja encendido y paga
por almacenar basura. Es un diseño perfectamente razonable desde el punto de vista de
Google, y perfectamente incómodo desde el mío.</p>

<h2>Solo hay dos formas de arreglarlo</h2>

<p>La primera es revisar el carrete cada cierto tiempo y borrar a mano. En teoría
funciona. En la práctica no lo hace nadie, porque es una tarea sin recompensa
inmediata que siempre puede esperar a mañana.</p>

<p>La segunda es decidir en el momento. Cuando haces la foto del ticket, sabes
perfectamente que no la quieres para siempre. Esa información existe justo en ese
instante y se evapora treinta segundos después. Snapgate no es más que un intento de
capturarla antes de que se pierda.</p>

<h2>Lo que aprendí construyéndolo</h2>

<p>La primera versión preguntaba foto a foto con una notificación. Me pareció obvio.
Luego hice seis fotos seguidas de un plato y recibí seis notificaciones, y entendí
que el diseño obvio era el equivocado.</p>

<p>La versión que ha sobrevivido agrupa: un solo aviso que se reescribe, con dos
botones dentro. Decides sin abrir nada, y si haces una ráfaga sigue siendo una sola
interrupción. Es menos elegante de explicar y mucho mejor de usar.</p>

<h2>Lo que Snapgate no resuelve</h2>

<p>Conviene ser honesto: esta app evita que se llene <em>tu nube</em>, no tu móvil.
La foto del ticket que descartas sigue ocupando tres megas en el teléfono. Hubo un
momento en el que pensé en añadir caducidad —que las fotos marcadas desaparecieran
solas a los siete días— y lo dejé fuera a propósito.</p>

<p>Borrar es irreversible a ojos del usuario, aunque técnicamente sea la papelera. Si
una app se equivoca una sola vez y desaparece una foto que importaba, la desinstalas
para siempre y con razón. Prefiero una app que haga menos y en la que puedas confiar
del todo.</p>
""",
            },
            "en": {
                "title": "Why Snapgate exists",
                "date_label": "14 September 2026",
                "excerpt": "Almost every photo filling my cloud is a document I "
                           "photographed to look at for ten minutes.",
                "body": """
<p>One day I looked into why my Google storage was full, and the answer was mildly
embarrassing. Not holidays. Not birthdays. Parking tickets, receipts, my car's bay
number on level 3 of an airport, a hotel wifi password, a shirt size, a whiteboard
from a meeting that ended eighteen months ago.</p>

<p>Photos I took to look at for ten minutes, paying rent in my account ever since.</p>

<h2>The problem isn't the camera, it's all-or-nothing</h2>

<p>Google Photos backup has exactly two states: on for an entire folder, or off.
There is no middle ground. Either it uploads your whole camera roll, or it uploads
nothing and you accept the risk of losing the photos that actually matter.</p>

<p>Since no nuance is possible, most people leave it on and pay to store rubbish. It
is a perfectly reasonable design from Google's point of view, and a perfectly
annoying one from mine.</p>

<h2>There are only two ways to fix it</h2>

<p>The first is to review your camera roll periodically and delete by hand. It works
in theory. In practice nobody does it, because it is a chore with no immediate reward
that can always wait until tomorrow.</p>

<p>The second is to decide in the moment. When you photograph a receipt, you know
perfectly well you don't want it forever. That information exists precisely then, and
evaporates thirty seconds later. Snapgate is nothing more than an attempt to capture
it before it's gone.</p>

<h2>What I learned building it</h2>

<p>The first version asked photo by photo with a notification. It seemed obvious.
Then I took six shots of the same plate and got six notifications, and understood
that the obvious design was the wrong one.</p>

<p>The version that survived groups them: a single notification that rewrites itself,
with two buttons inside. You decide without opening anything, and a burst is still
one interruption. It's less elegant to explain and far better to use.</p>

<h2>What Snapgate does not solve</h2>

<p>Worth being honest: this app stops <em>your cloud</em> filling up, not your phone.
The receipt photo you discard still takes three megabytes on the device. At one point
I considered adding expiry — marked photos disappearing on their own after seven days
— and deliberately left it out.</p>

<p>Deleting is irreversible in the user's eyes, even when it technically goes to the
bin. If an app gets it wrong once and a photo that mattered disappears, you uninstall
it forever, and rightly so. I would rather ship an app that does less and that you
can trust completely.</p>
""",
            },
        },
    },
]

POSTS.append({
    "slug": "decide-from-the-notification",
    "date": "2026-09-13",
    "langs": {
        "es": {
            "title": "Por qué decides desde la notificación",
            "date_label": "13 de septiembre de 2026",
            "excerpt": "Un botón en la notificación parece un detalle de interfaz. "
                       "En realidad viene impuesto por cómo Android protege tus ficheros.",
            "body": """
<p>Snapgate te deja resolver desde la propia notificación: dos botones, Descartar y
Subir, sin abrir la app. Parece una decisión de diseño cómoda. En realidad está
condicionada por una regla del sistema que casi nadie conoce.</p>

<h2>Mover un fichero ajeno requiere permiso; copiarlo no</h2>

<p>Desde Android 10, una app no puede tocar libremente ficheros que no ha creado.
Para mover una foto que hizo la cámara hay que pedir consentimiento con un diálogo
del sistema, y ese diálogo <strong>solo lo puede lanzar una Activity</strong>: es
decir, la app tiene que estar abierta en pantalla.</p>

<p>Si «Subir» tuviera que mover el fichero, pulsar el botón abriría la app y te
pondría delante otro diálogo. Dos toques más y la promesa de decidir en un gesto se
va al traste.</p>

<p>Pero copiar es otra historia. El fichero copiado lo creamos nosotros, así que no
hace falta permiso de nadie y funciona perfectamente en segundo plano. Por eso el
botón de la notificación copia en lugar de mover, y el original queda apuntado en una
cola de limpieza que se vacía después de una sola vez, con un único diálogo para todo
el lote.</p>

<p>Ese es el precio, y es un precio real: durante un rato tienes la foto duplicada en
el móvil. Nos pareció mejor que romper el gesto de un toque.</p>

<h2>Cuando hay cuenta de Google, el precio desaparece</h2>

<p>Todo lo anterior aplica a la ruta por carpetas, que es el plan B. Con la cuenta
conectada, Snapgate sube la foto directamente por la API de Google Photos, y para eso
solo necesita <em>leer</em> los bytes. Leer ya lo tenemos permitido.</p>

<p>Resultado: sin mover, sin copiar, sin duplicados y sin diálogos. Esa es la razón de
que la cuenta de Google pasara de ser una función opcional escondida en ajustes a ser
el camino principal del producto.</p>

<h2>La ventana de decisión</h2>

<p>Hay un detalle que nació de una conversación y resultó ser estructural: una foto
solo se te ofrece durante sus primeros minutos. Si no contestas, se queda en el móvil
sin subir y deja de preguntar.</p>

<p>Suena a comodidad, y también es una red de seguridad. Impide que una instalación
nueva —o un fallo en el cálculo de qué es «reciente»— te plante delante las novecientas
fotos de tu carrete pidiéndote que decidas una por una. Nos pasó durante el desarrollo,
y la ventana lo hace imposible pase lo que pase.</p>
""",
        },
        "en": {
            "title": "Why you decide from the notification",
            "date_label": "13 September 2026",
            "excerpt": "A button in a notification looks like an interface detail. "
                       "It is actually forced by how Android protects your files.",
            "body": """
<p>Snapgate lets you resolve things from the notification itself: two buttons, Discard
and Upload, without opening the app. It looks like a convenience decision. It is
actually shaped by a system rule most people never hear about.</p>

<h2>Moving someone else's file needs permission; copying doesn't</h2>

<p>Since Android 10, an app cannot freely touch files it did not create. To move a
photo the camera took, you must request consent through a system dialog — and that
dialog <strong>can only be launched by an Activity</strong>, meaning the app has to be
open on screen.</p>

<p>If "Upload" had to move the file, tapping the button would open the app and put
another dialog in front of you. Two extra taps, and the promise of deciding in one
gesture is gone.</p>

<p>Copying is a different story. We create the copied file, so no permission is needed
and it works perfectly in the background. That's why the notification button copies
instead of moving, and the original goes into a cleanup queue that is emptied later in
one go, with a single dialog for the whole batch.</p>

<p>That is the price, and it is a real one: for a while the photo exists twice on your
phone. It seemed better than breaking the one-tap gesture.</p>

<h2>With a Google account, the price disappears</h2>

<p>All of the above applies to the folder route, which is the fallback. With the account
connected, Snapgate uploads directly through the Google Photos API, and for that it only
needs to <em>read</em> the bytes. Reading is already permitted.</p>

<p>The result: no moving, no copying, no duplicates and no dialogs. That is why the
Google account went from being an optional feature hidden in settings to being the main
road of the product.</p>

<h2>The decision window</h2>

<p>One detail came out of a conversation and turned out to be structural: a photo is only
offered during its first few minutes. If you don't answer, it stays on the phone
un-uploaded and stops asking.</p>

<p>It sounds like a convenience, and it is also a safety net. It makes it impossible for a
fresh install — or a bug in working out what counts as "recent" — to drop nine hundred
camera-roll photos in front of you asking you to decide one by one. That happened during
development, and the window makes it impossible regardless.</p>
""",
        },
    },
})

POSTS.append({
    "slug": "the-night-the-phone-froze-us",
    "date": "2026-09-13",
    "langs": {
        "es": {
            "title": "La noche que el móvil nos congeló sin avisar",
            "date_label": "13 de septiembre de 2026",
            "excerpt": "Perseguimos durante horas un fallo que no existía. El "
                       "culpable era el ahorro de batería del fabricante.",
            "body": """
<p>La app estaba terminada, instalada y funcionando. Hacías una foto y no pasaba nada.
Ni notificación, ni traza, ni error. Silencio.</p>

<h2>Todo lo que comprobamos, y todo lo que salió bien</h2>

<p>El servicio estaba vivo y en primer plano. Los permisos, concedidos. La foto,
correctamente indexada por el sistema con un identificador más alto que nuestra línea
base. El proceso, sin congelar según el propio Android. Ninguna restricción declarada
en la configuración de la app.</p>

<p>Cada comprobación descartaba una hipótesis y nos dejaba con menos sitios donde
mirar.</p>

<h2>El error de diagnóstico</h2>

<p>Concluimos que el mecanismo de aviso de cambios del sistema estaba silenciado para
apps en segundo plano, y construimos una alternativa: un sondeo periódico. Tampoco
funcionó.</p>

<p>Entonces hicimos lo que deberíamos haber hecho al principio: añadir un latido. Una
traza cada pocos segundos diciendo simplemente «sigo aquí». Y ahí apareció el patrón.
El latido se paraba unos treinta segundos después de salir de la app, y no volvía.</p>

<p>No era que no nos llegaran los avisos. Es que <strong>no se estaba ejecutando nada</strong>.
El fabricante congelaba el proceso entero, con su servicio en primer plano y todo,
sin matarlo y sin reportarlo por ninguno de los canales que habíamos consultado.</p>

<h2>La solución tenía un interruptor</h2>

<p>Quitarle a la app las restricciones de batería en los ajustes del sistema. Un
interruptor. Con eso funcionó a la primera, y además reveló que nuestro diagnóstico era
falso: el mecanismo original nunca había estado roto, y el aviso llegaba en 415
milisegundos.</p>

<h2>Lo que nos llevamos</h2>

<p><strong>Un fallo silencioso es peor que uno ruidoso.</strong> Si el sistema nos
hubiera dicho «he congelado esta app», habríamos tardado cinco minutos. Al no decir
nada, gastamos horas construyendo una solución a un problema inexistente.</p>

<p><strong>Instrumenta el camino feliz, no solo los errores.</strong> Solo registrábamos
trazas cuando detectábamos algo. Por eso no podíamos distinguir «no ha pasado nada» de
«estoy muerto», que son dos situaciones con arreglos opuestos.</p>

<p><strong>Y sobre todo: eso le va a pasar a tus usuarios.</strong> No es una anécdota de
desarrollo. Cualquiera que instale la app en un móvil de esos fabricantes va a vivir
exactamente lo mismo, sin trazas y sin saber por qué. Por eso quitar la restricción de
batería dejó de ser una nota en el manual y pasó a ser un paso propio del alta, con su
estado comprobado por la app: si no está hecho, te lo dice y te lleva allí.</p>
""",
        },
        "en": {
            "title": "The night the phone froze us without saying so",
            "date_label": "13 September 2026",
            "excerpt": "We chased a bug that did not exist for hours. The culprit was "
                       "the manufacturer's battery saver.",
            "body": """
<p>The app was finished, installed and running. You took a photo and nothing happened.
No notification, no log line, no error. Silence.</p>

<h2>Everything we checked, and everything that was fine</h2>

<p>The service was alive and in the foreground. Permissions granted. The photo correctly
indexed by the system with an identifier higher than our baseline. The process not frozen
according to Android itself. No restrictions declared in the app's own configuration.</p>

<p>Every check ruled out a hypothesis and left us with fewer places to look.</p>

<h2>The misdiagnosis</h2>

<p>We concluded that the system's change-notification mechanism was being muted for
background apps, and built an alternative: periodic polling. That didn't work either.</p>

<p>Then we did what we should have done at the start: add a heartbeat. A log line every
few seconds saying simply "still here". And the pattern appeared. The heartbeat stopped
about thirty seconds after leaving the app, and never came back.</p>

<p>It wasn't that notifications weren't reaching us. It was that <strong>nothing was
running at all</strong>. The manufacturer was freezing the entire process, foreground
service and all, without killing it and without reporting it through any of the channels
we had checked.</p>

<h2>The fix was a single switch</h2>

<p>Removing the app's battery restrictions in the system settings. One switch. It worked
first time, and revealed that our diagnosis had been wrong: the original mechanism had
never been broken, and the notification arrived in 415 milliseconds.</p>

<h2>What we took away</h2>

<p><strong>A silent failure is worse than a loud one.</strong> Had the system told us "I
froze this app", it would have taken five minutes. Saying nothing, it cost us hours
building a solution to a problem that didn't exist.</p>

<p><strong>Instrument the happy path, not just the errors.</strong> We only logged when we
detected something. That meant we could not tell "nothing happened" apart from "I am
dead" — two situations with opposite fixes.</p>

<p><strong>And above all: this will happen to your users.</strong> It isn't a development
anecdote. Anyone installing the app on one of those phones will experience exactly the
same thing, without logs and without knowing why. That is why removing the battery
restriction stopped being a note in the manual and became a step in the setup flow, with
its state verified by the app: if it isn't done, it tells you and takes you there.</p>
""",
        },
    },
})
