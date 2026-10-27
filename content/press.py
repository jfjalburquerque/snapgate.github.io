# -*- coding: utf-8 -*-
"""
Pagina de prensa, en los seis idiomas de la web.

La estructura es una sola y los textos van por idioma: asi una cifra o un
enlace se cambian en un sitio y no se desincronizan entre versiones. Las
capturas de la galeria son las del idioma de la pagina; la tabla de abajo da
las de todos, porque una redaccion de un pais puede querer las de otro.

Todo lo que hay aqui tiene que poder copiarse tal cual en un articulo: frases
completas, datos que no caducan y enlaces directos a los ficheros.
"""

from content.legal import CONTACT
from content.site import LANGS, LANG_NAMES, LANDING

PLAY_URL = "https://play.google.com/store/apps/details?id=com.snapgate.app"
SHOT_NAMES = ["01-notif", "02-selection", "03-features", "04-onb1"]

# Cobertura, de la mas reciente a la mas antigua. El titulo se deja en su
# idioma original: es el que el lector encontrara si sigue el enlace. El nombre
# corto es el que sale en la portada, en la linea de «tambien en».
COVERAGE = [
    ("https://www.monitor.si/clanek/nas-izbor-na-androidu/252101/",
     "Monitor: Naš izbor na Androidu (november 2026)", "si", "Monitor"),
    ("https://www.youtube.com/watch?v=urBE-pYEg-k",
     "Gadgets One Malayalam: 5 Must-Try Android Apps October", "in", "Gadgets One"),
    ("https://www.bug.hr/appdana/snapgate-omogucuje-biranje-koje-ce-fotografije-zavrsiti-u-google-photosu-63479",
     "Bug.hr: App dana", "hr", "Bug.hr"),
    ("https://www.youtube.com/watch?v=P_iMZNBO7lk",
     "9TUENG: Snapgate", "th", "9TUENG"),
    ("https://www.youtube.com/watch?v=TYNzg59ke30&amp;t=61s",
     "HowToMen: Top 15 Best Android Apps, October 2026", "yt", "HowToMen"),
]

T = {}

T["en"] = {
    "title": "Press kit · Snapgate",
    "description": "Facts, screenshots, logos and contact for writing about Snapgate, "
                   "the Android app that asks before each photo goes to Google Photos.",
    "h1": "Press kit",
    "meta": "Everything you need to write about Snapgate. Use any of it freely.",
    "line_h2": "In one line",
    "line": "Snapgate asks you, right from the notification, whether each new photo "
            "should back up to Google Photos.",
    "para_h2": "In a paragraph",
    "para": "Google Photos backs up by folder, and everything from the camera lands in the "
            "same one. So receipts, "
            "parking spots, screenshots and meeting whiteboards end up in the cloud next "
            "to the photos that matter, eating into the free 15 GB. Snapgate adds what's "
            "missing: a decision per photo. Seconds after you take a photo, a notification shows a thumbnail with "
            "two buttons, Upload and Discard. Discarded photos stay on the phone untouched. "
            "Temporary modes and rules by time, day or folder handle the moments when you "
            "don't want to be asked. There are no servers, no ads and no analytics, and the "
            "Google permission it uses can only add photos, never read or delete them.",
    "facts_h2": "Fact sheet",
    "facts": [
        ("App", "Snapgate: selective backup"),
        ("Developer", "jfjalburquerque (visionatec), independent developer based in Spain"),
        ("Platform", "Android 11 or later"),
        ("Price", "Free 14-day trial, then a one-time purchase of €4.99 (local prices vary). "
                  "No subscription."),
        ("Privacy", "No servers, no ads, no analytics. Photos only leave the phone to the "
                    "user's own Google Photos library, and only when approved."),
        ("Languages", "English, Spanish, Portuguese, French, German, Italian"),
        ("Released", "September 2026"),
    ],
    "download": "Download",
    "shots_h2": "Screenshots",
    "shots_hint": "Click any image for the full-resolution PNG.",
    "shots_all": "The same four screenshots in every language the app supports:",
    "col_lang": "Language",
    "col_shots": "Screenshots (1080 × 1920 PNG)",
    "assets_h2": "Logos and graphics",
    "icon": "App icon",
    "logo_light": "Logo for light backgrounds",
    "logo_dark": "Logo for dark backgrounds",
    "feature": "Feature graphic",
    "coverage_h2": "Coverage",
    "where": {"hr": "Croatia", "th": "YouTube, Thailand", "yt": "YouTube", "in": "YouTube, India", "si": "Slovenia, magazine"},
    "contact_h2": "Contact",
    "contact": "Questions, interviews or a free unlock code for review:",
    "reply": "I usually answer within a day.",
}

T["es"] = {
    "title": "Prensa · Snapgate",
    "description": "Datos, capturas, logotipos y contacto para escribir sobre Snapgate, "
                   "la app de Android que pregunta antes de subir cada foto a Google Fotos.",
    "h1": "Prensa",
    "meta": "Todo lo necesario para escribir sobre Snapgate. Úsalo libremente.",
    "line_h2": "En una frase",
    "line": "Snapgate te pregunta, desde la propia notificación, si cada foto nueva debe "
            "subirse a Google Fotos.",
    "para_h2": "En un párrafo",
    "para": "Google Fotos decide por carpetas, y todo lo que sale de la cámara va a la misma. "
            "Así que tickets, plazas de aparcamiento, capturas de pantalla y pizarras de "
            "reuniones acaban en la nube junto a las fotos que importan, gastando los 15 GB "
            "gratuitos. Snapgate añade lo que falta: decidir foto a foto. Segundos después de hacer una foto, "
            "una notificación muestra la miniatura con dos botones, Subir y Descartar. Las "
            "fotos descartadas se quedan en el móvil intactas. Los modos temporales y las "
            "reglas por hora, día o carpeta cubren los momentos en que no quieres que te "
            "pregunte. No hay servidores, ni publicidad, ni analítica, y el permiso de Google "
            "que usa solo puede añadir fotos, nunca leerlas ni borrarlas.",
    "facts_h2": "Ficha",
    "facts": [
        ("App", "Snapgate: copia selectiva"),
        ("Desarrollador", "jfjalburquerque (visionatec), desarrollador independiente en España"),
        ("Plataforma", "Android 11 o superior"),
        ("Precio", "Prueba gratuita de 14 días y después un pago único de 4,99 € (el precio "
                   "varía según el país). Sin suscripción."),
        ("Privacidad", "Sin servidores, sin publicidad, sin analítica. Las fotos solo salen "
                       "del móvil hacia la biblioteca de Google Fotos del propio usuario, y "
                       "solo cuando él lo aprueba."),
        ("Idiomas", "Español, inglés, portugués, francés, alemán e italiano"),
        ("Lanzamiento", "Septiembre de 2026"),
    ],
    "download": "Descarga",
    "shots_h2": "Capturas",
    "shots_hint": "Pulsa cualquier imagen para descargar el PNG a resolución completa.",
    "shots_all": "Las mismas cuatro capturas en cada idioma de la app:",
    "col_lang": "Idioma",
    "col_shots": "Capturas (PNG de 1080 × 1920)",
    "assets_h2": "Logotipos y gráficos",
    "icon": "Icono de la app",
    "logo_light": "Logotipo para fondos claros",
    "logo_dark": "Logotipo para fondos oscuros",
    "feature": "Gráfico de cabecera",
    "coverage_h2": "Cobertura",
    "where": {"hr": "Croacia", "th": "YouTube, Tailandia", "yt": "YouTube", "in": "YouTube, India", "si": "Eslovenia, revista"},
    "contact_h2": "Contacto",
    "contact": "Preguntas, entrevistas o un código de desbloqueo gratuito para hacer una reseña:",
    "reply": "Suelo responder en menos de un día.",
}

T["pt"] = {
    "title": "Imprensa · Snapgate",
    "description": "Dados, capturas de ecrã, logótipos e contacto para escrever sobre o "
                   "Snapgate, a app Android que pergunta antes de enviar cada foto para o "
                   "Google Fotos.",
    "h1": "Imprensa",
    "meta": "Tudo o que precisas para escrever sobre o Snapgate. Usa à vontade.",
    "line_h2": "Numa frase",
    "line": "O Snapgate pergunta-te, a partir da própria notificação, se cada foto nova "
            "deve ir para o Google Fotos.",
    "para_h2": "Num parágrafo",
    "para": "O Google Fotos guarda por pastas, e tudo o que sai da câmara vai para a mesma. "
            "Por "
            "isso, recibos, lugares de estacionamento, capturas de ecrã e quadros de reuniões "
            "acabam na nuvem ao lado das fotos que importam, a gastar os 15 GB gratuitos. O "
            "Snapgate acrescenta o que falta: decidir foto a foto. Segundos depois de tirares uma foto, uma "
            "notificação mostra a miniatura com dois botões, Enviar e Descartar. As fotos "
            "descartadas ficam no telemóvel intactas. Os modos temporários e as regras por "
            "hora, dia ou pasta tratam dos momentos em que não queres que te pergunte. Não há "
            "servidores, nem publicidade, nem análise, e a permissão do Google que usa só "
            "consegue adicionar fotos, nunca lê-las nem apagá-las.",
    "facts_h2": "Ficha",
    "facts": [
        ("App", "Snapgate: cópia seletiva"),
        ("Programador", "jfjalburquerque (visionatec), programador independente em Espanha"),
        ("Plataforma", "Android 11 ou superior"),
        ("Preço", "Teste gratuito de 14 dias e depois um pagamento único de 4,99 € (o preço "
                  "varia consoante o país). Sem subscrição."),
        ("Privacidade", "Sem servidores, sem publicidade, sem análise. As fotos só saem do "
                        "telemóvel para a biblioteca do Google Fotos do próprio utilizador, e "
                        "só quando ele aprova."),
        ("Idiomas", "Português, inglês, espanhol, francês, alemão e italiano"),
        ("Lançamento", "Setembro de 2026"),
    ],
    "download": "Transferir",
    "shots_h2": "Capturas de ecrã",
    "shots_hint": "Toca em qualquer imagem para obter o PNG em resolução total.",
    "shots_all": "As mesmas quatro capturas em cada idioma da app:",
    "col_lang": "Idioma",
    "col_shots": "Capturas (PNG de 1080 × 1920)",
    "assets_h2": "Logótipos e gráficos",
    "icon": "Ícone da app",
    "logo_light": "Logótipo para fundos claros",
    "logo_dark": "Logótipo para fundos escuros",
    "feature": "Gráfico de destaque",
    "coverage_h2": "Cobertura",
    "where": {"hr": "Croácia", "th": "YouTube, Tailândia", "yt": "YouTube", "in": "YouTube, Índia", "si": "Eslovénia, revista"},
    "contact_h2": "Contacto",
    "contact": "Perguntas, entrevistas ou um código de desbloqueio gratuito para análise:",
    "reply": "Costumo responder em menos de um dia.",
}

T["fr"] = {
    "title": "Presse · Snapgate",
    "description": "Chiffres, captures d'écran, logos et contact pour écrire sur Snapgate, "
                   "l'app Android qui demande avant d'envoyer chaque photo vers Google Photos.",
    "h1": "Presse",
    "meta": "Tout ce qu'il faut pour écrire sur Snapgate. Libre d'utilisation.",
    "line_h2": "En une phrase",
    "line": "Snapgate vous demande, directement depuis la notification, si chaque nouvelle "
            "photo doit être sauvegardée dans Google Photos.",
    "para_h2": "En un paragraphe",
    "para": "Google Photos sauvegarde par dossier, et tout ce qui sort de l'appareil photo "
            "atterrit dans le même. Tickets, "
            "places de parking, captures d'écran et tableaux de réunion finissent donc dans "
            "le cloud à côté des photos qui comptent, et grignotent les 15 Go gratuits. "
            "Snapgate ajoute ce qui manque : décider photo par photo. Quelques secondes après une photo, une "
            "notification affiche une miniature et deux boutons, Envoyer et Ignorer. Les "
            "photos ignorées restent intactes sur le téléphone. Les modes temporaires et les "
            "règles par heure, jour ou dossier prennent le relais quand vous ne voulez pas "
            "être sollicité. Pas de serveurs, pas de publicité, pas de statistiques, et "
            "l'autorisation Google utilisée permet seulement d'ajouter des photos, jamais de "
            "les lire ni de les supprimer.",
    "facts_h2": "Fiche",
    "facts": [
        ("App", "Snapgate : sauvegarde au choix"),
        ("Développeur", "jfjalburquerque (visionatec), développeur indépendant basé en Espagne"),
        ("Plateforme", "Android 11 ou version ultérieure"),
        ("Prix", "Essai gratuit de 14 jours, puis un achat unique de 4,99 € (le prix varie "
                 "selon le pays). Sans abonnement."),
        ("Confidentialité", "Pas de serveurs, pas de publicité, pas de statistiques. Les "
                            "photos ne quittent le téléphone que vers la bibliothèque Google "
                            "Photos de l'utilisateur, et seulement avec son accord."),
        ("Langues", "Français, anglais, espagnol, portugais, allemand et italien"),
        ("Sortie", "Septembre 2026"),
    ],
    "download": "Téléchargement",
    "shots_h2": "Captures d'écran",
    "shots_hint": "Cliquez sur une image pour obtenir le PNG en pleine résolution.",
    "shots_all": "Les quatre mêmes captures dans chaque langue de l'app :",
    "col_lang": "Langue",
    "col_shots": "Captures (PNG 1080 × 1920)",
    "assets_h2": "Logos et visuels",
    "icon": "Icône de l'app",
    "logo_light": "Logo pour fonds clairs",
    "logo_dark": "Logo pour fonds sombres",
    "feature": "Bannière",
    "coverage_h2": "Couverture",
    "where": {"hr": "Croatie", "th": "YouTube, Thaïlande", "yt": "YouTube", "in": "YouTube, Inde", "si": "Slovénie, magazine"},
    "contact_h2": "Contact",
    "contact": "Questions, interviews ou un code de déverrouillage gratuit pour un test :",
    "reply": "Je réponds en général sous un jour.",
}

T["de"] = {
    "title": "Presse · Snapgate",
    "description": "Fakten, Screenshots, Logos und Kontakt für Artikel über Snapgate, die "
                   "Android-App, die vor jedem Foto fragt, ob es zu Google Fotos soll.",
    "h1": "Presse",
    "meta": "Alles, was du brauchst, um über Snapgate zu schreiben. Frei verwendbar.",
    "line_h2": "In einem Satz",
    "line": "Snapgate fragt dich direkt in der Benachrichtigung, ob jedes neue Foto in "
            "Google Fotos gesichert werden soll.",
    "para_h2": "In einem Absatz",
    "para": "Google Fotos sichert nach Ordnern, und alles aus der Kamera landet im selben. So "
            "landen Kassenzettel, Parkplätze, Screenshots und Whiteboards aus Meetings neben "
            "den Fotos, die zählen, in der Cloud und verbrauchen die kostenlosen 15 GB. "
            "Snapgate ergänzt, was fehlt: eine Entscheidung pro Foto. Sekunden nach dem Foto zeigt eine "
            "Benachrichtigung ein Vorschaubild mit zwei Schaltflächen, Hochladen und "
            "Verwerfen. Verworfene Fotos bleiben unverändert auf dem Handy. Temporäre Modi "
            "und Regeln nach Uhrzeit, Wochentag oder Ordner übernehmen, wenn du nicht gefragt "
            "werden willst. Keine Server, keine Werbung, keine Analyse, und die genutzte "
            "Google-Berechtigung kann nur Fotos hinzufügen, nie lesen oder löschen.",
    "facts_h2": "Steckbrief",
    "facts": [
        ("App", "Snapgate: Backup nach Wahl"),
        ("Entwickler", "jfjalburquerque (visionatec), unabhängiger Entwickler aus Spanien"),
        ("Plattform", "Android 11 oder neuer"),
        ("Preis", "14 Tage kostenlos testen, danach einmalig 4,99 € (Preise je nach Land). "
                  "Kein Abo."),
        ("Datenschutz", "Keine Server, keine Werbung, keine Analyse. Fotos verlassen das "
                        "Handy nur in die eigene Google-Fotos-Mediathek, und nur nach "
                        "Zustimmung."),
        ("Sprachen", "Deutsch, Englisch, Spanisch, Portugiesisch, Französisch, Italienisch"),
        ("Erschienen", "September 2026"),
    ],
    "download": "Download",
    "shots_h2": "Screenshots",
    "shots_hint": "Klicke auf ein Bild für das PNG in voller Auflösung.",
    "shots_all": "Dieselben vier Screenshots in jeder Sprache der App:",
    "col_lang": "Sprache",
    "col_shots": "Screenshots (PNG, 1080 × 1920)",
    "assets_h2": "Logos und Grafiken",
    "icon": "App-Icon",
    "logo_light": "Logo für helle Hintergründe",
    "logo_dark": "Logo für dunkle Hintergründe",
    "feature": "Vorstellungsgrafik",
    "coverage_h2": "Berichterstattung",
    "where": {"hr": "Kroatien", "th": "YouTube, Thailand", "yt": "YouTube", "in": "YouTube, Indien", "si": "Slowenien, Magazin"},
    "contact_h2": "Kontakt",
    "contact": "Fragen, Interviews oder ein kostenloser Freischaltcode für einen Test:",
    "reply": "Ich antworte meist innerhalb eines Tages.",
}

T["it"] = {
    "title": "Stampa · Snapgate",
    "description": "Dati, screenshot, loghi e contatti per scrivere di Snapgate, l'app "
                   "Android che chiede prima di caricare ogni foto su Google Foto.",
    "h1": "Stampa",
    "meta": "Tutto ciò che serve per scrivere di Snapgate. Usalo liberamente.",
    "line_h2": "In una frase",
    "line": "Snapgate ti chiede, direttamente dalla notifica, se ogni nuova foto deve "
            "finire su Google Foto.",
    "para_h2": "In un paragrafo",
    "para": "Google Foto fa il backup per cartelle, e tutto ciò che esce dalla fotocamera "
            "finisce nella stessa. Così scontrini, "
            "posti auto, screenshot e lavagne delle riunioni finiscono nel cloud accanto alle "
            "foto che contano, consumando i 15 GB gratuiti. Snapgate aggiunge ciò che "
            "manca: decidere foto per foto. Pochi secondi dopo lo scatto, una notifica mostra l'anteprima con due "
            "pulsanti, Carica e Scarta. Le foto scartate restano intatte sul telefono. Le "
            "modalità temporanee e le regole per orario, giorno o cartella pensano ai momenti "
            "in cui non vuoi essere interpellato. Niente server, niente pubblicità, niente "
            "analisi, e il permesso Google che usa può solo aggiungere foto, mai leggerle o "
            "cancellarle.",
    "facts_h2": "Scheda",
    "facts": [
        ("App", "Snapgate: backup selettivo"),
        ("Sviluppatore", "jfjalburquerque (visionatec), sviluppatore indipendente in Spagna"),
        ("Piattaforma", "Android 11 o successivo"),
        ("Prezzo", "Prova gratuita di 14 giorni, poi un acquisto unico di 4,99 € (il prezzo "
                   "varia per paese). Nessun abbonamento."),
        ("Privacy", "Niente server, niente pubblicità, niente analisi. Le foto escono dal "
                    "telefono solo verso la libreria Google Foto dell'utente, e solo con la "
                    "sua approvazione."),
        ("Lingue", "Italiano, inglese, spagnolo, portoghese, francese e tedesco"),
        ("Uscita", "Settembre 2026"),
    ],
    "download": "Download",
    "shots_h2": "Screenshot",
    "shots_hint": "Tocca un'immagine per il PNG a piena risoluzione.",
    "shots_all": "Gli stessi quattro screenshot in ogni lingua dell'app:",
    "col_lang": "Lingua",
    "col_shots": "Screenshot (PNG 1080 × 1920)",
    "assets_h2": "Loghi e grafiche",
    "icon": "Icona dell'app",
    "logo_light": "Logo per sfondi chiari",
    "logo_dark": "Logo per sfondi scuri",
    "feature": "Immagine in evidenza",
    "coverage_h2": "Copertura",
    "where": {"hr": "Croazia", "th": "YouTube, Thailandia", "yt": "YouTube", "in": "YouTube, India", "si": "Slovenia, rivista"},
    "contact_h2": "Contatti",
    "contact": "Domande, interviste o un codice di sblocco gratuito per una recensione:",
    "reply": "Di solito rispondo entro un giorno.",
}


def _body(lang):
    t = T[lang]
    alts = LANDING[lang]["shots"]
    facts = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in t["facts"])
    gallery = "".join(
        f'<a href="../assets/store/phone/{lang}/{name}.png">'
        f'<img src="../assets/web/shots/{lang}/{name}.webp" width="540" height="960" '
        f'loading="lazy" alt="{alt}"></a>'
        for name, alt in zip(SHOT_NAMES, alts)
    )
    rows = "".join(
        f"<tr><td>{LANG_NAMES[code]}</td>"
        + "".join(
            f'<td><a href="../assets/store/phone/{code}/{name}.png">{i}</a></td>'
            for i, name in enumerate(SHOT_NAMES, 1)
        )
        + "</tr>"
        for code in LANGS
    )
    # El grafico de cabecera existe en los seis idiomas; se da el de la pagina.
    coverage = "".join(
        f'<li><a href="{url}">{title}</a> ({t["where"][where]})</li>'
        for url, title, where, _ in COVERAGE
    )
    return f"""
<h2>{t["line_h2"]}</h2>
<p>{t["line"]}</p>

<h2>{t["para_h2"]}</h2>
<p>{t["para"]}</p>

<h2>{t["facts_h2"]}</h2>
<table>
{facts}
<tr><th>{t["download"]}</th><td><a href="{PLAY_URL}">Google Play</a></td></tr>
</table>

<h2>{t["shots_h2"]}</h2>
<p>{t["shots_hint"]}</p>
<div class="shots">{gallery}</div>
<p>{t["shots_all"]}</p>
<table><tr><th>{t["col_lang"]}</th><th colspan="4">{t["col_shots"]}</th></tr>{rows}</table>

<h2>{t["assets_h2"]}</h2>
<ul>
<li><a href="../assets/brand/play-icon-512.png">{t["icon"]}</a>, 512 × 512 PNG</li>
<li><a href="../assets/brand/logo-horizontal.png">{t["logo_light"]}</a>, PNG</li>
<li><a href="../assets/brand/logo-horizontal-dark.png">{t["logo_dark"]}</a>, PNG</li>
<li><a href="../assets/store/feature/{lang}.png">{t["feature"]}</a>, 1024 × 500 PNG</li>
</ul>

<h2>{t["coverage_h2"]}</h2>
<ul>{coverage}</ul>

<h2>{t["contact_h2"]}</h2>
<p>{t["contact"]} <a href="mailto:{CONTACT}">{CONTACT}</a>. {t["reply"]}</p>
"""


PRESS = {
    lang: {
        "title": T[lang]["title"],
        "description": T[lang]["description"],
        "h1": T[lang]["h1"],
        "meta": T[lang]["meta"],
        "body": _body(lang),
    }
    for lang in LANGS
}
