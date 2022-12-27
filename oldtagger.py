import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from config import config

logging.basicconfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = config.API_ID
api_hash = config.API_HASH
bot_token = config.BOT_TOKEN
bot_username = config.BOT_USERNAME
support = config.SUPPORT_CHAT
owner = config.OWNER_USERNAME
bot_name = config.BOT_NAME


SUDO_USERS = config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []

ozel_list = [5508658149,5354746778,5134595693]
anlik_calisan = []
grup_sayi = []
	


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**🤖Salam...💭,\n**Mənim Adım [𝕆 𝕃 𝔻  Tag Bot](http://t.me/oldtaggerbot)-u.\n**Qurupunuz'daki  bütün üzvləri tağ etmək səlahiyyətinə sahibəm.\n\n🤖Əmrlər üçün /help yazıb məndən kömək ala bilərsiniz.**",
		   
		    buttons=(
               
		      [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/oldtaggerbot?startgroup=a')],
                      [Button.url('Söhbət Qurupu', 'https://t.me/TacikistanOdlarYurdu')],
                      [Button.url('Duyuru Kanal📢', 'https://t.me/updatechanelold')],
		      [Button.url('🎉 Sahib', 'https://t.me/AnonyumAz'),
                      Button.url(' SAHİB BLOG', 'https://t.me/teamabasofblog')],
                      [Button.url('AnonyumAz Bot','http://t.me/AnonyumAzBot')],
                      [Button.url('TikTok Bot','http://t.me/TikTokDowlandBot')],
                     ),
                    link_preview=False
                   )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "** [𝕆𝕃𝔻 TAGGER](http://t.me/oldtaggerbot)-un Kömək Əmrlər Bunlardır...💭,⤵**\n\n**🤖➪ /sehid <səbəb> - Şəhid adı ilə tag edir.**\n**🤖➪ /tag <səbəb> - 5-li Tag Atışları.**\n**🤖➪ /etag <səbəb> - Emoji ilə etiketlər.**\n**🤖➪ /stag <səbəb> - Söz'lü Tag etiketlər.**\n**🤖➪ /tektag <səbəb> - Üzvləri Tək-Tək etiketlər.**\n**🤖➪ /old <səbəb> - old Tag Bot'una aid Tag etiketlər.**\n**🤖➪ /admins <səbəb> - İdarəçilər Tək-Tək etiketlər.**\n**🤖➪ /cancel - Tag Ələməyi Dayandır.**\n**🤖➪ /start - Botu işə salır**\n**🤖➪ /rtag - Rənglə tag edir**\n**🤖➪ /utag - ürəklə tag edir**\n**🤖➪ /futag - Futbolçu adları ilə tag edir**\n**🤖➪ /mtag <səbəb> - Mafia rolları ilə tag edir**\n**🤖➪ /atag <səbəb> - Maraqlı adla tag edir**\n**🤖➪ /seher <səbəb> - Şəhər adları ilə tag edir**\n**🤖➪ /btag <səbəb> - Bayrag ilətagedir**\n**🤖➪ /fdtag <səbəb> - federasiya adları ilə tag edit**\n**🤖➪ /sahib - Botun sahiblərinin siyahısını gətirir**\n**🤖➪ /reklam - Reklam və ya əməkdaşlıq üçün bu əmrdən istifadə edin.**"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/oldtaggerBot?startgroup=a')],
                      [Button.url('Söhbət Qurupu', 'https://t.me/TacikistanOdlarYurdu')],
                      [Button.url('Duyru Kanal📢', 'https://t.me/updatechanelold')],
		      [Button.url('🎉 Sahib', 'https://t.me/AnonyumAz'),
                      Button.url(' BLOG', 'https://t.me/teamabasofblog')],
                      [Button.url('AnonyumAz Bot','http://t.me/AnonyumAzBot')],
                      [Button.url('TikTok Bot','http://t.me/TikTokDowlandBot')],
                    ),
                    link_preview=False
                   )
	
	
	
	
	
	
    
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  

# emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 

emoji = "😀 🐵 🍓 😃 🦁 🍒 😄 🐯 🍎 😁 🐱 🍉 😆 🐶 🍑 😅 🐺 🍊 😂 🐻 🥭 🤣 🐨 🍍 😭 🐼 🍌 😗 🐹 🌶 😙 🐭 🍇 😚 🐰 🥝 😘 🦊 🍐 🥰 🦝 🍏 🤩 🐮 🍈 🥳 🐷 🍋 🤗 🐽 🍄 🙃 🐗 🥕 🙂 🦓 🍠 ☺️ 🦄 🧅 😊 🐴 🌽 😏 🐸 🥦 😌 🐲 🥒 😉 🦎 🥬 🤭 🐉 🥑 😶 🦖 🥯 😐 🦕 🥖 😑 🐢 🥐 😔 🐊 🍞 😋 🐁 🌰 😛 🐀 🥔 😝 🐇 🧄 😜 🐈 🍆 🤪 🐩 🧇 🤔 🐕 🥞 🤨 🦮 🥚 🧐 🐕‍🦺 🧀 🙄 🐅 🥓 😒 🐆 🥩 😤 🐎 🍗 😠 🐖 🍖 🤬 🐄 🥙 ☹️ 🐂 🌯 🙁 🐃 🌮 😕 🐏 🍕 😟 🐑 🍟 🥺 🐐 🥨 😳 🦌 🥪 😬 🦙 🌭 🤐 🦥 🍔 🤫 🦘 🧆 😰 🐘 🥘 😨 🦏 🍝 😧 🦛 🥫 😦 🦒 🥣 😮 🐒 🥗 😯 🦍 🍲 😲 🦧 🍛 😱 🐪 🍜 🤯 🐫 🍢 😢 🐿️ 🥟 😥 🦨 🍱 😓 🦡 🍚 😞 🦔 🥡 😖 🦦 🍤 😣 🦇 🍣 😩 🐓 🦞 😫 🐔 🦪 🤤 🐣 🍘 🥱 🐤 🍡 😴 🐥 🥠 😪 🐦 🥮 🤢 🦉 🍧 🤮 🦅 🍨 🤧 🦜 🍫 🤒 🪱 🍪 😶‍🌫 🕊️ 🥜 🤠 🦢 🍭 🤑 🦩 🧈 🤤 🦃 🦚 🥵 🦆 🫑 🥶 🐧 🍥 🥸 🦈 🍦 🤓 🐳 🍳 😇 🐝 🥧 🤭 🐌 🥤 🤫 🦋 🍨".split(" ")
  
renk = "🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪ " .split(" ")

urek = "❤️ 🧡 💛 💚 💙 💜 🖤 💘 💝 ❤️   🧡 💛 💚 💙 💜 🖤 💘 💝" .split(" ")

futbol = ['Maldonado', 'Lionel Messi', 'Bobô', 'Matías Delgado', 'Márcio Nobre1', 'Rodrigo Tello', 'Federico Higuaín', 'Lamine Diatta', 'Édouard Cissé', 'Gordon Schildenfeld', 'Filip Hološko', 'Anthony Šerić', 'Tomáš Sivok', 'Tomáš Zápotočný', 'Fabian Ernst', 'Michael Fink', 'Matteo Ferrari', 'Rodrigo Tabata', 'Ricardo Quaresma', 'Roberto Hilbert', 'Guti', 'Marco Aurélio1', 'Manuel Fernandes', 'Simao Sabrosa', 'Hugo Almeida', 'Sidnei', 'Bébé', 'Júlio Alves', 'Edú', 'Julien Escudé', 'Allan McGregor', 'Dentinho', 'Mamadou Niang', 'Pedro Franco', 'Michael Eneramo', 'Atiba Hutchinson', 'Ramon Motta', 'Jermaine Jones', 'Dany Nounkeu', 'Demba Ba', 'José Sosa', 'Alexander Milošević', 'Daniel Opare', 'Duško Tošić', 'Andreas Beck', 'Luiz Rhodolfo', 'Mario Gómez', 'Denis Boyko', 'Aras Özbiliz', 'Alexis Delgado', 'Marcelo Guedes', 'Fabri', 'Adriano Correia', 'Talisca', 'Vincent Aboubakar', 'Ryan Babel', 'Matej Mitrović', 'Pepe', 'Álvaro Negredo', 'Jeremain Lens', 'Gary Medel', 'Cyle Larin', 'Vágner Love', 'Domagoj Vida', 'Enzo Roco', 'Loris Karius', 'Adem Ljajić', 'Nicolas Isimat-Mirin', 'Shinji Kagawa', 'Tyler Boyd', 'Douglas', 'Víctor Ruiz', 'Pedro Rebocho', "Georges-Kévin N'Koudou", 'Muhammed Elneni', 'Abdoulay Diaby', 'Ajdin Hasić', 'Kevin-Prince Boateng', "Fabrice N'Sakala", 'Bernard Mensah', 'Welinton', 'Francisco Montero', 'Josef de Souza', 'Valentin Rosier', 'Raşit Gezzal', 'Alex Teixeira', 'Michy Batshuayi', 'Miralem Pjanić', 'Gedson Fernandes', 'Romain Saïss', 'Mert Günok', 'Ersin Destanoğlu', 'Emre Bilgin', 'Goktug Baytekin', 'Domagoj Vida', 'Welinton', 'Douglas', 'Fabrice NSkala', 'Umut Meras', 'Francisco Montero', 'Valentin Rosier', 'Kerem Kalafat', 'Rıdvan Yılmaz', 'Serdar Saatçi', 'Serkan Emrecan Terzi', 'Aytug Batur Komec', 'Atiba Hutchinson', 'Mehmet Topal', 'Miralem Pjanic', 'Adem Ljajic', 'Alex Teixeira', 'Necip Uysal', 'Gökhan Töre', 'Rachid Ghezzal', 'Oğuzhan Özyakup', 'Georges-Kevin Nkoudou', 'Muhayer Oktay', 'Can Bozdogan', 'Berkay Vardar', 'Emirhan İlkhan', 'Emirhan Delibas', 'Demir Tiknaz', 'Jeremain Lens', 'Michy Batshuayi', 'Kenan Karaman', 'Cyle Larin', 'Güven Yalçın', 'Koray Yagci', 'Ariel Ortega', 'Robert Enke', 'Vladimir Beschastnykh', 'Ivaylo Petkov', 'Sergiy Rebrov', 'Stjepan Tomas', 'Pierre van Hooijdonk', 'Marco Aurelio', 'Fábio Luciano', 'Mert Nobre', 'Fabiano', 'Alex De Souza', 'Stephen Appiah', 'Nicolas Anelka', 'Mateja Kežman', 'Edu Dracena', 'Diego Lugano', 'Deivid', 'Roberto Carlos', 'Wederson', 'Claudio Maldonado', 'Josico', 'Daniel Güiza', 'Fábio Bilica', 'André Santos', 'Cristian Baroni', 'Miroslav Stoch', 'Issiar Dia', 'Mamadou Niang', 'Joseph Yobo', 'Emmanuel Emenike', 'Reto Ziegler', 'Henri Bienvenu', 'Moussa Sow', 'Dirk Kuyt', 'Miloš Krasić', 'Raul Meireles', 'Pierre Webó', 'Bruno Alves', 'Michal Kadlec', 'Samuel Holmén', 'Diego', 'Simon Kjær', 'Fernandão', 'Abdoulaye Ba', 'Fabiano Ribeiro', 'Nani', 'Josef de Souza', 'Robin van Persie', 'Lazar Marković', 'Aatif Chahechouhe', 'Gregory van der Wiel', 'Roman Neustädter', 'Martin Škrtel', 'Jeremain Lens', 'Oleksandr Karavayev', 'Mathieu Valbuena', 'Nebil Dirar', 'Carlos Kameni', 'Mauricio Isla', 'Elif Elmas', 'Roberto Soldado', 'Giuliano', 'Luís Neto', 'Vincent Janssen', 'André Ayew', 'Islam Slimani', 'Michael Frey', 'Diego Reyes', 'Jailson', 'Yassine Benzia', 'Victor Moses', 'Miha Zajc', 'Max Kruse', 'Allahyar Seyyadmeneş', 'Vedat Muriqi', 'Garry Rodrigues', 'Zanka', 'Adil Rami', 'Luiz Gustavo', 'Simon Falette', 'Filip Novák', 'Mame Thiam', 'José Sosa', 'Mauricio Lemos', 'Enner Valencia', 'Marcel Tisserand', 'Mbwana Samatta', 'Papiss Cissé', 'Kemal Ademi', 'Dimitris Pelkas', 'Diego Perotti', 'Attila Szalai', 'Bright Osayi-Samuel', 'Mesut Özil', 'Steven Caulker', 'Kim Min-jae', 'Diego Rossi', 'Mërgim Berisha', 'Max Meyer', 'Miguel Crespo', 'Erol Bulut', 'Saffet Akbaş', 'Tayfun Korkut', 'Elvir Bolić', 'Mustafa Doğan', 'Samuel Johnson', 'Abdullah Ercan', 'Ogün Temizkanoğlu', 'Semih Şentürk', 'Ali Güneş', 'Serhat Akın', 'Ümit Özat', 'Volkan Demirel', 'Tuncay Şanlı', 'Selçuk Şahin', 'Fabio Luciano', 'Mehmet Yozgatlı', 'Mehmet Aurelio', 'Serkan Balcı', 'Önder Turacı', 'Uğur Boral', 'Gökhan Gönül', 'Gökçek Vederson', 'Colin Kâzım Richards', 'Emre Belözoğlu', 'Mehmet Topuz', 'Bekir İrtegün', 'Caner Erkin', 'Hasan Ali Kaldırım', 'Mehmet Topal', 'Alper Potuk', 'Şener Özbayraklı', 'Ozan Tufan', 'Aykut Erçetin', 'Çağlar Birinci', 'Gökhan Zan', 'Ceyhun Gülselam', 'Aydın Yılmaz', 'Selçuk İnan', 'Johan Elmander', 'Felipe Melo', 'Dida', 'Cafu', 'Stam', 'Nesta', 'Maldini', 'Pirlo', 'Gattuso', 'Seedorf', 'Kaka', 'Shevchenko', 'Inzaghi', 'Crespo', 'Diego Altube', 'Thibaut Courtois', 'Alphonse Areola', 'Andriy Lunin', 'Lucas Canizares', 'Luis Lopez', 'Toni Fuidias', 'Diego Del Alamo', 'Luis Federico', 'Sergio Ramos', 'Raphael Varane', 'Daniel Carvajal', 'Adrian De La Fuente', 'Ferland Mendy', 'Marcelo', 'Eder Militao', 'Alvaro Odriozola', 'Victor Chust', 'Sergio Santos', 'Pablo Ramon Parra', 'Miguel Gutierrez', 'David Alaba', 'Jesus Vallejo', 'Rafa Marin', 'Mario Gila', 'Reinier', 'Marco Asensio', 'Federico Valverde', 'Brahim Diaz', 'Luka Modric', 'Toni Kroos', 'Isco', 'Carlos Casemiro', 'Lucas Vazquez', 'Martin Odegaard', 'Marvin Park', 'Sergio Arribas', 'Antonio Blanco', 'Hugo Duro', 'Eduardo Camavinga', 'Dani Ceballos', 'Peter Gonzalez', 'Karim Benzema', 'Luka Jovic', 'Eden Hazard', 'Gareth Bale', 'Vinicius Junior', 'Rodrygo', 'James Rodriguez', 'Mariano Diaz', 'Borja Mayoral', 'Oscar Aranda', 'Juan Latasa', 'Neto', 'Marc-Andre Ter Stegen', 'Inaki Pena', 'Arnau Tenas', 'Lazar Carevic', 'Jordi Alba', 'Sergi Roberto', 'Ronald Araujo', 'Samuel Umtiti', 'Nelson Semedo', 'Clement Lenglet', 'Dani Morer', 'Junior Firpo', 'Gerard Pique', 'Sergio Akieme', 'Santiago Ramos', 'Arnau Comas', 'Sergino Dest', 'Oscar Mingueza', 'Eric Garcia', 'Emerson', 'Alejandro Balde', 'Dani Alves', 'Mika Marmol', 'Sergio Busquets', 'Hiroki Abe', 'Alex Collado', 'Frenkie De Jong', 'Ivan Rakitic', 'Arturo Vidal', 'Riqui Puig', 'Guillem Jaime', 'Miralem Pjanic', 'Philippe Coutinho', 'Carles Alena', 'Konrad De La Fuente', 'Ilaix Moriba', 'Matheus Fernandes', 'Yusuf Demir', 'Nico Gonzalez', 'Abde Ezzalzouli', 'Alvaro Sanz', 'Ferran Jutgla', 'Matheus Pereira', 'Lucas De Vega', 'Estanis Pedrola', 'Adama Traore', 'Luis Suarez', 'Ousmane Dembele', 'Antoine Griezmann', 'Ansu Fati', 'Lionel Messi', 'Rey Manaj', 'Martin Braithwaite', 'Memphis Depay', 'Sergio Agüero', 'Luuk De Jong', 'Ilias Akhomach', 'Ferran Torres', 'Pierre Aubameyang', 'Albert Riera', 'Milan Baroš', 'Tomáš Ujfaluši', 'Mehmet Batdal', 'Serkan Kurtuluş', 'Yiğit Gökoğlan', 'Hakan Balta', 'Fernando Muslera', 'Semih Kaya', 'Emmanuel Eboué', 'Yekta Kurtuluş', 'Engin Baytar', 'Emre Çolak', 'Sabri Sarıoğlu', 'Servet Çetin', 'Necati Ateş', 'Ufuk Ceylan', 'Sercan Yıldırım', 'Fernando Muslera', 'Felipe Melo', 'Hamit Altıntop', 'Gökhan Zan', 'Blerim Džemaili', 'Aydın Yılmaz', 'Selçuk İnan', 'Umut Bulut', 'Wesley Sneijder', 'Bruma', 'Alex Telles', 'Burak Yılmaz', 'Sinan Gümüş', 'Goran Pandev', 'Aurélien Chedjou', 'Fernando Muslera', 'Mariano', 'Maicon', 'Serdar Aziz', 'Ahmet Çalık', 'Tolga Ciğerci', 'Yasin Öztekin', 'Selçuk İnan', 'Eren Derdiyok', 'Younès Belhanda', 'Sinan Gümüş', 'Martin Linnes', 'Ryan Donk', 'Cédric Carrasso', 'Şener Özbayraklı', 'Omar Elabdellaoui', 'Taylan Antalyalı', 'Henry Onyekuru', 'Ryan Babel', 'Radamel Falcao', 'Halil Dervişoğlu', 'Oghenekaro Etebo', 'Martin Linnes', 'Ryan Donk', 'Oğulcan Çağlayan', 'Kerem Aktürkoğlu', 'Ömer Bayram', 'Emre Akbaba', 'Cristiano Ronaldo', 'Pele', 'Maradona', 'Ronaldo', 'Thierry Henry', 'Kaka', 'Sergio Agüero', 'Xavi', 'Ruud Gullit', 'Arthur Zico', 'Lev Yashin', 'Iniesta', 'Lothar Matthäus', 'Giuseppe Meazza', 'Franz Beckenbauer', 'George Best', 'Roberto Baggio', 'Johan Cruyff', 'Luis Figo', 'Andrea Pirlo', 'Marco Van Basten', 'Zlatan Ibrahimovic', 'Sandro Mazzola', 'Ferenc Puskas', 'Zinedine Zidane', 'Alfredo Di Stéfano', 'Rio Ferdinand', 'Paolo Maldini', 'Robin van Persie', 'Iker Casillas', 'Neymar', 'Fabio Cannavaro', 'Yaya Toure', 'Edinson Cavani', 'Gabriel Batistuta', 'Thiago Silva', 'Dennis Bergkamp', 'Franck Ribery', 'Carles Puyol', 'Mesut Özil', 'Dani Alves', 'David Silva', 'Karim Benzema', 'Javier Zanetti', 'Radamel Falcao', 'Bastian Schweinsteiger', 'Gianluigi Buffon', 'Arjen Robben', 'Wayne Rooney', 'Luis Suarez', 'Mbappe', 'Juan Román Riquelme', 'Sergio Ramos', 'Muhammed Salah', 'Cesc Fabregas', 'Gerard Pique', 'Pepe', 'Didier Drogba', 'Robert Lewandowski', 'David Villa', 'Wesley Sneijder', 'Philipp Lahm', "Samuel Eto'o", 'Carlos Tevez', 'Sergio Busquets', 'Samir Nasri', 'Eden Hazard', 'Diego Forlan', 'Klaas Jan Huntelaar', 'Sabri Sarıoğlu']

sehidler = "Abdullayev Qəzənfər","Polad Həşimov","Anar Kazımov","Ramazanov Vüsal","Ümüd Heydərov","Fərid Teymurov","Əlövsət Məmmədov","Riyad Əliyarov","Şöhrət Namazov","Gümrah Səfərquliyev","Nəcəf Abdullayev Nurlan","İnqilab Abdullayev","Nicat Mirnəbi","Abdullayev Məhəmməd","Ramazan Allahverənov","Telman Fazil","Alıyev Qələndər","Nofəl Abdullayev","İbrahim Habil","Abdullayev Elşən","Sabir Abdullayev","Həsən Qərib".split(" ")


bayrag = "🇦🇨 🇦🇩 🇦🇪 🇦🇫 🇦🇬 🇦🇮 🇦🇱 🇦🇴 🇦🇶 🇦🇷 🇦🇸 🇦🇹🇦🇺 🇦🇼 🇦🇽 🇦🇿 🇧🇦 🇧🇧 🇧🇩 🇧🇪 🇧🇫 🇧🇬 🇧🇭 🇧🇮🇧🇯 🇧🇱 🇧🇲 🇧🇳 🇧🇴 🇧🇶 🇧🇷 🇧🇸 🇧🇹 🇧🇻 🇧🇼 🇧🇾🇧🇿 🇨🇦 🇨🇨 🇨🇩 🇨🇫 🇨🇬 🇨🇭 🇨🇮 🇨🇰 🇨🇱 🇨🇲 🇨🇳🇨🇵 🇨🇷 🇨🇺 🇨🇻 🇨🇼 🇨🇽 🇨🇾 🇨🇿 🇩🇪 🇩🇬 🇩🇯 🇩🇰🇩🇲 🇩🇴 🇩🇿 🇪🇦 🇪🇨 🇪🇪 🇪🇬 🇪🇭 🇪🇷 🇪🇸 🇪🇹 🇪🇺🇫🇮 🇫🇯 🇫🇰 🇫🇲 🇫🇴 🇫🇷 🇬🇦 🇬🇧 🇬🇩 🇬🇪 🇬🇫 🇬🇬🇬🇭 🇬🇮 🇬🇱 🇬🇲 🇬🇳 🇬🇵 🇬🇶 🇬🇷 🇬🇸 🇬🇹 🇬🇺 🇬🇼🇬🇾 🇭🇰 🇭🇲 🇭🇳 🇭🇷 🇭🇹 🇭🇺 🇮🇨 🇮🇩 🇮🇪 🇮🇱 🇮🇲🇮🇳 🇮🇴 🇮🇶 🇮🇷 🇮🇸 🇮🇹 🇯🇪 🇯🇲 🇯🇴 🇯🇵 🇰🇪 🇰🇬🇰🇭 🇰🇮 🇰🇲 🇰🇳 🇰🇵 🇰🇷 🇰🇼 🇰🇾 🇰🇿 🇱🇦 🇱🇧 🇱🇨🇱🇮 🇱🇰 🇱🇷 🇱🇸 🇱🇹 🇱🇺 🇱🇻 🇱🇾 🇲🇦 🇲🇨 🇲🇩 🇲🇪🇲🇫 🇲🇬 🇲🇭 🇲🇰 🇲🇱 🇲🇲 🇲🇳 🇲🇴 🇲🇵 🇲🇶 🇲🇷 🇲🇸🇲🇹 🇲🇺 🇲🇻 🇲🇼 🇲🇽 🇲🇾 🇲🇿 🇳🇦 🇳🇨 🇳🇪 🇳🇫 🇳🇬🇳🇮 🇳🇱 🇳🇴 🇳🇵 🇳🇷 🇳🇺 🇳🇿 🇴🇲 🇵🇦 🇵🇪 🇵🇫 🇵🇬🇵🇭 🇵🇰 🇵🇱 🇵🇲 🇵🇳 🇵🇷 🇵🇸 🇵🇹 🇵🇼 🇵🇾 🇶🇦 🇷🇪🇷🇴 🇷🇸 🇷🇺 🇷🇼 🇸🇦 🇸🇧 🇸🇨 🇸🇩 🇸🇪 🇸🇬 🇸🇭 🇸🇮🇸🇯 🇸🇰 🇸🇱 🇸🇲 🇸🇳 🇸🇴 🇸🇷 🇸🇸 🇸🇹 🇸🇻 🇸🇽 🇸🇾🇸🇿 🇹🇦 🇹🇨 🇹🇩 🇹🇫 🇹🇬 🇹🇭 🇹🇯 🇹🇰 🇹🇱 🇹🇲 🇹🇳🇹🇴 🇹🇷 🇹🇹 🇹🇻 🇹🇼 🇹🇿 🇺🇦 🇺🇬 🇺🇲 🇺🇳 🇺🇸 🇺🇾🇺🇿 🇻🇦 🇻🇨 🇻🇪 🇻🇬 🇻🇮 🇻🇳 🇻🇺 🇼🇫 🇼🇸 🇽🇰 🇾🇪🇾🇹 🇿🇦 🇿🇲 🇿🇼 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🏴󠁧󠁢󠁳󠁣󠁴󠁿 🏴󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")

seherler = "Ağcabədi Ağdam Ağdaş Ağdərə Ağıstafa Ağsu Astara Babək Bakı Balakən Beyləqan Bərdə Biləsuvar Cəbrayıl Cəlilabad Culfa Daşkəsən Dəliməmmədli Xocalı Füzuli Gədəbəy Gəncə Goranboy Göyçay Göygöl Göytəpə Hacıqabul Horadiz Xaçmaz Xankəndi Xocalı Xocavənd Xırdalan Xızı Xudat İmişli İsmayıllı Kəlbəcər Kürdəmir Qax Qazax Qəbələ Qobustan Qovlar Quba Qubadlı Qusar Laçın Lerik Lənkəran Liman Masallı Naftalan Naxçıvan Neftçala Oğuz Ordubad Saatlı Sabirabad Salyan Samux Siyəzən Sumqayıt Şuşa Şabran Şahbuz Şamaxı Şəki Şəmkir Şərur Şirvan Tərtər Tovuz Ucar Yardımlı Yevlax Zaqatala Zəngilan Zərdab󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")

mafia = "👨‍🌾Vətəndaş 👨‍✈️Komissar Kattani 👨‍💼Çavuş 👨‍⚕️Doktor 🧟‍♀️Cadugar 🕵️Suiqəstçi 🧔Bomj 🦎Buqələmun 💂🏻Securıty 👳🏻‍♂️Satıcı 🙇🏻‍♂️Oğru 👷🏻‍♂️Mədənçi ⭐️General 🧝🏻‍♀️Şəhzadə 🎧DJ 🏦Bankir 🕴Don 🕺Mafia 👨‍⚖️Vəkil 🙍🏻‍♂️Məhbus 👨🏻‍🦱Dedektiv 🦦Köstəbək 👨🏻‍🎤Specialist 🔪Manyak 🤡Joker 👻Ruh 🧚🏻‍♀️Mələk 🦹🏻‍♂️BOSS 🥷Ninja 🥷SUPER Ninja 👨🏻‍🦲Dəli 🔮Reviver 💂Killer 🧛🏻‍♂️Vampir󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")

ad = ( "🐰 Dovşan","🦁 Şir","💍 Evli","🐶 İT","🐻 Ayı","🐭 Siçan","🥰 Sevimli","😜 Subay","😎Sevgili","👨‍👩‍👦‍👦 Ailə","🤑 Varlı","🕵‍♂ Vəkil","🐒 Meymun","🐣 Cücə","🦊 Tülkü","👩‍⚕ Həkim","👨‍🏫 Müəllim","👨‍🍳 Aşbaz","👩‍🏫 Müəllimə","🧚‍♀ Mələk","😊 Dəyərli","Gözəl💄","Çirkin😒","Unutqan 🤕","🦠 Karona","🤭 Dəcəl","😡 Lovğa","🙈Utancaq","😎 Səbirli","🧑‍🔬 Ağıllı")

fedler = "LC","DTÖ","GOLD","XAOS","KARONA","FC","ASO","STFU","KARABAKH","TTK","GGT","TAO","DEV","FM","DAB","BQB","ATOM","ELİT","BTO","CRAZY","BTB","ALPHA","FELLİX","QANUN","RCI","SO","XTQ","BT","DTB","KİNG","HOST","AMON","DTX","TAD","KOBRA".split(" ")

salam = (
"Salam",
"Salam Kişi",
"Salam Balam",
"Salamdaa",
"Uşş balama salam",
"Salam Cənab 🫶",
"Salam Lələ 🔥",
)



@client.on(events.NewMessage(pattern="^/fdtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmir qruplar üçün etibarlıdı**")
    
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmirdən yalnız idarəçilər isdifadə edə bilər!**")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
       return await event.respond("**Əvvəlki mesajlara cavab verə bilərəm!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
   
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants (event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(fedler)}](tg://user?id={user.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choic(fedler)}](tg://user?id={user_id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def mentionall(event):
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id)
  
  
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmir qruplar üçün etibarlıdı**")
    
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmirdən yalnız idarəçilər isdifadə edə bilər!**")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
       return await event.respond("**Əvvəlki mesajlara cavab verə bilərəm!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
   
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants (event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(ad)}](tg://user?id={user.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choic(ad)}](tg://user?id={user_id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def mentionall(event):
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmir qruplar üçün etibarlıdı**")
    
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmirdən yalnız idarəçilər isdifadə edə bilər!**")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
       return await event.respond("**Əvvəlki mesajlara cavab verə bilərəm!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
   
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants (event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(mafia)}](tg://user?id={user.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choic(mafia)}](tg://user?id={user_id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def mentionall(event):
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/seher ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmir qruplar üçün etibarlıdı**")
    
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmirdən yalnız idarəçilər isdifadə edə bilər!**")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
       return await event.respond("**Əvvəlki mesajlara cavab verə bilərəm!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
   
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants (event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(seherler)}](tg://user?id={user.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choic(seherler)}](tg://user?id={user_id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def mentionall(event):
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmir qruplar üçün etibarlıdı**")
    
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmirdən yalnız idarəçilər isdifadə edə bilər!**")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
       return await event.respond("**Əvvəlki mesajlara cavab verə bilərəm!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
   
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants (event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={user.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
    
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choic(bayrag)}](tg://user?id={user_id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def mentionall(event):
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id)
        
        
@client.on(events.NewMessage(pattern="^/sehid ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmir qruplar üçün etibarlıdı**")
    
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmirdən yalnız idarəçilər isdifadə edə bilər!**")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
       return await event.respond("**Əvvəlki mesajlara cavab verə bilərəm!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
   
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants (event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(sehidler)}](tg://user?id={user.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choic(sehidler)}](tg://user?id={user_id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def mentionall(event):
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id)
        
        

@client.on(events.NewMessage(pattern="^/futag ?(.*)"))
async def mentionall(event):
  global anlik_calisan 
  if event.is_private:
    return await event.respond("**Bu əmir qruplar üçün etibarlıdı!**")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmirdən yalnız idarəçilər isdifadə edə bilər!**")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
       return await event.respond("**Əvvəlki mesajlara cavab verə bilərəm!**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants (event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(futbol)}](tg://user?id={user.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
	
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choic(futbol)}](tg://user?id={user_id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
	
	
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def mentionall(event):
  global anlik_calisan 
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdı!**")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmirdən yalnız idarəçilər isdifadə edə bilər!**")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki mesajlara cavab verə bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for user in client.iter_participants(event.chat.id):
      usrnum += 1
      usrtxt += f"[{random.choice(urek)}](tg://user?id={user.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond(f"**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(urek)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond(f"**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def mentionall(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdı!**")
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmirdən yalnız idarəçilər isdifadə edə bilər!**")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
   return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
   return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(renk)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
	
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(renk)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
	
	
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	
	
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Tag'a başlamaq üçün səbəb yazın...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond(f"**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"✰ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"✰ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**✰ - [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"✰ - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

stag = (
"Bəzi insanlar yağışı hiss edər, digərləri isə sadəcə islanar",
"Unutma; Hər gələn sevməz.. Və heç bir sevgili getməz",
"Heç bir ruhun ağrısı sənin dərdindən az deyil",
"Mən hər şeyi sınayıram; amma bacardığımı edirəm.",
"Sevgi bir qadının həyatının bütün hekayəsidir və bir kişinin yeganə macərasıdır.",
"Xoşbəxtlik ilk növbədə bədən sağlamlığındadır.",
"Nə qədər yaşadığımız deyil, necə yaşadığımızdır",
"Yer göy qurşağı, ağıl prizma, varlıq isə ağ şüadır.",
"Hara getdiyinizi bilmirsinizsə, hansı tərəfə getdiyinizin əhəmiyyəti yoxdur.",
"Həyatın ən qiymətli vaxtıdır. Kimə hədiyyə etdiyinizə diqqət edin.",
"Evin bütün pəncərələrini sındırıb, sonra qapını döyə bilməzsən.",
"Xoşbəxtlik yaşadığın həyat tərzində deyil, həyata baxış tərzindədir.",
"Unutma; Hər gələn sevməz.. Və heç bir sevgili getməz.",
"Bu həyatda yarım nəfəs. Sevgidən başqa heç nə planlaşdırma...",
"Hər kəsə içindəki yaxşılar qədər yaxşı bir həyat arzulayıram.",
"Gözəlliyi gözəl edən ədəbdir, ədəb isə gözəlliyi sevmək üçün səbəbdir!",
"Qızılgülün ətri qızılgül verənin əlində qalır",
"Axtardığın şey səni axtarandır.",
"Hətta bir quş da göydə qanad çırpar.",
"Könül almağı bilməyənlərə həyat əmanət deyil.",
"Dürüst olmaqdan qorxma, ən çox itirəcəyiniz yanlış insanlar olacaq.",
"İnsan ağac deyil, qırılanda səs çıxararsan.",
"Öyrənmək həyatın yeganə sübutudur.",
"Dünya əhalisi artdıqca insanların sayı azalır.",
"Layiq olmadığını düşündüyünüz insanlara əsla həqiqəti deməyin.",
"Çox şükür ki, göy hələ heç bir pul kisəsinə sığmır.",
"Özün ol. Artıq hamı götürüb.",
"Zərər çəkdim, boğazımdakı düyünləri uddum.",
"O qədər gözəl gülümsəyirdi ki, sevməsəydim boşuna olardı.",
"Onun sevdiyi men deyilem. Bunun ağrısını sizə deyə bilmərəm.",
"Onun sevdiyi men deyilem. Bunun ağrısını sizə deyə bilmərəm.",
"Zamanla hər şeyə alışırsan, amma bitmir.",
"Əgər həqiqəti deyirsənsə, heç nəyi xatırlamağa ehtiyac yoxdur.",
"Həqiqəti ilk söyləyən siz olun... Əks halda kimsə sizin yerinizə mütləq həqiqəti söyləyəcək.",
"Kişilər daha güclü ola bilər, amma qadınlar dözümlüdürlər.",
"Ağrı üçün heç bir resept yoxdur",
"Ardınca getməyə cəsarətiniz varsa, bütün arzular gerçəkləşə bilər.",
"Bu gizli sevgidir, heç kimə dərdlərimi deyə bilmərəm.",
"Sizcə sevgi hər şeyi bağışlayır?",
"Mənə də, sənə də siqaret lazımdır",
"Mən səndən xüsusi birini tanımırdım",
"Bir gün sevgi bitər, xatirələr qalır",
"Sevmək nə qədər uzun bir sözdür!",
"Hatırladığım en unutulası şeysin.",
"Birlikdə gülmək üçün darıxdığım insanlar var.",
"Xoşbəxtliyi səndə tapan sənindir, üstəlik qonaq.",
"Çox sev, amma bəyənmirsənsə məcbur etmə!",
"O  qədər  gözəl gülürdü ki, sevməsəm ziyan olacaqdı.",
"və  insan insana yoldaş olmalı yaralarını sağalatmalı",
"Məzarlıq, əsəb  uğruna peşman olanlarla dolu",
"Eşq külək  kimidir görməzsən ama hiss edə bilərsən.",
"tərəzi  var ölçü var , hərşeyin bir vaxtı var",

"Yanıltmasın səni masum baxışlar, bəzılarını şeytan ayaqdə alqışlar...",
"həyat sabahı gözləyəcək qədər uzun deyil",
"Yaxşılar əsla itirməz , itirilir.",
"görməzden gəldiyin sevgiyə möhtac qalman diləyiylə",
"Kaşki ağıl vermək yerinə hüzur versəniz",
"Heç bilmədiyim o qoxunu çox özləyirəm",
    #Mfmf
"𝑌𝑎𝑥𝑠̧𝚤 𝑜𝑙𝑎𝑛 𝑖𝑡𝑖𝑟𝑠𝑒𝑑𝑒 𝑞𝑎𝑧𝑎𝑛ı𝑟",
"𝐴ş𝑖𝑞 𝑜𝑙𝑚𝑎𝑞 𝑔𝑜̈𝑧ə𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑ə𝑐ə 𝑠ənə",
"𝐻𝑒𝑐̧𝑘𝑖𝑚 ℎ𝑒𝑐̧𝑘𝑖𝑚𝑖 𝑖𝑡𝑖𝑟𝑚𝑒𝑧  𝑔𝑖𝑑ə𝑛 𝑏𝑎ş𝑞𝑎𝑠ı𝑛ı 𝑡𝑎𝑝𝑎𝑟, 𝑞𝑎𝑙𝑎𝑛 𝑜̈𝑧𝑢̈𝑛𝑢̈",
"Ç𝑜𝑥 ö𝑛ə𝑚𝑠ə𝑑𝑖𝑘 𝑖şə 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡𝚤𝑞 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑟𝑖𝑘",
"Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑑𝑢𝑞𝑙𝑎𝑟𝚤𝑛𝚤𝑧𝚤  𝑒𝑠̧𝑖𝑑𝑒𝑛 𝑏𝑖𝑟𝑖𝑦𝑙ə 𝑘𝑒ç𝑖𝑟𝑖𝑛",
"𝐺ö𝑛𝑙ü𝑛ü𝑧ə  𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑔̆ı 𝑏𝑖𝑙𝑠𝑖𝑛",
"𝑆ə𝑛 ç𝑜𝑥 𝑠𝑒𝑣 𝑑𝑒 𝑏𝑢𝑟𝑎𝑥ı𝑏  𝑔𝑖𝑑ə𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
"𝑌𝑎𝑥𝑠̧𝚤 𝑜𝑙𝑎𝑛 𝑖𝑡𝑖𝑟𝑠ə𝑑ə 𝑞𝑎𝑧𝑎𝑛ı𝑟",
"𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏𝑢𝑟𝑎𝑥𝚤𝑟𝑎𝑚  𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦",
"𝑁ə 𝑖ç𝑖𝑚𝑑ə𝑘𝑖 𝑘𝑢̈𝑐̧ə𝑙ə𝑟ə 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁ə 𝑑ə 𝑐̧𝑜̈𝑙𝑑ə𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎",                  
"𝐴𝑟𝑡ı𝑞 ℎ𝑒ç𝑏𝑖𝑟 ş𝑒𝑦 ə𝑣𝑣ə𝑙𝑘𝑖 𝑘𝑖𝑚𝑖 𝑑𝑒𝑦𝑖𝑙 𝐵𝑢𝑛𝑎 𝑚ə𝑛𝑑ə 𝑑𝑎𝑥𝑖𝑙ə𝑚",                
"𝐴ş𝑖𝑞 𝑜𝑙𝑚𝑎𝑞 𝑔𝑜̈𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑ə𝑐ə 𝑠ə𝑛ə",                 
"İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖çə𝑘 𝑎ç𝑎𝑟",
"𝑌𝑎𝑥𝑠̧𝚤𝑦𝑎𝑚 𝑑𝑒𝑠ə𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑞, 𝑜 𝑘ə𝑑ə𝑟 𝑥ə𝑏ə𝑟𝑠𝑖𝑧 𝑚ə𝑛𝑑ə𝑛", 
"𝐸𝑙ə 𝑔𝑜̈𝑧ə𝑙 𝑏𝑎𝑥𝑡ı 𝑘𝑖 𝑞ə𝑙𝑏𝑖 𝑑ə 𝑔ü𝑙üşü 𝑞ə𝑑ə𝑟 𝑔𝑜̈𝑧ə𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚",
"𝑀ə𝑠𝑎𝑓ə𝑙ə𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒𝑦𝑖𝑙, İç𝑖𝑚𝑑ə 𝐸𝑛 𝐺ü𝑧ə𝑙 𝑌𝑒𝑟𝑑ə𝑠ə𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏ə𝑧ə𝑛 𝑏𝑜̈𝑦ü𝑘 𝑥ə𝑦𝑎𝑙𝑙𝑎𝑟𝚤𝑛𝚤 𝑘𝑖ç𝑖𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑ə𝑟",
"𝐻𝑒𝑐̧𝑘𝑖𝑚 ℎ𝑒𝑐̧𝑘𝑖𝑚𝑖 𝑖𝑡𝑖𝑟𝑚ə𝑧 𝑔𝑒𝑑ə𝑛 𝑏𝑎ş𝑞𝑎𝑠ı𝑛ı 𝑡𝑎𝑝𝑎𝑟  𝑞𝑎𝑙𝑎𝑛 𝑜̈𝑧𝑢̈𝑛𝑢̈",
"Ç𝑜𝑥 ö𝑛ə𝑚𝑠ə𝑑𝑖𝑘 𝑖şə 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑞 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑟𝑖𝑘",              
"𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑞𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛",
"𝐻ə𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙ə𝑛 𝑑𝑒𝑦𝑖𝑙 𝑞ı𝑦𝑚ə𝑡 𝑏𝑖𝑙ə𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎə𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎",
"𝑉𝑒𝑟𝑖𝑙ə𝑛 𝑑ə𝑦ə𝑟𝑖𝑛 𝑛𝑎𝑛𝑘𝑜𝑟𝑢 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎə𝑙𝑙𝑜𝑙𝑢𝑟",
"𝑀ə𝑠𝑎𝑓ə 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁ə ℎə𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛ə 𝑑ə 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑥𝑎𝑛",                
"𝐻ə𝑦𝑎𝑡 𝑖rəl𝑖𝑦ə 𝑏𝑎𝑥ı𝑙𝑎𝑟𝑎𝑞 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦ə  𝑏𝑎𝑥𝑎𝑟𝑎𝑞 𝑎𝑛𝑙𝑎şı𝑙ı𝑟",
"𝑆ə𝑛 ç𝑜𝑥 𝑠𝑒𝑣 ,  𝑔𝑒𝑑ə𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",
"𝐵𝑖𝑟 𝑀𝑜̈𝑐𝑢̈𝑧ə𝑦ə 𝐸ℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟 𝑖𝑑𝑖 𝐻ə𝑦𝑎𝑡 𝑆ə𝑛𝑖 𝑄𝑎𝑟şı𝑚𝑎 Çı𝑥𝑎𝑟𝑑ı",
"İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣ə 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖çə𝑘 𝑎ç𝑎𝑟",
"𝑢̈𝑟ə𝑦𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏𝑜̈𝑦ü𝑘 𝑏𝑖𝑟                    𝑦𝑜𝑟𝑔̆𝑢𝑛𝑙𝑢𝑞 𝑣𝑎𝑟",
"𝑄ə𝑙𝑏𝑖 𝑔𝑜̈𝑧ə𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑ə𝑛 𝑦𝑎ş ə𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış",
"𝐻ə𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑑𝑖𝑦𝑖 𝑦𝑒𝑟𝑑ə 𝑚ə𝑛𝑑ə 𝑏𝑖𝑡𝑑𝑖𝑚 𝑑ə𝑦𝑖ş𝑑𝑖𝑛 𝑑𝑒𝑦ə𝑛𝑙ə𝑟𝑖𝑛 ə𝑠ə𝑟𝑖𝑦ə𝑚",
"𝐺ü𝑣ə𝑛𝑚ə𝑘 𝑠𝑒𝑣𝑚ə𝑘𝑑ə𝑛 𝑑𝑎ℎ𝑎 𝑑ə𝑦ə𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛",
"İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠ə𝑏𝑟𝑙ə  𝑔𝑜̈𝑧𝑙ə𝑑𝑖𝑦𝑖𝑛 ℎ𝑒𝑟 ş𝑒𝑦 𝑢̈𝑐̧𝑢̈𝑛 𝑥𝑒𝑦𝑖𝑟𝑙𝑖 𝑏𝑖𝑟 𝑥ə𝑏ə𝑟 𝑎𝑙ı𝑟𝑠ı𝑛",
"İ𝑛𝑠𝑎𝑛 𝑏ə𝑧ə𝑛 𝑏𝑜̈𝑦𝑢̈𝑘 𝑥ə𝑦𝑎𝑙𝑙𝑎𝑟𝚤𝑛𝚤 𝑘𝑖𝑐̧𝑖𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑ə𝑟 ",
"Ö𝑙𝑚ə𝑘 𝐵𝑖𝑟 ş𝑒𝑦 𝑑𝑒y𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑞 𝑞𝑜𝑟𝑥𝑢𝑛𝑐",
"𝐻ə𝑟𝑘ə𝑠𝑖𝑛 𝑏𝑖𝑟 𝑘𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑ə 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖",
"𝐺ü𝑐𝑙ü 𝑔ö𝑟ü𝑛ə 𝑏𝑖𝑙ə𝑟ə𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛           𝑦𝑜𝑟𝑔̆𝑢𝑛𝑎𝑚",
"𝐻ə𝑦𝑎𝑡 𝑛ə 𝑔𝑒𝑑ə𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔ə𝑡𝑖𝑟𝑖𝑟 𝑛ə𝑑ə 𝑖𝑡𝑖𝑟𝑑𝑖𝑦𝑖𝑛𝑖𝑧 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔ə𝑡𝑖𝑟𝑖𝑟",                   
"𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢."
)	

@client.on(events.NewMessage(pattern="^/stag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
    
			    			     
@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "♕︎Adminlər Siyahısı♕︎"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n ➮ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#@client.on(events.NewMessage(pattern="^/admins|/admin|@admin|@admins ?(.*)"))
#async def _(event):
 #   chat_id = event.chat_id
  #  if event.is_private:
   #     return await event.respond("sᴏʀʀʏ ʏᴏᴜ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀᴅᴍɪɴ ᴏɴʟʏ ɪɴ ɢʀᴏᴜᴘ")

    #is_admin = False
    #try:
     #   partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    #except UserNotParticipantError:
     #   is_admin = False
    #else:
     #   if isinstance(
      #      partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
       # ):
    #        is_admin = True
   # if not is_admin:
     #   return await event.respond("ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs")

   # if event.pattern_match.group(1) and event.is_reply:
    #    return await event.respond("ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ")
    #elif event.pattern_match.group(1):
     #   mode = "text_on_cmd"
      #  msg = event.pattern_match.group(1) 
    #elif event.is_reply:
     #   mode = "text_on_reply"
      #  msg = await event.get_reply_message()
       # if msg == None:
 #           return await event.respond(
  #              "__ɪ ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ꜰᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (ᴍᴇssᴀɢᴇs ᴡʜɪᴄʜ ᴀʀᴇ sᴇɴᴛ ʙᴇꜰᴏʀᴇ ɪ'ᴍ ᴀᴅᴅᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ)__"
   #         )
    #else:
     #   return await event.respond(
      #      "__ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs!__"
       # )

    #spam_chats.append(chat_id)
    #usrnum = 0
    #usrtxt = ""
    #chat = await event.get_input_chat()
    #async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
     #   if not chat_id in spam_chats:
      #      break
       # usrnum += 1
        #usrtxt += f" \n [{x.first_name}](tg://user?id={x.id})"
        #if usrnum == 5:
         #   if mode == "text_on_cmd":
          #      txt = f"{usrtxt}\n\n{msg}"
           #     await client.send_message(chat_id, txt)
         #   elif mode == "text_on_reply":
        #        await msg.reply(usrtxt)
       #      usrnum = 0
     #       usrtxt = ""
    #try:
     #   spam_chats.remove(chat_id)
    #except:
        #pass

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#





















#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
#async def mentionall(tagadmin):

 #if tagadmin.pattern_match.group(1):
 # seasons = tagadmin.pattern_match.group(1)
 #else:
 # seasons = ""

 #chat = await tagadmin.get_input_chat()
 #a_=0
 #await tagadmin.delete()
# async for i in client.iter_participants(chat, filter=cp):
#  if a_ == 500:
  # break
#  a_+=5
 # await tagadmin.client.send_message(tagadmin.chat_id, "{} {}".format(i.first_name, i.id, seasons))
 # sleep(0.5)


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

	
@client.on(events.NewMessage(pattern="^/old ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu əmr qruplar üçün etibarlıdır! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu əmrdən yalnız idarəçilər istifadə edə bilər! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Əvvəlki Mesajlara Cavab verə Bilərəm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur! **")
  else:
    return await event.respond("**Başlamaq üçün heç bir səbəb yoxdur,yazın...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(old)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(old)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı**")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

old = ('Buda kimmiş də miş miş👀😁😍','🙄👉🤲Aağil','🙄 Sən dediyim sözü elədin? 😐','Həyatımın dolması 🥲 nassın😍','Mənə niyə elə baxırsan? 🌝','İkinci planda olmaqdansa, plana daxil olmamağı seçərəm.  🎯','səni basqa qrublardada görmüsdüm ','Ac olanda sən o sən deyilsən','Niyə yalan danışırsan adamın üstündə patalok var','Həci necəsən ficuuu ','köhnə məkanın yeni sakini ','günün günnən durdun uzax de görüm haramı bəyənmədin','deyrlər ölübsən🤔','Güçlüyüm... Çünkü başka seçeneğim yok düşersem tutanım olmayacak biliyorum...🚬','gəl bir birimizi arka sokaklar bitənə qədər sevək❤️','corona belə böyüdü sən böyümədin','corona belə unduldu səni unuda bilmədim🚬','səni sevirəm sözündə neçə dənə samit var','oğlanlar niyə az yaşayır','bitkilər yaşlandıqcamı ölər yoxsa baxımsızlıqdanmı','isti havada çay içirsən hələdə','allah rəhmət eləsin','tez gəlin hədiyyəli yarışımız basladı','Benim hayelerim kelebeğin ömrü kadar yaşar 💔🥀','Çiçəklərə aşağıdan baxmağa gedirəm..➰','susмuş вir qadın üçün... вiтмiş вir adaмsan.! 🖤','𝚂ə𝚏𝚕ə𝚛𝚒𝚗𝚒 𝚞̈𝚣𝚕ə𝚛𝚒𝚗ə 𝚟𝚞𝚛𝚖𝚊𝚍𝚒𝚐̆𝚒𝚖𝚒𝚣 𝚞̈𝚌̧𝚞̈𝚗 𝚘̈𝚣𝚕𝚎𝚛𝚒𝚗𝚒 𝚚𝚞̈𝚜𝚞𝚛𝚜𝚞𝚣 𝚜𝚊𝚗𝚊𝚗 𝚒𝚗𝚜𝚊𝚗𝚕𝚊𝚛 𝚟𝚊𝚛😒','Güclü olmağa məndən daha çox ehtiyacın var, çünki haqsız olduğunu ürəyinin bir yerində bilirsən.🤙','Makiyaj və üz boyalarınıza güvənməyin. Yollar da gözəldir, lakin altından kanalizasiya keçir.👋😉','𝙸̇𝚝𝚒𝚛𝚍𝚒𝚢𝚒𝚗 𝚟𝚊𝚡𝚝𝚒 𝚚𝚊𝚢𝚝𝚊𝚛𝚊 𝚋𝚒𝚕𝚖ə𝚍𝚒𝚢𝚒𝚗 𝚔𝚒𝚖𝚒 𝚎𝚕ə𝚍𝚒𝚢𝚒𝚗 𝚙𝚒𝚜𝚕𝚒𝚢𝚒 𝚍ə 𝚑𝚎𝚌̧ 𝚟𝚊𝚡𝚝 𝚍𝚞̈𝚣ə𝚕𝚍ə 𝚋𝚒𝚕𝚖𝚎𝚢ə𝚌𝚎𝚔𝚜ən😐','𝙱𝚒𝚛𝚊𝚣 𝚒𝚗𝚜𝚊𝚗 𝚘𝚕 𝚍𝚎𝚢e𝚌ə𝚖 𝚊𝚖𝚖𝚊 𝚜ə𝚗𝚒 𝚍ə 𝚌̧ə𝚝𝚒𝚗 𝚟ə𝚣𝚒𝚢𝚢ə𝚝𝚍ə 𝚚𝚘𝚢𝚖𝚊𝚐̆ 𝚒𝚜𝚝ə𝚖𝚒𝚛ə𝚖🤧','İnsanlığa dəvət etdikdə yolu soruşan insanlar var.🔥😂','Qoyduğum şeyləri öz yerində tapa bilmirəm. Bəzilərini adam yerinə qoydum, indi gəl tap görün necə tapırsan✊','Ayə biri bunu aparsın🫢','Əgər bu həyatda öz tayını tapa bilmirsənsə üzülmə, deməli sən tayı bərabəri olmayan birisən.Qabriel Qarsia Markuez (Meksikalı yazıçı)🥲','Xoş Gəldim Nəfəs🥲','Gəlmirsən Balaca😒','Kimə Yazısan??? 🤨','Çirkin Çocuq Gəl😌','Cikolatam😍','Aaa Səndə Burdasan😳','Al Sənə Çikolata🤓👉🍫','Sevmirsən Məni?🙁 Onda Ol🙂','Haa Düz derisən?🧐','Bu Kimdir😁','Gəl Dava Edəx😁💪','Bax Sənə Nə Aldım😌👉🐒','Nə Gözəlsən🤢 Çirkin Ördək Yavrusu','Sən Kimsən🙄A Gədə👀','Gəl Sənə Sürpürüzüm var🤫','Ooo Çox Gözəlsin🤌🤐Bal','Şəxsiyə Yaz😌dünbələx','Gəl Görüm Hələ🧐 Nə demisən Mənə😬','Ayib Olsun😫 Niyə Yazmırsan😑','Bezdim Səndən🥲','Bu Neçədir✌️🙂','Nömrəni ver də Vpda yazışa🙊','👉👀 Gözün Çıxsın gəl😒','ımmm Gəl yogo yapalım🧘‍♀🤭','gəl sənə bıra süzdüm😪🍻','Ağlımı Başımdan ala şəxs😵‍💫gəl mənə doğru','Səni gördüm qızmam qalxdə🤒',) 

# @app.on_message(
       # filters.command("broadcast") & filters.user(SUDO_USERS)
  #  )
   # async def broadcast_func(_, message: Message):
   #  if db is None:
          #  return await message.reply_text(
               # "MONGO_DB_URI var müəyyən edilməyib. Zəhmət olmasa əvvəlcə onu müəyyənləşdirin"
           # )
       # if message.reply_to_message:
        #    x = message.reply_to_message.message_id
          #  y = message.chat.id
       # else:
           # if len(message.command) < 2:
              #  return await message.reply_text(
                   # "**İstifadə**:\n/broadcast [MESSAGE] və ya [Mesajı Cavab]"
              #  )
          #  query = message.text.split(None, 1)[1]

      #  susr = 0
      #  served_users = []
       # susers = await mongo.get_served_users()
       # for user in susers:
           # served_users.append(int(user["user_id"]))
      #  for i in served_users:
           # try:
              #  await app.forward_messages(
                   # i, y, x
              #  ) if message.reply_to_message else await app.send_message(
                   # i, text=query
               # )
              #  susr += 1
          #  except FloodWait as e:
               # flood_time = int(e.x)
               # if flood_time > 200:
               #     continue
               # await asyncio.sleep(flood_time)
           # except Exception:
             #   pass
       # try:
          #  await message.reply_text(
               # f"**Mesajı yayımlayın {susr} İstifadəçilər.**"
          #  )
        #except:
          #  pass








@client.on(events.NewMessage(pattern='/olive'))
async def handler(event):
    # Kimsə "Salam" və başqa bir şey deyəndə cavab verin
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("__Sən mənə sahib deyilsən!__")
    await event.reply('**Bot Online Narahat Olmayın** \n @AnonyumAzBot')

	
	

@client.on(events.NewMessage())
async def mentionalladmin(event):
  global grup_sayi
  if event.is_group:
    if event.chat_id in grup_sayi:
      pass
    else:
      grup_sayi.append(event.chat_id)

@client.on(events.NewMessage(pattern='^/statik ?(.*)'))
async def son_durum(event):
    global anlik_calisan,grup_sayi,özel_list
    sender = await event.get_sender()
    if sender.id not in ozel_list:
      return
    await event.respond(f"**O L D TAGGER BOT Statikaları ⚛**\n\nToplam Grup: `{len(grup_sayi)}`\nAnlıq Aktiv Grup: `{len(anlik_calisan)}`")
	
	
	

@client.on(events.NewMessage(pattern='^/broadcast ?(.*)'))
async def duyuru(event):
	
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**Reklam**\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Gönderildi.")
	
	
	
	
@client.on(events.NewMessage(pattern='/reklam'))
async def handler(event):	
     await event.reply('🤖 [ 𝕆𝕃𝔻 TAGGER BOT](http://t.me/oldtaggerBot)-unda Reklam Almaq Üzçün [sahibim ¦ 💎](https://t.me/AnonyumAz)-ilə Әlaqә Saxlayın.')
    


@client.on(events.NewMessage(pattern='^/pro'))
async def event(ups):
  if ups.sender_id == 5508658149:
    await ups.reply("**Salam ᴀʙᴀᴤᴏᴠ! O L D TAGGER hizmətindədir. ☯️**")
  elif ups.sender_id == 5134595693:
    await ups.reply("**Salam Sahibim! O L D TAGGER hizmətindədir. ☯️**")
  elif ups.sender_id == 5823284681:
    await ups.reply("**Salam Dosdum Zeyn! O L D TAGGER hizmətindədir. ☯️**")
  else:
    await ups.reply("**Sən pro user deyilsən. 💎**")



@client.on(events.NewMessage(pattern='/sahib'))
async def handler(event):	
     await event.reply('🇦🇿 sahiblər**\n**@AnonyumAz**\n**@SatisAzOwner.')
    

 
@client.on(events.ChatAction)   
async def handler(event):
    if event.user_joined:
        await event.reply("Salam Xow geldin")
          
          
 
@client.on(events.NewMessage(pattern='(?i)salam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}") 


        
print(">> Bot işləyir narahat olmayın. @AnonyumAz Məlumat almaq üçün <<")
client.run_until_disconnected()
