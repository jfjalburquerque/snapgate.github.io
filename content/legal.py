# -*- coding: utf-8 -*-
"""Política de privacidad y términos, por idioma.

La política es requisito de Google Play y de la verificación de OAuth: tiene que
estar publicada en una URL accesible antes de poder configurar el consentimiento.
"""

PRIVACY = {}
TERMS = {}

UPDATED = "2026-09-17"
CONTACT = "jfjalburquerque@gmail.com"

PRIVACY["es"] = {
    "title": "Política de privacidad · Snapgate",
    "description": "Qué datos trata Snapgate y, sobre todo, qué no puede hacer.",
    "h1": "Política de privacidad",
    "meta": "Última actualización: 17 de septiembre de 2026",
    "body": f"""
<p>Snapgate es una aplicación para Android que te permite decidir, foto a foto,
cuáles se suben a tu biblioteca de Google Fotos y cuáles no.</p>

<p>Resumen en una frase: <strong>no existe ningún servidor nuestro</strong>, tus
fotos no salen de tu dispositivo salvo hacia tu propia cuenta de Google, y solo
cuando tú lo pides.</p>

<h2>Responsable</h2>
<p>El desarrollador de Snapgate. Puedes contactar en <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>Qué datos se tratan y para qué</h2>

<h3>Tus fotos</h3>
<p>La aplicación lee las imágenes de las carpetas que tú configuras para poder
mostrártelas y preguntarte qué hacer con ellas. Esa lectura ocurre íntegramente
en tu dispositivo. No se envían copias a ningún sitio, no se analizan y no se
conservan fuera del propio almacenamiento del teléfono.</p>

<h3>Tu cuenta de Google</h3>
<p>Si decides conectarla, Snapgate solicita dos permisos concretos:</p>
<ul>
  <li><code>photoslibrary.appendonly</code>, que permite <strong>únicamente
      añadir</strong> fotos a tu biblioteca.</li>
  <li><code>photoslibrary.readonly.appcreateddata</code>, que permite ver
      solamente los álbumes que la propia aplicación ha creado.</li>
</ul>
<p>Con esos permisos la aplicación <strong>no puede leer, modificar ni eliminar</strong>
ninguna foto o álbum que ya tuvieras. La restricción la impone Google, no nosotros.
El testigo de acceso se guarda cifrado en el almacenamiento privado de la app y
nunca se transmite a terceros.</p>

<h3>Tu ubicación</h3>
<p>Solo si activas las reglas por lugar y concedes el permiso. Se consulta la
última posición conocida en el momento de evaluar una foto, para comprobar si
encaja con una regla que tú has creado. No se registra, no se almacena y no sale
del dispositivo.</p>

<h3>Datos de uso</h3>
<p>Ninguno. No hay analítica, ni herramientas de medición, ni identificadores
publicitarios, ni informes de fallos automáticos.</p>

<h2>Datos de usuario de Google a los que accede la aplicación</h2>

<p>Si conectas tu cuenta, Snapgate solicita exactamente dos permisos de la API de
Google Photos y ninguno más:</p>

<table>
  <tr><th>Permiso</th><th>Qué permite exactamente</th></tr>
  <tr>
    <td><code>photoslibrary.appendonly</code></td>
    <td>Solo <strong>añadir</strong> fotos y crear álbumes en tu biblioteca. Es
        de escritura: no da acceso de lectura a nada de lo que ya tienes.</td>
  </tr>
  <tr>
    <td><code>photoslibrary.readonly.appcreateddata</code></td>
    <td>Leer <strong>únicamente</strong> los álbumes creados por la propia
        aplicación, para que puedas elegir a cuál enviar tus fotos.</td>
  </tr>
</table>

<p>Con esos permisos, los datos de tu cuenta de Google a los que la aplicación
tiene acceso se limitan a:</p>

<ul>
  <li>El <strong>título e identificador de los álbumes creados por la propia
      aplicación</strong>, para mostrártelos como destino.</li>
  <li>Los <strong>testigos de acceso</strong> (token de acceso y de renovación)
      que emite Google al autorizarla.</li>
</ul>

<p>La aplicación <strong>no accede</strong> a tus fotos o álbumes existentes, ni a
tu nombre, correo, contactos, calendario, archivos de Drive ni a ningún otro
servicio de Google. Esa limitación no depende de nuestra buena fe: la impone
Google al conceder solo esos permisos, y puedes comprobarla en la pantalla de
consentimiento antes de aceptar.</p>

<p><strong>Para qué se usan.</strong> Únicamente para subir a tu biblioteca las
fotografías que apruebas de forma explícita, y para ofrecerte como destino los
álbumes que la aplicación haya creado. No se usan para publicidad, ni para
elaborar perfiles, ni para entrenar modelos, ni se venden o ceden a nadie.</p>

<h2>Cómo se protegen estos datos</h2>

<ul>
  <li><strong>En tránsito.</strong> Toda comunicación con las API de Google viaja
      cifrada mediante HTTPS/TLS. La aplicación no se comunica con ningún otro
      servidor, porque no existe ningún servidor nuestro.</li>
  <li><strong>En reposo.</strong> Los testigos de acceso se guardan en el
      almacenamiento privado de la aplicación, aislado por el espacio de nombres
      de Android, al que ninguna otra aplicación del dispositivo puede llegar.</li>
  <li><strong>Fuera de las copias de seguridad.</strong> El fichero que contiene
      los testigos está excluido tanto de la copia en la nube como de la
      transferencia directa a un dispositivo nuevo. La credencial no sale nunca
      del móvil en el que la autorizaste.</li>
  <li><strong>Mínimo imprescindible.</strong> Se pide el permiso de escritura más
      restringido que existe para esta función, en lugar de acceso completo a la
      biblioteca.</li>
  <li><strong>Conservación y borrado.</strong> Los testigos se conservan mientras
      la cuenta siga conectada. Se eliminan al desconectarla desde los ajustes de
      la aplicación y al desinstalarla. Puedes además revocar el acceso en
      cualquier momento desde la
      <a href="https://myaccount.google.com/permissions">página de permisos de tu
      cuenta de Google</a>, lo que invalida los testigos de inmediato.</li>
  <li><strong>Sin terceros.</strong> No se emplea analítica, ni SDK publicitarios,
      ni servicios de registro de errores que pudieran recibir estos datos.</li>
</ul>

<h2>Con quién se comparten</h2>
<p>Con nadie. Las únicas comunicaciones de red que realiza la aplicación son:</p>
<ul>
  <li>Con los servidores de Google, para subir a <em>tu</em> biblioteca las fotos
      que tú apruebas.</li>
  <li>Con Google Play, para verificar tu compra.</li>
</ul>

<h2>Conservación</h2>
<p>Los ajustes, la lista de fotos ya decididas y el testigo de acceso se guardan
en tu dispositivo mientras la aplicación esté instalada. Desinstalarla los elimina
por completo.</p>

<h2>Tus derechos</h2>
<p>Puedes desconectar tu cuenta de Google desde los ajustes de la aplicación en
cualquier momento, y revocar el acceso por completo desde la
<a href="https://myaccount.google.com/permissions">página de permisos de tu cuenta
de Google</a>. Como no conservamos datos tuyos en ningún sistema propio, no hay
nada que solicitar ni que suprimir por nuestra parte.</p>

<p>Si resides en la Unión Europea, te asisten los derechos del RGPD. Dado que no
tratamos datos personales fuera de tu dispositivo, su ejercicio se resuelve con la
desinstalación y la revocación del acceso descritas arriba. Para cualquier duda,
escríbenos.</p>

<h2>Menores</h2>
<p>Snapgate no está dirigida a menores de 13 años y no recopila conscientemente
datos de ellos.</p>

<h2>Cambios</h2>
<p>Si esta política cambia, se publicará la versión actualizada en esta misma
página con su fecha. Los cambios sustanciales se anunciarán además dentro de la
aplicación.</p>
""",
}

TERMS["es"] = {
    "title": "Términos y condiciones · Snapgate",
    "description": "Condiciones de uso de la aplicación Snapgate.",
    "h1": "Términos y condiciones",
    "meta": "Última actualización: 17 de septiembre de 2026",
    "body": f"""
<p>Al instalar y usar Snapgate aceptas estas condiciones. Si no estás de acuerdo
con ellas, no uses la aplicación.</p>

<h2>1. Qué es Snapgate</h2>
<p>Una aplicación para Android que te permite decidir qué fotografías de tu
dispositivo se suben a tu biblioteca de Google Fotos. Snapgate <strong>no es un
producto de Google</strong> ni está afiliada, patrocinada o respaldada por Google
LLC. Google Fotos, Google Play y Android son marcas de Google LLC.</p>

<h2>2. Licencia</h2>
<p>Se te concede una licencia personal, intransferible y no exclusiva para usar la
aplicación en los dispositivos asociados a tu cuenta de Google Play. No puedes
revenderla, redistribuirla ni intentar eludir el mecanismo de compra.</p>

<h2>3. Prueba y compra</h2>
<p>Snapgate se puede usar gratuitamente durante catorce días. Transcurrido ese
plazo, seguir usándola requiere un <strong>pago único</strong> a través de Google
Play; no es una suscripción y no se renueva. Las devoluciones se rigen por la
política de Google Play, que actualmente incluye un reembolso automático dentro de
las primeras dos horas tras la compra.</p>

<h2>4. Uso correcto</h2>
<p>Te comprometes a usar la aplicación únicamente con fotografías sobre las que
tengas derechos, y a no emplearla para tratar contenido ilícito.</p>

<h2>5. Dependencia de servicios de terceros</h2>
<p>El funcionamiento de la aplicación depende de servicios ajenos —la API de
Google Photos, Google Play y el propio sistema Android— sobre los que no tenemos
control. Cambios en esos servicios pueden alterar o impedir el funcionamiento de
algunas funciones. Del mismo modo, ciertos fabricantes aplican restricciones de
ahorro de energía que pueden impedir que la aplicación detecte fotografías
nuevas; la aplicación te avisa de esa circunstancia y te guía para corregirla,
pero no puede resolverla por sí sola.</p>

<h2>6. Garantías</h2>
<p>La aplicación se proporciona «tal cual». Dentro de lo permitido por la ley, no
se ofrece ninguna garantía de que vaya a funcionar sin interrupciones ni errores.
<strong>Snapgate nunca elimina fotografías</strong>: descartar una foto significa
no subirla, y el archivo permanece en tu dispositivo.</p>

<h2>7. Responsabilidad</h2>
<p>En la medida máxima permitida por la legislación aplicable, la responsabilidad
total del desarrollador queda limitada al importe que hayas pagado por la
aplicación. Nada en estas condiciones limita los derechos que la normativa de
consumo te reconozca de forma imperativa.</p>

<h2>8. Terminación</h2>
<p>Puedes dejar de usar la aplicación cuando quieras desinstalándola. La licencia
termina si incumples estas condiciones de forma sustancial.</p>

<h2>9. Legislación aplicable</h2>
<p>Estas condiciones se rigen por la legislación española. Si actúas como
consumidor, conservas el derecho a acudir a los tribunales de tu lugar de
residencia.</p>

<h2>10. Contacto</h2>
<p><a href="mailto:{CONTACT}">{CONTACT}</a></p>
""",
}

PRIVACY["en"] = {
    "title": "Privacy policy · Snapgate",
    "description": "What data Snapgate handles and, above all, what it cannot do.",
    "h1": "Privacy policy",
    "meta": "Last updated: 17 September 2026",
    "body": f"""
<p>Snapgate is an Android application that lets you decide, photo by photo, which
images are uploaded to your Google Photos library and which are not.</p>

<p>The one-sentence summary: <strong>we operate no servers</strong>, your photos
never leave your device except towards your own Google account, and only when you
ask for it.</p>

<h2>Who is responsible</h2>
<p>The developer of Snapgate. You can get in touch at
<a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>What data is handled, and why</h2>

<h3>Your photos</h3>
<p>The app reads images from the folders you configure so it can show them to you
and ask what to do with them. That reading happens entirely on your device. No
copies are sent anywhere, nothing is analysed, and nothing is retained outside your
phone's own storage.</p>

<h3>Your Google account</h3>
<p>If you choose to connect it, Snapgate requests two specific permissions:</p>
<ul>
  <li><code>photoslibrary.appendonly</code>, which allows it <strong>only to add</strong>
      photos to your library.</li>
  <li><code>photoslibrary.readonly.appcreateddata</code>, which allows it to see only
      the albums the app itself created.</li>
</ul>
<p>With those permissions the app <strong>cannot read, modify or delete</strong> any
photo or album you already had. That restriction is enforced by Google, not promised
by us. The access token is stored in the app's private storage on your device and is
never transmitted to third parties.</p>

<h3>Your location</h3>
<p>Only if you enable place-based rules and grant the permission. The last known
position is read at the moment a photo is evaluated, to check whether it matches a
rule you created. It is not logged, not stored and never leaves the device.</p>

<h3>Usage data</h3>
<p>None. There is no analytics, no measurement tooling, no advertising identifiers
and no automatic crash reporting.</p>

<h2>Google user data accessed by the application</h2>

<p>If you connect your account, Snapgate requests exactly two Google Photos API
scopes and no others:</p>

<table>
  <tr><th>Scope</th><th>What it allows, exactly</th></tr>
  <tr>
    <td><code>photoslibrary.appendonly</code></td>
    <td>Only to <strong>add</strong> photos and create albums in your library. It
        is write-only: it grants no read access to anything you already have.</td>
  </tr>
  <tr>
    <td><code>photoslibrary.readonly.appcreateddata</code></td>
    <td>To read <strong>only</strong> the albums created by the application
        itself, so you can choose which one to send photos to.</td>
  </tr>
</table>

<p>With those scopes, the Google user data the application can access is limited
to:</p>

<ul>
  <li>The <strong>title and identifier of albums created by the application
      itself</strong>, in order to offer them as a destination.</li>
  <li>The <strong>access and refresh tokens</strong> Google issues when you
      authorise it.</li>
</ul>

<p>The application <strong>does not access</strong> your existing photos or
albums, your name, email address, contacts, calendar, Drive files or any other
Google service. That limitation does not rest on our good faith: Google enforces
it by granting only those scopes, and you can verify it on the consent screen
before accepting.</p>

<p><strong>What it is used for.</strong> Solely to upload to your library the
photographs you explicitly approve, and to offer app-created albums as a
destination. It is not used for advertising, profiling or model training, and it
is never sold or transferred to anyone.</p>

<h2>How this data is protected</h2>

<ul>
  <li><strong>In transit.</strong> All communication with Google's APIs is
      encrypted using HTTPS/TLS. The app talks to no other server, because no
      server of ours exists.</li>
  <li><strong>At rest.</strong> Tokens are stored in the application's private
      storage, isolated by the Android sandbox, which no other app on the device
      can reach.</li>
  <li><strong>Excluded from backups.</strong> The file holding the tokens is
      excluded from both cloud backup and direct device-to-device transfer. The
      credential never leaves the phone where you authorised it.</li>
  <li><strong>Least privilege.</strong> The most restricted write scope available
      for this purpose is requested, rather than full library access.</li>
  <li><strong>Retention and deletion.</strong> Tokens are kept only while the
      account remains connected. They are deleted when you disconnect it from the
      app's settings and when you uninstall the app. You can also revoke access at
      any time from your
      <a href="https://myaccount.google.com/permissions">Google account
      permissions page</a>, which invalidates the tokens immediately.</li>
  <li><strong>No third parties.</strong> There is no analytics, no advertising SDK
      and no crash-reporting service that could receive this data.</li>
</ul>

<h2>Who it is shared with</h2>
<p>Nobody. The only network communication the app performs is:</p>
<ul>
  <li>With Google's servers, to upload the photos you approve to <em>your</em> library.</li>
  <li>With Google Play, to verify your purchase.</li>
</ul>

<h2>Retention</h2>
<p>Settings, the list of already-decided photos and the access token are kept on your
device for as long as the app is installed. Uninstalling removes them completely.</p>

<h2>Your rights</h2>
<p>You can disconnect your Google account from the app's settings at any time, and
revoke access entirely from your
<a href="https://myaccount.google.com/permissions">Google account permissions page</a>.
Since we hold no data about you on any system of ours, there is nothing for us to
provide or erase.</p>

<p>If you live in the European Union, the GDPR applies to you. Because we process no
personal data outside your device, exercising those rights is resolved by the
uninstall and revocation described above. Write to us with any question.</p>

<h2>Children</h2>
<p>Snapgate is not directed at children under 13 and does not knowingly collect data
from them.</p>

<h2>Changes</h2>
<p>If this policy changes, the updated version will be published on this page with its
date. Substantial changes will also be announced inside the app.</p>
""",
}

TERMS["en"] = {
    "title": "Terms and conditions · Snapgate",
    "description": "Terms of use for the Snapgate application.",
    "h1": "Terms and conditions",
    "meta": "Last updated: 17 September 2026",
    "body": f"""
<p>By installing and using Snapgate you accept these terms. If you do not agree with
them, do not use the app.</p>

<h2>1. What Snapgate is</h2>
<p>An Android application that lets you decide which photos on your device are uploaded
to your Google Photos library. Snapgate <strong>is not a Google product</strong> and is
not affiliated with, sponsored by or endorsed by Google LLC. Google Photos, Google Play
and Android are trademarks of Google LLC.</p>

<h2>2. Licence</h2>
<p>You are granted a personal, non-transferable, non-exclusive licence to use the app on
devices associated with your Google Play account. You may not resell it, redistribute it
or attempt to circumvent the purchase mechanism.</p>

<h2>3. Trial and purchase</h2>
<p>Snapgate can be used free of charge for fourteen days. After that, continuing to use
it requires a <strong>one-time payment</strong> through Google Play; it is not a
subscription and does not renew. Refunds are governed by Google Play's policy, which
currently includes an automatic refund within two hours of purchase.</p>

<h2>4. Acceptable use</h2>
<p>You agree to use the app only with photographs you hold rights to, and not to use it
to process unlawful content.</p>

<h2>5. Reliance on third-party services</h2>
<p>The app depends on services outside our control — the Google Photos API, Google Play
and Android itself. Changes to those services may alter or prevent some features from
working. Likewise, certain manufacturers apply battery-saving restrictions that can stop
the app from detecting new photos; the app warns you about this and guides you to fix
it, but cannot resolve it on its own.</p>

<h2>6. Warranties</h2>
<p>The app is provided "as is". To the extent permitted by law, no warranty is given that
it will operate uninterrupted or error-free. <strong>Snapgate never deletes
photographs</strong>: discarding a photo means not uploading it, and the file remains on
your device.</p>

<h2>7. Liability</h2>
<p>To the maximum extent permitted by applicable law, the developer's total liability is
limited to the amount you paid for the app. Nothing in these terms limits any rights
mandatory consumer law grants you.</p>

<h2>8. Termination</h2>
<p>You may stop using the app at any time by uninstalling it. The licence terminates if
you materially breach these terms.</p>

<h2>9. Governing law</h2>
<p>These terms are governed by Spanish law. If you are acting as a consumer, you retain
the right to bring proceedings in the courts of your place of residence.</p>

<h2>10. Contact</h2>
<p><a href="mailto:{CONTACT}">{CONTACT}</a></p>
""",
}

# --- Português ---

PRIVACY["pt"] = {
    "title": "Política de privacidade · Snapgate",
    "description": "Que dados o Snapgate trata e, sobretudo, o que não pode fazer.",
    "h1": "Política de privacidade",
    "meta": "Última atualização: 17 de setembro de 2026",
    "body": f"""
<p>O Snapgate é uma aplicação Android que te permite decidir, foto a foto, quais são
enviadas para a tua biblioteca do Google Fotos.</p>
<p>Resumo numa frase: <strong>não existe nenhum servidor nosso</strong>, as tuas fotos
não saem do dispositivo exceto para a tua própria conta Google, e só quando o pedes.</p>

<h2>Responsável</h2>
<p>O programador do Snapgate. Contacto: <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>Que dados são tratados</h2>
<h3>As tuas fotos</h3>
<p>A app lê as imagens das pastas que configuras para tas mostrar e perguntar o que
fazer. Essa leitura acontece inteiramente no teu dispositivo. Não são enviadas cópias
para lado nenhum nem conservadas fora do telemóvel.</p>

<h3>A tua conta Google</h3>
<p>Se a ligares, são pedidas duas permissões: <code>photoslibrary.appendonly</code>, que
permite <strong>apenas adicionar</strong> fotos, e
<code>photoslibrary.readonly.appcreateddata</code>, que permite ver só os álbuns criados
pela própria app. Com elas a aplicação <strong>não pode ler, alterar nem eliminar</strong>
nada do que já tens. A restrição é imposta pela Google. O testigo de acesso fica no
armazenamento privado da app e nunca é transmitido a terceiros.</p>

<h3>A tua localização</h3>
<p>Só se ativares as regras por lugar. É consultada no momento de avaliar uma foto, para
verificar se corresponde a uma regra tua. Não é registada, não é guardada e não sai do
dispositivo.</p>

<h3>Dados de utilização</h3>
<p>Nenhuns. Sem analítica, sem rastreadores, sem identificadores publicitários e sem
relatórios automáticos de erros.</p>

<h2>Dados de utilizador do Google a que a aplicação acede</h2>

<p>Se ligares a tua conta, o Snapgate pede exatamente duas permissões da API do
Google Photos e mais nenhuma:</p>

<table>
  <tr><th>Permissão</th><th>O que permite exatamente</th></tr>
  <tr><td><code>photoslibrary.appendonly</code></td>
      <td>Só <strong>adicionar</strong> fotos e criar álbuns na tua biblioteca. É
          de escrita: não dá acesso de leitura a nada do que já tens.</td></tr>
  <tr><td><code>photoslibrary.readonly.appcreateddata</code></td>
      <td>Ler <strong>apenas</strong> os álbuns criados pela própria aplicação,
          para poderes escolher para qual enviar as fotos.</td></tr>
</table>

<p>Com essas permissões, os dados da tua conta Google a que a aplicação tem acesso
limitam-se a:</p>
<ul>
  <li>O <strong>título e identificador dos álbuns criados pela própria
      aplicação</strong>, para tos mostrar como destino.</li>
  <li>Os <strong>tokens de acesso e de renovação</strong> emitidos pela Google ao
      autorizares.</li>
</ul>

<p>A aplicação <strong>não acede</strong> às tuas fotos ou álbuns existentes, nem
ao teu nome, email, contactos, calendário, ficheiros do Drive ou qualquer outro
serviço Google. Essa limitação não depende da nossa boa-fé: é imposta pela Google
ao conceder apenas essas permissões, e podes confirmá-la no ecrã de consentimento
antes de aceitares.</p>

<p><strong>Para que servem.</strong> Unicamente para enviar para a tua biblioteca
as fotografias que aprovas de forma explícita e para te oferecer como destino os
álbuns criados pela aplicação. Não são usados para publicidade, perfis ou treino
de modelos, nem vendidos ou cedidos a ninguém.</p>

<h2>Como estes dados são protegidos</h2>
<ul>
  <li><strong>Em trânsito.</strong> Toda a comunicação com as API da Google é
      cifrada com HTTPS/TLS. A app não comunica com mais nenhum servidor, porque
      não existe nenhum servidor nosso.</li>
  <li><strong>Em repouso.</strong> Os tokens ficam no armazenamento privado da
      aplicação, isolado pelo sandbox do Android, onde nenhuma outra app do
      dispositivo chega.</li>
  <li><strong>Fora das cópias de segurança.</strong> O ficheiro com os tokens está
      excluído tanto da cópia na nuvem como da transferência direta para um
      dispositivo novo. A credencial nunca sai do telemóvel onde a autorizaste.</li>
  <li><strong>Mínimo indispensável.</strong> Pede-se a permissão de escrita mais
      restrita que existe para esta função, em vez de acesso total à biblioteca.</li>
  <li><strong>Conservação e eliminação.</strong> Os tokens duram enquanto a conta
      estiver ligada. São eliminados ao desligá-la nas definições e ao desinstalar.
      Podes ainda revogar o acesso a qualquer momento na
      <a href="https://myaccount.google.com/permissions">página de permissões da
      tua conta Google</a>, o que os invalida de imediato.</li>
  <li><strong>Sem terceiros.</strong> Não há analítica, SDK publicitários nem
      serviços de registo de erros que pudessem receber estes dados.</li>
</ul>

<h2>Com quem são partilhados</h2>
<p>Com ninguém. As únicas comunicações de rede são com os servidores da Google, para
enviar para <em>a tua</em> biblioteca o que aprovas, e com a Google Play, para verificar
a compra.</p>

<h2>Conservação</h2>
<p>As definições e o testigo de acesso ficam no teu dispositivo enquanto a app estiver
instalada. Desinstalar elimina tudo.</p>

<h2>Os teus direitos</h2>
<p>Podes desligar a conta nas definições da app e revogar o acesso na
<a href="https://myaccount.google.com/permissions">página de permissões da tua conta
Google</a>. Como não guardamos dados teus em nenhum sistema nosso, não há nada para
fornecer nem apagar do nosso lado. Se resides na União Europeia, aplica-se o RGPD.</p>

<h2>Menores</h2>
<p>O Snapgate não se dirige a menores de 13 anos nem recolhe conscientemente dados deles.</p>

<h2>Alterações</h2>
<p>Qualquer alteração será publicada nesta página com a respetiva data.</p>
""",
}

TERMS["pt"] = {
    "title": "Termos e condições · Snapgate",
    "description": "Condições de utilização da aplicação Snapgate.",
    "h1": "Termos e condições",
    "meta": "Última atualização: 17 de setembro de 2026",
    "body": f"""
<p>Ao instalar e usar o Snapgate aceitas estas condições. Se não concordares, não uses a
aplicação.</p>

<h2>1. O que é o Snapgate</h2>
<p>Uma aplicação Android que te permite decidir que fotos do teu dispositivo são enviadas
para a tua biblioteca do Google Fotos. O Snapgate <strong>não é um produto da Google</strong>
nem está afiliado ou patrocinado pela Google LLC. Google Fotos, Google Play e Android são
marcas da Google LLC.</p>

<h2>2. Licença</h2>
<p>É-te concedida uma licença pessoal, intransmissível e não exclusiva para usar a app nos
dispositivos associados à tua conta Google Play. Não podes revendê-la, redistribuí-la nem
contornar o mecanismo de compra.</p>

<h2>3. Experiência e compra</h2>
<p>Catorze dias gratuitos. Depois, continuar a usá-la exige um <strong>pagamento único</strong>
através da Google Play; não é subscrição e não se renova. Os reembolsos regem-se pela
política da Google Play.</p>

<h2>4. Utilização correta</h2>
<p>Comprometes-te a usar a app apenas com fotografias sobre as quais tenhas direitos e a não
a utilizar para conteúdo ilícito.</p>

<h2>5. Dependência de serviços de terceiros</h2>
<p>O funcionamento depende de serviços fora do nosso controlo — a API do Google Photos, a
Google Play e o próprio Android. Além disso, alguns fabricantes aplicam restrições de
poupança de energia que podem impedir a deteção de fotos novas; a app avisa-te e orienta-te,
mas não o pode resolver sozinha.</p>

<h2>6. Garantias</h2>
<p>A aplicação é fornecida «tal como está». Dentro do permitido por lei, não se garante
funcionamento ininterrupto ou sem erros. <strong>O Snapgate nunca elimina fotografias</strong>:
descartar significa não enviar, e o ficheiro permanece no dispositivo.</p>

<h2>7. Responsabilidade</h2>
<p>Na medida máxima permitida por lei, a responsabilidade total do programador limita-se ao
valor pago pela aplicação. Nada nestas condições limita direitos imperativos de consumo.</p>

<h2>8. Cessação</h2>
<p>Podes deixar de usar a app desinstalando-a. A licença cessa em caso de incumprimento
substancial destas condições.</p>

<h2>9. Legislação aplicável</h2>
<p>Estas condições regem-se pela lei espanhola. Como consumidor, mantens o direito de
recorrer aos tribunais do teu local de residência.</p>

<h2>10. Contacto</h2>
<p><a href="mailto:{CONTACT}">{CONTACT}</a></p>
""",
}

# --- Français ---

PRIVACY["fr"] = {
    "title": "Politique de confidentialité · Snapgate",
    "description": "Quelles données Snapgate traite et, surtout, ce qu'elle ne peut pas faire.",
    "h1": "Politique de confidentialité",
    "meta": "Dernière mise à jour : 17 septembre 2026",
    "body": f"""
<p>Snapgate est une application Android qui vous permet de décider, photo par photo,
lesquelles sont envoyées vers votre bibliothèque Google Photos.</p>
<p>Résumé en une phrase : <strong>nous n'exploitons aucun serveur</strong>, vos photos ne
quittent pas votre appareil sauf vers votre propre compte Google, et uniquement à votre
demande.</p>

<h2>Responsable</h2>
<p>Le développeur de Snapgate. Contact : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>Quelles données sont traitées</h2>
<h3>Vos photos</h3>
<p>L'application lit les images des dossiers que vous configurez afin de vous les présenter
et de vous demander quoi en faire. Cette lecture se fait entièrement sur votre appareil.
Aucune copie n'est envoyée nulle part.</p>

<h3>Votre compte Google</h3>
<p>Si vous le connectez, deux autorisations sont demandées :
<code>photoslibrary.appendonly</code>, qui permet <strong>uniquement d'ajouter</strong> des
photos, et <code>photoslibrary.readonly.appcreateddata</code>, qui permet de voir seulement
les albums créés par l'application. Avec elles, l'app <strong>ne peut ni lire, ni modifier,
ni supprimer</strong> ce que vous possédez déjà. Cette restriction est imposée par Google.
Le jeton d'accès reste dans le stockage privé de l'application.</p>

<h3>Votre position</h3>
<p>Uniquement si vous activez les règles de lieu. Elle est lue au moment d'évaluer une photo,
pour vérifier si elle correspond à une règle que vous avez créée. Elle n'est ni journalisée,
ni stockée, et ne quitte jamais l'appareil.</p>

<h3>Données d'usage</h3>
<p>Aucune. Pas d'analytique, pas de traqueurs, pas d'identifiants publicitaires, pas de
rapports de plantage automatiques.</p>

<h2>Données utilisateur Google auxquelles l'application accède</h2>

<p>Si vous connectez votre compte, Snapgate demande exactement deux autorisations
de l'API Google Photos, et aucune autre :</p>

<table>
  <tr><th>Autorisation</th><th>Ce qu'elle permet, exactement</th></tr>
  <tr><td><code>photoslibrary.appendonly</code></td>
      <td>Uniquement <strong>ajouter</strong> des photos et créer des albums dans
          votre bibliothèque. En écriture seule : aucun accès en lecture à ce que
          vous possédez déjà.</td></tr>
  <tr><td><code>photoslibrary.readonly.appcreateddata</code></td>
      <td>Lire <strong>seulement</strong> les albums créés par l'application
          elle-même, afin que vous puissiez choisir la destination.</td></tr>
</table>

<p>Avec ces autorisations, les données de votre compte Google auxquelles
l'application a accès se limitent à :</p>
<ul>
  <li>Le <strong>titre et l'identifiant des albums créés par l'application
      elle-même</strong>, pour vous les proposer comme destination.</li>
  <li>Les <strong>jetons d'accès et de rafraîchissement</strong> délivrés par
      Google lors de l'autorisation.</li>
</ul>

<p>L'application <strong>n'accède pas</strong> à vos photos ou albums existants,
ni à votre nom, adresse e-mail, contacts, agenda, fichiers Drive ou tout autre
service Google. Cette limite ne repose pas sur notre bonne foi : Google l'impose
en n'accordant que ces autorisations, et vous pouvez le vérifier sur l'écran de
consentement avant d'accepter.</p>

<p><strong>À quoi elles servent.</strong> Uniquement à envoyer dans votre
bibliothèque les photographies que vous approuvez explicitement, et à vous
proposer comme destination les albums créés par l'application. Elles ne servent ni
à la publicité, ni au profilage, ni à l'entraînement de modèles, et ne sont jamais
vendues ni cédées.</p>

<h2>Comment ces données sont protégées</h2>
<ul>
  <li><strong>En transit.</strong> Toute communication avec les API de Google est
      chiffrée via HTTPS/TLS. L'app ne parle à aucun autre serveur, car aucun
      serveur de notre part n'existe.</li>
  <li><strong>Au repos.</strong> Les jetons sont stockés dans l'espace privé de
      l'application, isolé par le bac à sable d'Android, inaccessible aux autres
      applications.</li>
  <li><strong>Hors sauvegardes.</strong> Le fichier contenant les jetons est exclu
      à la fois de la sauvegarde cloud et du transfert direct vers un nouvel
      appareil. L'identifiant ne quitte jamais le téléphone où vous l'avez
      autorisé.</li>
  <li><strong>Moindre privilège.</strong> L'autorisation d'écriture la plus
      restreinte possible est demandée, plutôt qu'un accès complet.</li>
  <li><strong>Conservation et suppression.</strong> Les jetons ne durent que tant
      que le compte reste connecté. Ils sont supprimés à la déconnexion depuis les
      réglages et à la désinstallation. Vous pouvez aussi révoquer l'accès à tout
      moment depuis la
      <a href="https://myaccount.google.com/permissions">page des autorisations de
      votre compte Google</a>, ce qui les invalide immédiatement.</li>
  <li><strong>Aucun tiers.</strong> Pas d'analytique, pas de SDK publicitaire, pas
      de service de rapport de plantage susceptible de recevoir ces données.</li>
</ul>

<h2>Partage</h2>
<p>Avec personne. Les seules communications réseau se font avec les serveurs de Google, pour
envoyer vers <em>votre</em> bibliothèque ce que vous approuvez, et avec Google Play pour
vérifier votre achat.</p>

<h2>Conservation</h2>
<p>Les réglages et le jeton d'accès restent sur votre appareil tant que l'application est
installée. La désinstaller les supprime entièrement.</p>

<h2>Vos droits</h2>
<p>Vous pouvez déconnecter votre compte depuis les réglages de l'app et révoquer l'accès
depuis la <a href="https://myaccount.google.com/permissions">page des autorisations de votre
compte Google</a>. Comme nous ne détenons aucune donnée vous concernant, il n'y a rien à
fournir ni à effacer de notre côté. Si vous résidez dans l'Union européenne, le RGPD
s'applique.</p>

<h2>Mineurs</h2>
<p>Snapgate ne s'adresse pas aux moins de 13 ans et ne collecte pas sciemment leurs données.</p>

<h2>Modifications</h2>
<p>Toute modification sera publiée sur cette page avec sa date.</p>
""",
}

TERMS["fr"] = {
    "title": "Conditions générales · Snapgate",
    "description": "Conditions d'utilisation de l'application Snapgate.",
    "h1": "Conditions générales",
    "meta": "Dernière mise à jour : 17 septembre 2026",
    "body": f"""
<p>En installant et en utilisant Snapgate, vous acceptez ces conditions. Si vous n'êtes pas
d'accord, n'utilisez pas l'application.</p>

<h2>1. Ce qu'est Snapgate</h2>
<p>Une application Android qui vous permet de décider quelles photos de votre appareil sont
envoyées vers votre bibliothèque Google Photos. Snapgate <strong>n'est pas un produit
Google</strong> et n'est ni affiliée ni sponsorisée par Google LLC. Google Photos, Google Play
et Android sont des marques de Google LLC.</p>

<h2>2. Licence</h2>
<p>Vous recevez une licence personnelle, non transférable et non exclusive pour utiliser
l'application sur les appareils associés à votre compte Google Play. Sa revente, sa
redistribution ou le contournement du mécanisme d'achat sont interdits.</p>

<h2>3. Essai et achat</h2>
<p>Quatorze jours gratuits. Ensuite, poursuivre l'utilisation nécessite un <strong>achat
unique</strong> via Google Play ; ce n'est pas un abonnement et il ne se renouvelle pas. Les
remboursements relèvent de la politique de Google Play.</p>

<h2>4. Usage acceptable</h2>
<p>Vous vous engagez à n'utiliser l'application qu'avec des photographies sur lesquelles vous
détenez des droits, et à ne pas l'employer pour traiter des contenus illicites.</p>

<h2>5. Dépendance à des services tiers</h2>
<p>Le fonctionnement dépend de services hors de notre contrôle — l'API Google Photos, Google
Play et Android. Par ailleurs, certains fabricants appliquent des restrictions d'économie
d'énergie susceptibles d'empêcher la détection des nouvelles photos ; l'application vous en
avertit et vous guide, mais ne peut y remédier seule.</p>

<h2>6. Garanties</h2>
<p>L'application est fournie « en l'état ». Dans les limites permises par la loi, aucune
garantie de fonctionnement ininterrompu ou sans erreur n'est donnée. <strong>Snapgate ne
supprime jamais de photographies</strong> : écarter signifie ne pas envoyer, et le fichier
reste sur votre appareil.</p>

<h2>7. Responsabilité</h2>
<p>Dans la mesure maximale permise par la loi applicable, la responsabilité totale du
développeur est limitée au montant que vous avez payé. Rien ici ne limite vos droits
impératifs de consommateur.</p>

<h2>8. Résiliation</h2>
<p>Vous pouvez cesser d'utiliser l'application à tout moment en la désinstallant. La licence
prend fin en cas de manquement substantiel à ces conditions.</p>

<h2>9. Droit applicable</h2>
<p>Ces conditions sont régies par le droit espagnol. En tant que consommateur, vous conservez
le droit de saisir les tribunaux de votre lieu de résidence.</p>

<h2>10. Contact</h2>
<p><a href="mailto:{CONTACT}">{CONTACT}</a></p>
""",
}

# --- Deutsch ---

PRIVACY["de"] = {
    "title": "Datenschutzerklärung · Snapgate",
    "description": "Welche Daten Snapgate verarbeitet und vor allem, was die App nicht kann.",
    "h1": "Datenschutzerklärung",
    "meta": "Zuletzt aktualisiert: 17. September 2026",
    "body": f"""
<p>Snapgate ist eine Android-App, mit der du Foto für Foto entscheidest, welche Bilder in
deine Google-Fotos-Mediathek hochgeladen werden.</p>
<p>Die Zusammenfassung in einem Satz: <strong>Wir betreiben keine Server</strong>, deine
Fotos verlassen dein Gerät nur in Richtung deines eigenen Google-Kontos, und nur wenn du es
verlangst.</p>

<h2>Verantwortlich</h2>
<p>Der Entwickler von Snapgate. Kontakt: <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>Welche Daten verarbeitet werden</h2>
<h3>Deine Fotos</h3>
<p>Die App liest Bilder aus den von dir eingestellten Ordnern, um sie dir zu zeigen und zu
fragen, was damit geschehen soll. Das geschieht vollständig auf deinem Gerät. Es werden keine
Kopien versendet.</p>

<h3>Dein Google-Konto</h3>
<p>Wenn du es verbindest, werden zwei Berechtigungen angefragt:
<code>photoslibrary.appendonly</code>, die <strong>nur das Hinzufügen</strong> von Fotos
erlaubt, und <code>photoslibrary.readonly.appcreateddata</code>, die nur die von der App
selbst erstellten Alben sichtbar macht. Damit kann die App <strong>nichts lesen, ändern oder
löschen</strong>, was du bereits hast. Diese Einschränkung erzwingt Google. Das Zugriffstoken
bleibt im privaten Speicher der App.</p>

<h3>Dein Standort</h3>
<p>Nur wenn du Ortsregeln aktivierst. Er wird im Moment der Auswertung eines Fotos gelesen,
um zu prüfen, ob eine deiner Regeln zutrifft. Er wird nicht protokolliert, nicht gespeichert
und verlässt das Gerät nie.</p>

<h3>Nutzungsdaten</h3>
<p>Keine. Keine Analyse, kein Tracking, keine Werbe-IDs, keine automatischen Absturzberichte.</p>

<h2>Google-Nutzerdaten, auf die die App zugreift</h2>

<p>Wenn du dein Konto verbindest, fordert Snapgate genau zwei Berechtigungen der
Google-Photos-API an und keine weiteren:</p>

<table>
  <tr><th>Berechtigung</th><th>Was sie genau erlaubt</th></tr>
  <tr><td><code>photoslibrary.appendonly</code></td>
      <td>Nur Fotos <strong>hinzufügen</strong> und Alben anlegen. Schreibend:
          kein Lesezugriff auf das, was du bereits hast.</td></tr>
  <tr><td><code>photoslibrary.readonly.appcreateddata</code></td>
      <td><strong>Nur</strong> die von der App selbst erstellten Alben lesen,
          damit du ein Ziel auswählen kannst.</td></tr>
</table>

<p>Damit beschränken sich die zugänglichen Daten deines Google-Kontos auf:</p>
<ul>
  <li><strong>Titel und Kennung der von der App selbst erstellten Alben</strong>,
      um sie dir als Ziel anzubieten.</li>
  <li>Die von Google ausgestellten <strong>Zugriffs- und Aktualisierungstoken</strong>.</li>
</ul>

<p>Die App <strong>greift nicht</strong> auf deine vorhandenen Fotos oder Alben zu,
auch nicht auf Name, E-Mail, Kontakte, Kalender, Drive-Dateien oder andere
Google-Dienste. Diese Grenze beruht nicht auf unserem guten Willen: Google erzwingt
sie, indem es nur diese Berechtigungen erteilt, und du kannst es vor dem Zustimmen
auf dem Einwilligungsbildschirm prüfen.</p>

<p><strong>Wozu sie dienen.</strong> Ausschließlich dazu, die von dir ausdrücklich
freigegebenen Fotos in deine Mediathek zu laden und dir von der App erstellte Alben
als Ziel anzubieten. Nicht für Werbung, Profilbildung oder Modelltraining, und
niemals verkauft oder weitergegeben.</p>

<h2>Wie diese Daten geschützt werden</h2>
<ul>
  <li><strong>Bei der Übertragung.</strong> Die gesamte Kommunikation mit Googles
      APIs ist per HTTPS/TLS verschlüsselt. Mit anderen Servern spricht die App
      nicht, denn einen eigenen Server gibt es nicht.</li>
  <li><strong>Im Ruhezustand.</strong> Die Token liegen im privaten Speicher der
      App, abgeschottet durch die Android-Sandbox, für andere Apps unerreichbar.</li>
  <li><strong>Von Sicherungen ausgenommen.</strong> Die Datei mit den Token ist
      sowohl von der Cloud-Sicherung als auch von der Geräteübertragung
      ausgeschlossen. Die Zugangsdaten verlassen nie das Handy, auf dem du sie
      erteilt hast.</li>
  <li><strong>Geringstmögliche Rechte.</strong> Angefordert wird die
      restriktivste Schreibberechtigung statt vollem Mediathekzugriff.</li>
  <li><strong>Aufbewahrung und Löschung.</strong> Die Token bestehen nur, solange
      das Konto verbunden ist. Sie werden beim Trennen in den Einstellungen und
      beim Deinstallieren gelöscht. Du kannst den Zugriff zudem jederzeit auf der
      <a href="https://myaccount.google.com/permissions">Berechtigungsseite deines
      Google-Kontos</a> widerrufen, was sie sofort ungültig macht.</li>
  <li><strong>Keine Dritten.</strong> Keine Analyse, keine Werbe-SDKs, keine
      Absturzberichte, die diese Daten erhalten könnten.</li>
</ul>

<h2>Weitergabe</h2>
<p>An niemanden. Die einzige Netzwerkkommunikation erfolgt mit Googles Servern, um Freigegebenes
in <em>deine</em> Mediathek zu laden, und mit Google Play zur Kaufprüfung.</p>

<h2>Speicherdauer</h2>
<p>Einstellungen und Zugriffstoken bleiben auf deinem Gerät, solange die App installiert ist.
Das Deinstallieren löscht sie vollständig.</p>

<h2>Deine Rechte</h2>
<p>Du kannst dein Konto in den App-Einstellungen trennen und den Zugriff auf der
<a href="https://myaccount.google.com/permissions">Berechtigungsseite deines Google-Kontos</a>
vollständig widerrufen. Da wir keinerlei Daten über dich in eigenen Systemen halten, gibt es
unsererseits nichts herauszugeben oder zu löschen. In der EU gilt die DSGVO.</p>

<h2>Minderjährige</h2>
<p>Snapgate richtet sich nicht an Kinder unter 13 Jahren und erhebt wissentlich keine Daten
von ihnen.</p>

<h2>Änderungen</h2>
<p>Änderungen werden mit Datum auf dieser Seite veröffentlicht.</p>
""",
}

TERMS["de"] = {
    "title": "Nutzungsbedingungen · Snapgate",
    "description": "Nutzungsbedingungen der App Snapgate.",
    "h1": "Nutzungsbedingungen",
    "meta": "Zuletzt aktualisiert: 17. September 2026",
    "body": f"""
<p>Mit der Installation und Nutzung von Snapgate akzeptierst du diese Bedingungen. Wenn du
nicht einverstanden bist, nutze die App nicht.</p>

<h2>1. Was Snapgate ist</h2>
<p>Eine Android-App, mit der du entscheidest, welche Fotos deines Geräts in deine
Google-Fotos-Mediathek hochgeladen werden. Snapgate <strong>ist kein Google-Produkt</strong>
und weder mit Google LLC verbunden noch von ihr gesponsert. Google Fotos, Google Play und
Android sind Marken von Google LLC.</p>

<h2>2. Lizenz</h2>
<p>Du erhältst eine persönliche, nicht übertragbare und nicht ausschließliche Lizenz zur
Nutzung der App auf Geräten, die mit deinem Google-Play-Konto verknüpft sind. Weiterverkauf,
Weiterverbreitung oder das Umgehen des Kaufmechanismus sind untersagt.</p>

<h2>3. Test und Kauf</h2>
<p>Vierzehn Tage kostenlos. Danach erfordert die weitere Nutzung eine <strong>einmalige
Zahlung</strong> über Google Play; es ist kein Abo und verlängert sich nicht. Für Erstattungen
gilt die Richtlinie von Google Play.</p>

<h2>4. Zulässige Nutzung</h2>
<p>Du verpflichtest dich, die App nur mit Fotos zu verwenden, an denen du Rechte hast, und sie
nicht für rechtswidrige Inhalte einzusetzen.</p>

<h2>5. Abhängigkeit von Diensten Dritter</h2>
<p>Der Betrieb hängt von Diensten außerhalb unserer Kontrolle ab — der Google-Photos-API,
Google Play und Android selbst. Zudem wenden manche Hersteller Energiesparbeschränkungen an,
die das Erkennen neuer Fotos verhindern können; die App weist darauf hin und führt dich zur
Lösung, kann es aber nicht selbst beheben.</p>

<h2>6. Gewährleistung</h2>
<p>Die App wird „wie besehen“ bereitgestellt. Soweit gesetzlich zulässig, wird kein
unterbrechungs- oder fehlerfreier Betrieb zugesichert. <strong>Snapgate löscht niemals
Fotos</strong>: Verwerfen bedeutet Nicht-Hochladen, die Datei bleibt auf deinem Gerät.</p>

<h2>7. Haftung</h2>
<p>Soweit gesetzlich zulässig, ist die Gesamthaftung des Entwicklers auf den für die App
gezahlten Betrag begrenzt. Zwingende Verbraucherrechte bleiben unberührt.</p>

<h2>8. Beendigung</h2>
<p>Du kannst die Nutzung jederzeit durch Deinstallation beenden. Die Lizenz endet bei
wesentlichem Verstoß gegen diese Bedingungen.</p>

<h2>9. Anwendbares Recht</h2>
<p>Es gilt spanisches Recht. Als Verbraucher behältst du das Recht, die Gerichte deines
Wohnsitzes anzurufen.</p>

<h2>10. Kontakt</h2>
<p><a href="mailto:{CONTACT}">{CONTACT}</a></p>
""",
}

# --- Italiano ---

PRIVACY["it"] = {
    "title": "Informativa sulla privacy · Snapgate",
    "description": "Quali dati tratta Snapgate e, soprattutto, cosa non può fare.",
    "h1": "Informativa sulla privacy",
    "meta": "Ultimo aggiornamento: 17 settembre 2026",
    "body": f"""
<p>Snapgate è un'app Android che ti permette di decidere, foto per foto, quali immagini
vengono caricate nella tua libreria di Google Foto.</p>
<p>Il riassunto in una frase: <strong>non esiste alcun nostro server</strong>, le tue foto non
lasciano il dispositivo se non verso il tuo account Google, e solo quando lo chiedi tu.</p>

<h2>Titolare</h2>
<p>Lo sviluppatore di Snapgate. Contatto: <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>Quali dati vengono trattati</h2>
<h3>Le tue foto</h3>
<p>L'app legge le immagini delle cartelle che configuri per mostrartele e chiederti cosa
farne. Questa lettura avviene interamente sul tuo dispositivo. Nessuna copia viene inviata
altrove.</p>

<h3>Il tuo account Google</h3>
<p>Se lo colleghi, vengono richiesti due permessi: <code>photoslibrary.appendonly</code>, che
consente <strong>solo di aggiungere</strong> foto, e
<code>photoslibrary.readonly.appcreateddata</code>, che consente di vedere soltanto gli album
creati dall'app stessa. Con essi l'app <strong>non può leggere, modificare né eliminare</strong>
nulla di ciò che possiedi già. La restrizione è imposta da Google. Il token di accesso resta
nell'archivio privato dell'app.</p>

<h3>La tua posizione</h3>
<p>Solo se attivi le regole per luogo. Viene letta nel momento in cui si valuta una foto, per
verificare se corrisponde a una tua regola. Non viene registrata, né salvata, né esce dal
dispositivo.</p>

<h3>Dati di utilizzo</h3>
<p>Nessuno. Niente analitica, niente tracciamento, nessun identificatore pubblicitario e
nessun rapporto automatico sugli arresti anomali.</p>

<h2>Dati utente Google a cui accede l'applicazione</h2>

<p>Se colleghi il tuo account, Snapgate richiede esattamente due permessi dell'API
di Google Foto e nessun altro:</p>

<table>
  <tr><th>Permesso</th><th>Cosa consente esattamente</th></tr>
  <tr><td><code>photoslibrary.appendonly</code></td>
      <td>Solo <strong>aggiungere</strong> foto e creare album nella tua libreria.
          È in scrittura: non dà accesso in lettura a ciò che hai già.</td></tr>
  <tr><td><code>photoslibrary.readonly.appcreateddata</code></td>
      <td>Leggere <strong>soltanto</strong> gli album creati dall'app stessa, per
          poter scegliere la destinazione.</td></tr>
</table>

<p>Con questi permessi, i dati del tuo account Google a cui l'app accede si
limitano a:</p>
<ul>
  <li><strong>Titolo e identificatore degli album creati dall'app stessa</strong>,
      per proportele come destinazione.</li>
  <li>I <strong>token di accesso e di aggiornamento</strong> emessi da Google.</li>
</ul>

<p>L'app <strong>non accede</strong> alle tue foto o ai tuoi album esistenti, né a
nome, email, contatti, calendario, file di Drive o altri servizi Google. Questo
limite non dipende dalla nostra buona fede: lo impone Google concedendo solo questi
permessi, e puoi verificarlo nella schermata di consenso prima di accettare.</p>

<p><strong>A cosa servono.</strong> Unicamente a caricare nella tua libreria le
fotografie che approvi esplicitamente e a offrirti come destinazione gli album
creati dall'app. Non servono per pubblicità, profilazione o addestramento di
modelli, e non vengono mai venduti né ceduti.</p>

<h2>Come vengono protetti questi dati</h2>
<ul>
  <li><strong>In transito.</strong> Tutte le comunicazioni con le API di Google
      sono cifrate con HTTPS/TLS. L'app non parla con nessun altro server, perché
      un nostro server non esiste.</li>
  <li><strong>A riposo.</strong> I token restano nell'archivio privato dell'app,
      isolato dalla sandbox di Android, irraggiungibile da altre app.</li>
  <li><strong>Fuori dai backup.</strong> Il file con i token è escluso sia dal
      backup su cloud sia dal trasferimento diretto verso un nuovo dispositivo. La
      credenziale non lascia mai il telefono su cui l'hai autorizzata.</li>
  <li><strong>Privilegio minimo.</strong> Si richiede il permesso di scrittura più
      ristretto disponibile, invece dell'accesso completo alla libreria.</li>
  <li><strong>Conservazione ed eliminazione.</strong> I token durano finché
      l'account resta collegato. Vengono eliminati scollegandolo dalle impostazioni
      e disinstallando l'app. Puoi inoltre revocare l'accesso in qualsiasi momento
      dalla <a href="https://myaccount.google.com/permissions">pagina dei permessi
      del tuo account Google</a>, cosa che li invalida subito.</li>
  <li><strong>Nessun terzo.</strong> Nessuna analitica, nessun SDK pubblicitario,
      nessun servizio di segnalazione errori che possa ricevere questi dati.</li>
</ul>

<h2>Condivisione</h2>
<p>Con nessuno. Le uniche comunicazioni di rete avvengono con i server di Google, per caricare
nella <em>tua</em> libreria ciò che approvi, e con Google Play per verificare l'acquisto.</p>

<h2>Conservazione</h2>
<p>Impostazioni e token restano sul dispositivo finché l'app è installata. Disinstallarla li
elimina completamente.</p>

<h2>I tuoi diritti</h2>
<p>Puoi scollegare l'account dalle impostazioni dell'app e revocare l'accesso dalla
<a href="https://myaccount.google.com/permissions">pagina dei permessi del tuo account
Google</a>. Poiché non conserviamo dati che ti riguardano su alcun nostro sistema, non c'è
nulla da fornire o cancellare da parte nostra. Se risiedi nell'Unione Europea si applica il
GDPR.</p>

<h2>Minori</h2>
<p>Snapgate non è rivolta a minori di 13 anni e non raccoglie consapevolmente i loro dati.</p>

<h2>Modifiche</h2>
<p>Ogni modifica sarà pubblicata su questa pagina con la relativa data.</p>
""",
}

TERMS["it"] = {
    "title": "Termini e condizioni · Snapgate",
    "description": "Condizioni d'uso dell'applicazione Snapgate.",
    "h1": "Termini e condizioni",
    "meta": "Ultimo aggiornamento: 17 settembre 2026",
    "body": f"""
<p>Installando e usando Snapgate accetti queste condizioni. Se non sei d'accordo, non usare
l'applicazione.</p>

<h2>1. Cos'è Snapgate</h2>
<p>Un'app Android che ti permette di decidere quali foto del tuo dispositivo vengono caricate
nella tua libreria di Google Foto. Snapgate <strong>non è un prodotto Google</strong> e non è
affiliata né sponsorizzata da Google LLC. Google Foto, Google Play e Android sono marchi di
Google LLC.</p>

<h2>2. Licenza</h2>
<p>Ti viene concessa una licenza personale, non trasferibile e non esclusiva per usare l'app
sui dispositivi associati al tuo account Google Play. Non puoi rivenderla, ridistribuirla né
aggirare il meccanismo di acquisto.</p>

<h2>3. Prova e acquisto</h2>
<p>Quattordici giorni gratuiti. Dopo, continuare a usarla richiede un <strong>acquisto
unico</strong> tramite Google Play; non è un abbonamento e non si rinnova. I rimborsi seguono
la politica di Google Play.</p>

<h2>4. Uso corretto</h2>
<p>Ti impegni a usare l'app solo con fotografie sulle quali detieni diritti e a non impiegarla
per contenuti illeciti.</p>

<h2>5. Dipendenza da servizi di terzi</h2>
<p>Il funzionamento dipende da servizi fuori dal nostro controllo — l'API di Google Photos,
Google Play e Android stesso. Inoltre alcuni produttori applicano restrizioni di risparmio
energetico che possono impedire il rilevamento di foto nuove; l'app te lo segnala e ti guida,
ma non può risolverlo da sola.</p>

<h2>6. Garanzie</h2>
<p>L'app è fornita «così com'è». Nei limiti consentiti dalla legge non si garantisce un
funzionamento ininterrotto o privo di errori. <strong>Snapgate non elimina mai
fotografie</strong>: scartare significa non caricare, e il file resta sul dispositivo.</p>

<h2>7. Responsabilità</h2>
<p>Nella misura massima consentita dalla legge applicabile, la responsabilità totale dello
sviluppatore è limitata all'importo pagato per l'app. Nulla in queste condizioni limita i
diritti inderogabili del consumatore.</p>

<h2>8. Cessazione</h2>
<p>Puoi smettere di usare l'app in qualsiasi momento disinstallandola. La licenza cessa in
caso di violazione sostanziale di queste condizioni.</p>

<h2>9. Legge applicabile</h2>
<p>Queste condizioni sono regolate dalla legge spagnola. In qualità di consumatore mantieni il
diritto di rivolgerti ai tribunali del tuo luogo di residenza.</p>

<h2>10. Contatti</h2>
<p><a href="mailto:{CONTACT}">{CONTACT}</a></p>
""",
}
