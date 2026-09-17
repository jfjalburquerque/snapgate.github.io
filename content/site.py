# -*- coding: utf-8 -*-
"""Cabecera, pie y portada, por idioma."""

LANGS = ["es", "en", "pt", "fr", "de", "it"]

LANG_NAMES = {
    "es": "Español",
    "en": "English",
    "pt": "Português",
    "fr": "Français",
    "de": "Deutsch",
    "it": "Italiano",
}

UI = {}
LANDING = {}

# --------------------------------------------------------------------------
# Español
# --------------------------------------------------------------------------

UI["es"] = {
    "nav_how": "Cómo funciona",
    "nav_privacy": "Privacidad",
    "nav_terms": "Términos",
    "nav_blog": "Blog",
    "footer_tagline": "tú decides qué sube a la nube",
    "footer_rights": "Hecho en España.",
}

LANDING["es"] = {
    "title": "Snapgate · Decide qué fotos llegan a tu nube",
    "description": "Google Fotos sube tu carrete entero o no sube nada. "
                   "Snapgate te deja decidir foto a foto, desde la notificación.",
    "h1": "Tu nube se llena de fotos que nunca quisiste guardar",
    "lede": "El ticket del parking, la factura, la pizarra de una reunión. "
            "Google Fotos sube tu carrete entero o no sube nada. Snapgate mete "
            "un portero en medio.",
    "cta_primary": "Cómo funciona",
    "cta_secondary": "Por qué la hicimos",
    "note": "Android 11 o superior · Pago único, sin suscripción",

    "problem_h2": "El problema no es tu cámara, es el todo o nada",
    "problem_sub": "La copia de seguridad de Google Fotos solo tiene dos "
                   "estados: encendida para toda una carpeta, o apagada. No "
                   "hay término medio, y por eso tu almacenamiento se llena de "
                   "cosas que fotografiaste para mirarlas diez minutos.",
    "problem_callout": "<p>Hay dos maneras de que deje de llenarse: revisar el "
                       "carrete cada cierto tiempo y borrar a mano —que nadie "
                       "hace—, o decidir en el momento. Snapgate es lo segundo.</p>",

    "steps_h2": "Cuatro pasos, y solo uno es tuyo",
    "steps_sub": "Todo ocurre en los segundos siguientes al disparo, mientras "
                 "todavía te acuerdas de por qué hiciste esa foto.",
    "steps": [
        ("Haces la foto",
         "Con tu cámara de siempre. Snapgate no sustituye nada ni se mete en medio."),
        ("Llega un aviso",
         "En menos de medio segundo desde que el sistema registra la imagen, "
         "con la miniatura para que veas de qué estás decidiendo."),
        ("Pulsas Subir o Descartar",
         "En la propia notificación. No hay que abrir la app ni confirmar nada más."),
        ("Lo descartado se queda en tu móvil",
         "No se borra ni se sube: simplemente nunca llega a ocupar espacio en tu "
         "cuenta de Google."),
    ],

    "features_h2": "Y cuando no quieres decidir cada vez",
    "features_sub": "Porque hay ratos en los que preguntar molesta más que ayuda.",
    "features": [
        ("Modos temporales",
         "«Durante ocho horas no subas nada.» «Estos cuatro días sube todo, estoy "
         "de viaje.» Caducan solos, para que no se te queden puestos."),
        ("Reglas por contexto",
         "Decide por franja horaria, día de la semana o carpeta. Las fotos "
         "del horario laboral no tienen por qué acabar en tu cuenta personal."),
        ("Colecciones",
         "Manda lo que apruebes directamente a un álbum concreto de tu biblioteca, "
         "sin pasar por el carrete."),
        ("Ventana de decisión",
         "Una foto solo se ofrece durante sus primeros minutos. Si no contestas, "
         "se queda en el móvil y no vuelve a molestarte."),
        ("Consumo insignificante",
         "0,02 segundos de CPU por minuto en segundo plano, medido. Con la "
         "pantalla apagada no hace absolutamente nada."),
        ("Seis idiomas",
         "Español, inglés, portugués, francés, alemán e italiano, incluidos los "
         "plurales que casi nadie traduce bien."),
    ],

    "privacy_h2": "Lo que Snapgate no puede hacer",
    "privacy_body": """
<p>Snapgate <strong>no tiene servidores</strong>. No hay ningún sitio al que
mandar tus fotos, porque no existe.</p>
<p>Cuando conectas tu cuenta de Google, la app pide un permiso concreto que
<strong>solo le deja añadir fotos</strong> a tu biblioteca. No puede leerlas,
no puede modificarlas y no puede borrar nada de lo que ya tienes. Esa
limitación no es una promesa nuestra: la impone Google y la puedes revisar en
la pantalla de consentimiento antes de aceptar.</p>
<p>La ubicación, si activas las reglas por lugar, se consulta en el momento de
hacer la foto y no se guarda ni sale del dispositivo. No hay analítica, ni
rastreadores, ni publicidad.</p>
<p>El único destino al que sale una foto es tu propia biblioteca, y solo cuando
tú lo pides.</p>
""",

    "faq_h2": "Preguntas razonables",
    "faq": [
        ("¿Tengo que apagar la copia de seguridad de Google Fotos?",
         "Sí, y es el único paso que ningún diseño puede evitar. Mientras esté "
         "encendida, Google Fotos sube tu carrete entero haga lo que haga "
         "Snapgate. Es un solo interruptor y el alta te guía hasta él."),
        ("¿Y si no contesto al aviso?",
         "No pasa nada. La foto se queda en tu móvil, no se sube, y después de "
         "unos minutos deja de preguntarte. Configurable, con cinco minutos por "
         "defecto."),
        ("¿Borra mis fotos?",
         "Nunca. Descartar significa «no la subas»; la foto sigue en tu carrete "
         "exactamente igual que antes."),
        ("¿Por qué necesita una notificación permanente?",
         "Porque Android solo avisa de una foto nueva a las apps que están en "
         "marcha. Es el precio de enterarse al momento en lugar de cada quince "
         "minutos. Puedes ocultarla desde los ajustes del sistema."),
        ("¿Es una suscripción?",
         "No. Se prueba catorce días y luego se desbloquea con un pago único."),
    ],
}

# --------------------------------------------------------------------------
# English
# --------------------------------------------------------------------------

UI["en"] = {
    "nav_how": "How it works",
    "nav_privacy": "Privacy",
    "nav_terms": "Terms",
    "nav_blog": "Blog",
    "footer_tagline": "you decide what reaches the cloud",
    "footer_rights": "Made in Spain.",
}

LANDING["en"] = {
    "title": "Snapgate · Decide which photos reach your cloud",
    "description": "Google Photos backs up your whole camera roll or none of it. "
                   "Snapgate lets you decide photo by photo, from the notification.",
    "h1": "Your cloud fills up with photos you never meant to keep",
    "lede": "The parking ticket, the receipt, a meeting whiteboard. Google Photos "
            "backs up your entire camera roll, or none of it. Snapgate puts a gate "
            "in between.",
    "cta_primary": "How it works",
    "cta_secondary": "Why we built it",
    "note": "Android 11 or later · One-time purchase, no subscription",

    "problem_h2": "The problem isn't your camera, it's all-or-nothing",
    "problem_sub": "Google Photos backup has exactly two states: on for an entire "
                   "folder, or off. There is no middle ground, which is why your "
                   "storage fills with things you photographed to look at for ten "
                   "minutes.",
    "problem_callout": "<p>There are two ways to stop it filling up: review your "
                       "camera roll regularly and delete by hand — which nobody "
                       "does — or decide in the moment. Snapgate is the second one.</p>",

    "steps_h2": "Four steps, and only one is yours",
    "steps_sub": "It all happens in the seconds after the shutter, while you still "
                 "remember why you took that photo.",
    "steps": [
        ("You take the photo",
         "With your usual camera. Snapgate replaces nothing and gets in the way of "
         "nothing."),
        ("A notification arrives",
         "Under half a second after the system registers the image, with a thumbnail "
         "so you can see what you're deciding about."),
        ("You tap Upload or Discard",
         "Right there in the notification. No need to open the app or confirm "
         "anything else."),
        ("Discarded photos stay on your phone",
         "They are not deleted and not uploaded: they simply never take up space in "
         "your Google account."),
    ],

    "features_h2": "And when you don't want to decide every time",
    "features_sub": "Because there are stretches where being asked is worse than "
                    "being helped.",
    "features": [
        ("Temporary modes",
         "\"Don't upload anything for eight hours.\" \"Upload everything for four "
         "days, I'm travelling.\" They always expire on their own, so you can't "
         "leave one running by accident."),
        ("Context rules",
         "Decide by time of day, day of week or folder. Photos taken during "
         "work hours don't have to end up in your personal account."),
        ("Collections",
         "Send what you approve straight into a specific album in your library, "
         "skipping the camera roll entirely."),
        ("Decision window",
         "A photo is only offered during its first few minutes. If you don't answer, "
         "it stays on the phone and stops bothering you."),
        ("Negligible battery use",
         "0.02 seconds of CPU per minute in the background, measured. With the "
         "screen off it does nothing at all."),
        ("Six languages",
         "Spanish, English, Portuguese, French, German and Italian — including the "
         "plural forms almost nobody gets right."),
    ],

    "privacy_h2": "What Snapgate cannot do",
    "privacy_body": """
<p>Snapgate <strong>has no servers</strong>. There is nowhere to send your photos,
because no such place exists.</p>
<p>When you connect your Google account, the app requests a specific permission that
<strong>only lets it add photos</strong> to your library. It cannot read them, cannot
modify them and cannot delete anything you already have. That limitation isn't our
promise: Google enforces it, and you can check it on the consent screen before you
accept.</p>
<p>Location, if you turn on place-based rules, is read at the moment you take a photo
and is never stored or sent anywhere. There is no analytics, no tracking and no
advertising.</p>
<p>The only destination a photo ever reaches is your own library, and only when you
ask for it.</p>
""",

    "faq_h2": "Fair questions",
    "faq": [
        ("Do I have to turn off Google Photos backup?",
         "Yes, and it's the one step no design can avoid. While it's on, Google "
         "Photos uploads your whole camera roll no matter what Snapgate does. It's a "
         "single switch and the setup walks you to it."),
        ("What if I don't answer the notification?",
         "Nothing bad. The photo stays on your phone, isn't uploaded, and after a few "
         "minutes it stops asking. Configurable, five minutes by default."),
        ("Does it delete my photos?",
         "Never. Discard means \"don't upload this\"; the photo stays in your camera "
         "roll exactly as before."),
        ("Why does it need a permanent notification?",
         "Because Android only tells running apps about a new photo. It's the price of "
         "finding out immediately instead of every fifteen minutes. You can hide it "
         "from the system settings."),
        ("Is it a subscription?",
         "No. Fourteen-day trial, then a one-time unlock."),
    ],
}

# --------------------------------------------------------------------------
# Português
# --------------------------------------------------------------------------

UI["pt"] = {
    "nav_how": "Como funciona",
    "nav_privacy": "Privacidade",
    "nav_terms": "Termos",
    "nav_blog": "Blog",
    "footer_tagline": "decides tu o que vai para a nuvem",
    "footer_rights": "Feito em Espanha.",
}

LANDING["pt"] = {
    "title": "Snapgate · Decide que fotos chegam à tua nuvem",
    "description": "O Google Fotos guarda o rolo inteiro ou não guarda nada. "
                   "O Snapgate deixa-te decidir foto a foto, a partir da notificação.",
    "h1": "A tua nuvem enche-se de fotos que nunca quiseste guardar",
    "lede": "O bilhete do estacionamento, a fatura, o quadro de uma reunião. "
            "O Google Fotos guarda o rolo inteiro ou não guarda nada. O Snapgate "
            "põe um porteiro pelo meio.",
    "cta_primary": "Como funciona",
    "cta_secondary": "Porque a criámos",
    "note": "Android 11 ou superior · Pagamento único, sem subscrição",

    "problem_h2": "O problema não é a câmara, é o tudo ou nada",
    "problem_sub": "A cópia de segurança do Google Fotos tem apenas dois estados: "
                   "ligada para uma pasta inteira, ou desligada. Não há meio termo, "
                   "e é por isso que o teu armazenamento se enche de coisas que "
                   "fotografaste para ver durante dez minutos.",
    "problem_callout": "<p>Há duas formas de parar isto: rever o rolo regularmente "
                       "e apagar à mão — o que ninguém faz — ou decidir no momento. "
                       "O Snapgate é a segunda.</p>",

    "steps_h2": "Quatro passos, e só um é teu",
    "steps_sub": "Tudo acontece nos segundos a seguir ao disparo, enquanto ainda te "
                 "lembras porque tiraste aquela foto.",
    "steps": [
        ("Tiras a foto",
         "Com a tua câmara do costume. O Snapgate não substitui nada nem se mete no "
         "caminho."),
        ("Chega um aviso",
         "Em menos de meio segundo depois de o sistema registar a imagem, com a "
         "miniatura para veres sobre o que estás a decidir."),
        ("Tocas em Enviar ou Descartar",
         "Na própria notificação. Não é preciso abrir a app nem confirmar mais nada."),
        ("O descartado fica no telemóvel",
         "Não é apagado nem enviado: simplesmente nunca ocupa espaço na tua conta "
         "Google."),
    ],

    "features_h2": "E quando não queres decidir de cada vez",
    "features_sub": "Porque há alturas em que perguntar atrapalha mais do que ajuda.",
    "features": [
        ("Modos temporários",
         "«Durante oito horas não envies nada.» «Estes quatro dias envia tudo, estou "
         "de viagem.» Expiram sozinhos, para não ficarem ligados por esquecimento."),
        ("Regras por contexto",
         "Decide por hora, dia da semana ou pasta. As fotos do horário de "
         "trabalho não têm de acabar na tua conta pessoal."),
        ("Coleções",
         "Envia o que aprovares diretamente para um álbum concreto da tua biblioteca, "
         "sem passar pelo rolo."),
        ("Janela de decisão",
         "Uma foto só é oferecida nos primeiros minutos. Se não responderes, fica no "
         "telemóvel e deixa de te incomodar."),
        ("Consumo insignificante",
         "0,02 segundos de CPU por minuto em segundo plano, medido. Com o ecrã "
         "desligado não faz absolutamente nada."),
        ("Seis idiomas",
         "Espanhol, inglês, português, francês, alemão e italiano, incluindo os "
         "plurais que quase ninguém traduz bem."),
    ],

    "privacy_h2": "O que o Snapgate não pode fazer",
    "privacy_body": """
<p>O Snapgate <strong>não tem servidores</strong>. Não há para onde enviar as tuas
fotos, porque esse sítio não existe.</p>
<p>Quando ligas a tua conta Google, a app pede uma permissão concreta que
<strong>só lhe permite adicionar fotos</strong> à tua biblioteca. Não as pode ler,
não as pode alterar e não pode apagar nada do que já tens. Essa limitação não é uma
promessa nossa: é imposta pela Google e podes confirmá-la no ecrã de consentimento
antes de aceitares.</p>
<p>A localização, se ativares as regras por lugar, é consultada no momento da foto e
nunca é guardada nem sai do dispositivo. Não há analítica, nem rastreadores, nem
publicidade.</p>
<p>O único destino de uma foto é a tua própria biblioteca, e só quando tu o pedes.</p>
""",

    "faq_h2": "Perguntas razoáveis",
    "faq": [
        ("Tenho de desligar a cópia do Google Fotos?",
         "Sim, e é o único passo que nenhum desenho consegue evitar. Enquanto estiver "
         "ligada, o Google Fotos envia o rolo inteiro faça o Snapgate o que fizer. É "
         "um só interruptor e a configuração leva-te até ele."),
        ("E se não responder ao aviso?",
         "Não acontece nada. A foto fica no telemóvel, não é enviada, e ao fim de uns "
         "minutos deixa de perguntar. Configurável, cinco minutos por omissão."),
        ("Apaga as minhas fotos?",
         "Nunca. Descartar significa «não envies esta»; a foto continua no rolo tal "
         "como estava."),
        ("Porque precisa de uma notificação permanente?",
         "Porque o Android só avisa de uma foto nova às apps em execução. É o preço de "
         "saber no momento em vez de a cada quinze minutos. Podes escondê-la nas "
         "definições do sistema."),
        ("É uma subscrição?",
         "Não. Catorze dias de experiência e depois um pagamento único."),
    ],
}

# --------------------------------------------------------------------------
# Français
# --------------------------------------------------------------------------

UI["fr"] = {
    "nav_how": "Comment ça marche",
    "nav_privacy": "Confidentialité",
    "nav_terms": "Conditions",
    "nav_blog": "Blog",
    "footer_tagline": "vous décidez de ce qui monte dans le cloud",
    "footer_rights": "Conçu en Espagne.",
}

LANDING["fr"] = {
    "title": "Snapgate · Choisissez les photos qui montent dans votre cloud",
    "description": "Google Photos sauvegarde toute votre pellicule ou rien du tout. "
                   "Snapgate vous laisse décider photo par photo, depuis la notification.",
    "h1": "Votre cloud se remplit de photos que vous ne vouliez pas garder",
    "lede": "Le ticket de parking, la facture, le tableau blanc d'une réunion. "
            "Google Photos sauvegarde toute votre pellicule, ou rien. Snapgate place "
            "un portier au milieu.",
    "cta_primary": "Comment ça marche",
    "cta_secondary": "Pourquoi nous l'avons créée",
    "note": "Android 11 ou plus · Achat unique, sans abonnement",

    "problem_h2": "Le problème n'est pas votre appareil, c'est le tout ou rien",
    "problem_sub": "La sauvegarde de Google Photos n'a que deux états : activée pour "
                   "un dossier entier, ou désactivée. Aucun intermédiaire, et c'est "
                   "pourquoi votre stockage se remplit de choses photographiées pour "
                   "être regardées dix minutes.",
    "problem_callout": "<p>Deux façons d'arrêter l'hémorragie : trier sa pellicule "
                       "régulièrement et supprimer à la main — ce que personne ne "
                       "fait — ou décider sur le moment. Snapgate, c'est la seconde.</p>",

    "steps_h2": "Quatre étapes, et une seule est la vôtre",
    "steps_sub": "Tout se joue dans les secondes qui suivent le déclenchement, quand "
                 "vous vous souvenez encore pourquoi vous avez pris cette photo.",
    "steps": [
        ("Vous prenez la photo",
         "Avec votre appareil habituel. Snapgate ne remplace rien et ne gêne rien."),
        ("Une notification arrive",
         "Moins d'une demi-seconde après l'enregistrement de l'image par le système, "
         "avec la vignette pour voir ce que vous décidez."),
        ("Vous touchez Envoyer ou Écarter",
         "Directement dans la notification. Sans ouvrir l'app ni rien confirmer."),
        ("Ce qui est écarté reste sur le téléphone",
         "Ni supprimé ni envoyé : cela n'occupe simplement jamais de place dans votre "
         "compte Google."),
    ],

    "features_h2": "Et quand vous ne voulez pas décider à chaque fois",
    "features_sub": "Parce qu'il y a des moments où être sollicité dérange plus que "
                    "cela n'aide.",
    "features": [
        ("Modes temporaires",
         "« N'envoie rien pendant huit heures. » « Envoie tout pendant quatre jours, "
         "je voyage. » Ils expirent toujours d'eux-mêmes."),
        ("Règles contextuelles",
         "Décidez selon l'heure, le jour ou le dossier. Les photos prises au "
         "travail n'ont pas à finir dans votre compte personnel."),
        ("Collections",
         "Envoyez ce que vous approuvez directement dans un album précis de votre "
         "bibliothèque."),
        ("Fenêtre de décision",
         "Une photo n'est proposée que pendant ses premières minutes. Sans réponse, "
         "elle reste sur le téléphone et cesse de vous solliciter."),
        ("Consommation négligeable",
         "0,02 seconde de CPU par minute en arrière-plan, mesuré. Écran éteint, elle "
         "ne fait absolument rien."),
        ("Six langues",
         "Espagnol, anglais, portugais, français, allemand et italien, y compris les "
         "pluriels que presque personne ne traduit correctement."),
    ],

    "privacy_h2": "Ce que Snapgate ne peut pas faire",
    "privacy_body": """
<p>Snapgate <strong>n'a pas de serveurs</strong>. Il n'existe nulle part où envoyer
vos photos.</p>
<p>Quand vous connectez votre compte Google, l'app demande une autorisation précise qui
<strong>lui permet uniquement d'ajouter des photos</strong> à votre bibliothèque. Elle
ne peut ni les lire, ni les modifier, ni supprimer quoi que ce soit d'existant. Cette
limite n'est pas une promesse de notre part : Google l'impose, et vous pouvez la
vérifier sur l'écran de consentement avant d'accepter.</p>
<p>La position, si vous activez les règles de lieu, est lue au moment de la photo et
n'est jamais enregistrée ni transmise. Pas d'analytique, pas de traqueurs, pas de
publicité.</p>
<p>La seule destination d'une photo est votre propre bibliothèque, et seulement quand
vous le demandez.</p>
""",

    "faq_h2": "Questions légitimes",
    "faq": [
        ("Dois-je désactiver la sauvegarde de Google Photos ?",
         "Oui, et c'est la seule étape qu'aucune conception ne peut éviter. Tant "
         "qu'elle est active, Google Photos envoie toute votre pellicule quoi que "
         "fasse Snapgate. C'est un seul interrupteur et la configuration vous y mène."),
        ("Et si je ne réponds pas à la notification ?",
         "Rien de grave. La photo reste sur le téléphone, n'est pas envoyée, et après "
         "quelques minutes elle cesse de vous solliciter. Configurable, cinq minutes "
         "par défaut."),
        ("Est-ce que ça supprime mes photos ?",
         "Jamais. Écarter signifie « ne l'envoie pas » ; la photo reste dans votre "
         "pellicule exactement comme avant."),
        ("Pourquoi une notification permanente ?",
         "Parce qu'Android ne signale une nouvelle photo qu'aux apps en cours "
         "d'exécution. C'est le prix d'être averti immédiatement. Vous pouvez la "
         "masquer depuis les réglages système."),
        ("Est-ce un abonnement ?",
         "Non. Quatorze jours d'essai, puis un achat unique."),
    ],
}

# --------------------------------------------------------------------------
# Deutsch
# --------------------------------------------------------------------------

UI["de"] = {
    "nav_how": "So funktioniert es",
    "nav_privacy": "Datenschutz",
    "nav_terms": "Bedingungen",
    "nav_blog": "Blog",
    "footer_tagline": "du entscheidest, was in die Cloud geht",
    "footer_rights": "Gemacht in Spanien.",
}

LANDING["de"] = {
    "title": "Snapgate · Entscheide, welche Fotos in deine Cloud kommen",
    "description": "Google Fotos sichert deine ganze Kamerarolle oder gar nichts. "
                   "Mit Snapgate entscheidest du Foto für Foto, direkt aus der "
                   "Benachrichtigung.",
    "h1": "Deine Cloud füllt sich mit Fotos, die du nie behalten wolltest",
    "lede": "Der Parkschein, die Rechnung, das Whiteboard aus einem Meeting. Google "
            "Fotos sichert deine ganze Kamerarolle — oder gar nichts. Snapgate setzt "
            "einen Türsteher dazwischen.",
    "cta_primary": "So funktioniert es",
    "cta_secondary": "Warum wir sie gebaut haben",
    "note": "Android 11 oder neuer · Einmalkauf, kein Abo",

    "problem_h2": "Das Problem ist nicht die Kamera, sondern das Alles-oder-nichts",
    "problem_sub": "Die Sicherung von Google Fotos kennt genau zwei Zustände: an für "
                   "einen ganzen Ordner, oder aus. Nichts dazwischen — und deshalb "
                   "füllt sich dein Speicher mit Dingen, die du fotografiert hast, um "
                   "sie zehn Minuten anzuschauen.",
    "problem_callout": "<p>Es gibt zwei Wege, das zu stoppen: die Kamerarolle "
                       "regelmäßig durchgehen und von Hand löschen — was niemand "
                       "macht — oder im Moment entscheiden. Snapgate ist der zweite.</p>",

    "steps_h2": "Vier Schritte, und nur einer ist deiner",
    "steps_sub": "Alles passiert in den Sekunden nach dem Auslösen, solange du noch "
                 "weißt, warum du das Foto gemacht hast.",
    "steps": [
        ("Du machst das Foto",
         "Mit deiner gewohnten Kamera. Snapgate ersetzt nichts und steht nirgends im "
         "Weg."),
        ("Eine Benachrichtigung kommt",
         "Keine halbe Sekunde nachdem das System das Bild erfasst hat — mit Vorschau, "
         "damit du siehst, worüber du entscheidest."),
        ("Du tippst Hochladen oder Verwerfen",
         "Direkt in der Benachrichtigung. Ohne die App zu öffnen oder sonst etwas zu "
         "bestätigen."),
        ("Verworfenes bleibt auf dem Handy",
         "Es wird weder gelöscht noch hochgeladen: es belegt einfach nie Platz in "
         "deinem Google-Konto."),
    ],

    "features_h2": "Und wenn du nicht jedes Mal entscheiden willst",
    "features_sub": "Weil es Phasen gibt, in denen Nachfragen mehr stört als hilft.",
    "features": [
        ("Zeitmodi",
         "„Acht Stunden lang nichts hochladen.“ „Vier Tage alles hochladen, ich bin "
         "unterwegs.“ Sie laufen immer von selbst ab."),
        ("Kontextregeln",
         "Entscheide nach Uhrzeit, Wochentag oder Ordner. Fotos aus der "
         "Arbeitszeit müssen nicht in deinem privaten Konto landen."),
        ("Sammlungen",
         "Schicke Freigegebenes direkt in ein bestimmtes Album deiner Mediathek."),
        ("Entscheidungsfenster",
         "Ein Foto wird nur in seinen ersten Minuten angeboten. Ohne Antwort bleibt es "
         "auf dem Handy und fragt nicht wieder."),
        ("Verschwindender Verbrauch",
         "Gemessen 0,02 Sekunden CPU pro Minute im Hintergrund. Bei ausgeschaltetem "
         "Bildschirm tut sie gar nichts."),
        ("Sechs Sprachen",
         "Spanisch, Englisch, Portugiesisch, Französisch, Deutsch und Italienisch — "
         "samt der Pluralformen, die fast niemand richtig übersetzt."),
    ],

    "privacy_h2": "Was Snapgate nicht kann",
    "privacy_body": """
<p>Snapgate <strong>hat keine Server</strong>. Es gibt keinen Ort, an den deine Fotos
geschickt werden könnten.</p>
<p>Wenn du dein Google-Konto verbindest, fordert die App eine ganz bestimmte
Berechtigung an, die ihr <strong>nur erlaubt, Fotos hinzuzufügen</strong>. Sie kann
sie nicht lesen, nicht ändern und nichts löschen, was du schon hast. Diese Grenze ist
kein Versprechen von uns: Google erzwingt sie, und du kannst sie auf dem
Zustimmungsbildschirm nachlesen, bevor du zustimmst.</p>
<p>Der Standort wird, falls du Ortsregeln aktivierst, im Moment der Aufnahme gelesen
und niemals gespeichert oder übertragen. Keine Analyse, kein Tracking, keine Werbung.</p>
<p>Das einzige Ziel eines Fotos ist deine eigene Mediathek — und nur, wenn du es
verlangst.</p>
""",

    "faq_h2": "Berechtigte Fragen",
    "faq": [
        ("Muss ich die Sicherung von Google Fotos ausschalten?",
         "Ja, und das ist der eine Schritt, den kein Design vermeiden kann. Solange sie "
         "an ist, lädt Google Fotos deine ganze Kamerarolle hoch, egal was Snapgate "
         "tut. Es ist ein einziger Schalter, und die Einrichtung führt dich hin."),
        ("Was, wenn ich nicht auf die Benachrichtigung reagiere?",
         "Nichts Schlimmes. Das Foto bleibt auf dem Handy, wird nicht hochgeladen, und "
         "nach ein paar Minuten fragt sie nicht mehr. Einstellbar, standardmäßig fünf "
         "Minuten."),
        ("Löscht sie meine Fotos?",
         "Nie. Verwerfen heißt „nicht hochladen“; das Foto bleibt genau wie vorher in "
         "deiner Kamerarolle."),
        ("Warum braucht sie eine dauerhafte Benachrichtigung?",
         "Weil Android nur laufenden Apps von einem neuen Foto erzählt. Das ist der "
         "Preis dafür, es sofort zu erfahren statt alle fünfzehn Minuten. Du kannst sie "
         "in den Systemeinstellungen ausblenden."),
        ("Ist das ein Abo?",
         "Nein. Vierzehn Tage testen, dann einmalig freischalten."),
    ],
}

# --------------------------------------------------------------------------
# Italiano
# --------------------------------------------------------------------------

UI["it"] = {
    "nav_how": "Come funziona",
    "nav_privacy": "Privacy",
    "nav_terms": "Termini",
    "nav_blog": "Blog",
    "footer_tagline": "decidi tu cosa finisce nel cloud",
    "footer_rights": "Fatto in Spagna.",
}

LANDING["it"] = {
    "title": "Snapgate · Decidi quali foto arrivano al tuo cloud",
    "description": "Google Foto carica tutto il rullino o niente. Snapgate ti lascia "
                   "decidere foto per foto, dalla notifica.",
    "h1": "Il tuo cloud si riempie di foto che non volevi conservare",
    "lede": "Il biglietto del parcheggio, la fattura, la lavagna di una riunione. "
            "Google Foto carica tutto il rullino, o niente. Snapgate mette un portiere "
            "in mezzo.",
    "cta_primary": "Come funziona",
    "cta_secondary": "Perché l'abbiamo fatta",
    "note": "Android 11 o successivo · Acquisto unico, senza abbonamento",

    "problem_h2": "Il problema non è la fotocamera, è il tutto o niente",
    "problem_sub": "Il backup di Google Foto ha esattamente due stati: attivo per "
                   "un'intera cartella, oppure spento. Non c'è via di mezzo, ed è per "
                   "questo che il tuo spazio si riempie di cose fotografate per "
                   "guardarle dieci minuti.",
    "problem_callout": "<p>Ci sono due modi di fermarlo: rivedere il rullino ogni "
                       "tanto e cancellare a mano — cosa che non fa nessuno — oppure "
                       "decidere sul momento. Snapgate è il secondo.</p>",

    "steps_h2": "Quattro passi, e uno solo è tuo",
    "steps_sub": "Tutto succede nei secondi dopo lo scatto, mentre ancora ricordi "
                 "perché hai fatto quella foto.",
    "steps": [
        ("Scatti la foto",
         "Con la tua fotocamera di sempre. Snapgate non sostituisce nulla e non si "
         "mette in mezzo."),
        ("Arriva un avviso",
         "Meno di mezzo secondo dopo che il sistema registra l'immagine, con la "
         "miniatura per vedere su cosa stai decidendo."),
        ("Tocchi Carica o Scarta",
         "Nella notifica stessa. Senza aprire l'app né confermare altro."),
        ("Ciò che scarti resta sul telefono",
         "Non viene eliminato né caricato: semplicemente non occupa mai spazio nel tuo "
         "account Google."),
    ],

    "features_h2": "E quando non vuoi decidere ogni volta",
    "features_sub": "Perché ci sono momenti in cui essere interrotti dà più fastidio "
                    "che aiuto.",
    "features": [
        ("Modalità temporanee",
         "«Per otto ore non caricare niente.» «Questi quattro giorni carica tutto, sono "
         "in viaggio.» Scadono sempre da sole."),
        ("Regole di contesto",
         "Decidi per orario, giorno della settimana o cartella. Le foto in "
         "orario di lavoro non devono finire nel tuo account personale."),
        ("Raccolte",
         "Manda ciò che approvi direttamente in un album preciso della tua libreria."),
        ("Finestra di decisione",
         "Una foto viene proposta solo nei primi minuti. Se non rispondi resta sul "
         "telefono e smette di disturbarti."),
        ("Consumo trascurabile",
         "0,02 secondi di CPU al minuto in background, misurati. A schermo spento non "
         "fa assolutamente nulla."),
        ("Sei lingue",
         "Spagnolo, inglese, portoghese, francese, tedesco e italiano, comprese le "
         "forme plurali che quasi nessuno traduce bene."),
    ],

    "privacy_h2": "Cosa Snapgate non può fare",
    "privacy_body": """
<p>Snapgate <strong>non ha server</strong>. Non c'è nessun posto dove mandare le tue
foto, perché non esiste.</p>
<p>Quando colleghi il tuo account Google, l'app chiede un permesso specifico che
<strong>le consente solo di aggiungere foto</strong> alla tua libreria. Non può
leggerle, non può modificarle e non può eliminare nulla di ciò che hai già. Questo
limite non è una nostra promessa: lo impone Google, e puoi verificarlo nella schermata
di consenso prima di accettare.</p>
<p>La posizione, se attivi le regole per luogo, viene letta al momento dello scatto e
non viene mai salvata né trasmessa. Nessuna analitica, nessun tracciamento, nessuna
pubblicità.</p>
<p>L'unica destinazione di una foto è la tua libreria, e solo quando lo chiedi tu.</p>
""",

    "faq_h2": "Domande legittime",
    "faq": [
        ("Devo disattivare il backup di Google Foto?",
         "Sì, ed è l'unico passo che nessun progetto può evitare. Finché è attivo, "
         "Google Foto carica tutto il rullino qualunque cosa faccia Snapgate. È un solo "
         "interruttore e la configurazione ti ci accompagna."),
        ("E se non rispondo alla notifica?",
         "Non succede niente. La foto resta sul telefono, non viene caricata, e dopo "
         "qualche minuto smette di chiedertelo. Configurabile, cinque minuti di "
         "default."),
        ("Cancella le mie foto?",
         "Mai. Scartare significa «non caricarla»; la foto resta nel rullino esattamente "
         "come prima."),
        ("Perché serve una notifica permanente?",
         "Perché Android avvisa di una foto nuova solo le app in esecuzione. È il prezzo "
         "di saperlo subito invece che ogni quindici minuti. Puoi nasconderla dalle "
         "impostazioni di sistema."),
        ("È un abbonamento?",
         "No. Quattordici giorni di prova, poi un acquisto unico."),
    ],
}
