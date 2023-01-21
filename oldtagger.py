import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import events, Button
from telethon.tl.custom import Button
import random # pip install random
from random import randint
import configparser
from asyncio import sleep
from telethon import events
from Config import Config 
# Pyrogram----------------------------------------------------------------------------------------------------
import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import time
import traceback
import aiofiles
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os, youtube_dl, requests, time
from Config import Config
from youtube_search import YoutubeSearch
import lyricsgenius
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import yt_dlp
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery 
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import random, re
from telegraph import upload_file
import pyrogram
import os
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)



logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS

ydl_opts = {
    'format': 'best',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True,
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="➕️ GROUPA ELAVE ET", url=f"http://t.me/oldtaggerbot?startgroup=a")]])

#-#-#-# Pyrogram Başlanğıc #-#-#-#
app = Client(":memory:", api_id, api_hash, bot_token=bot_token)



# Qruplara yayım mesajı




############## DEĞİŞKENLER ##############

DATABASE_URL = "mongodb+srv://Bots:Bots@cluster0.nedd9xs.mongodb.net/?retryWrites=true&w=majority"
BOT_USERNAME = "OldMultiBot"
LOG_CHANNEL = -1001737573985
GROUP_SUPPORT = "TEAMABASOFcom"
GONDERME_TURU = False
OWNER_ID = [5134595693]
LANGAUGE = "AZ"

#---------------------------------------------------------------GROUP GIREKEN SALAMLAMA MSJ------------------------------------------------------------------------------#
@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `Məni` {msg.chat.title} `Qrupa əlavə etdiyiniz üçün təşəkkürlər⚡️` \n\n **🤖Qrupda bir cox funksyalı Multi botam.\n🤖Kömək üçün /start yazmaq kifayətdir.✨**''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-------------------------------------------------------------OWNERS SALAMLAMA MSJ---------------------------------------------------------------------------------------#
      
#	elif str(new_user.id) == str(Config.OWNER_ID):
#           await msg.reply('🤖 [Ədalət 𝗧𝗮𝗴𝗴𝗲𝗿](https://t.me/EdaletSup)-un Sahibi, Qrupa Qatıldı.\n Xoş Gəldin  Aramıza Sahib, Necəsən?🥰.')

	
	
	
#-------------------------------------------------------------VERİTABANI VERİ GİRİŞ ÇIKIŞI---------------------------------------------------------------------------------------#
 
class Database: 
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id): # Veritabanına yeni kullanıcı ekler
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            ban_status=dict(
                is_banned=False,
                ban_duration=0,
                banned_on=datetime.date.max.isoformat(),
                ban_reason="",
            ),
        )

    async def add_user(self, id): # Veritabına yeni kullanıcı eklemek için ön def
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id): # Bir kullanıcının veritabında olup olmadığını kontrol eder.
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self): # Veritabanındaki toplam kullanıcıları sayar.
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self): # Veritabındaki tüm kullanıcıların listesini verir.
        return self.col.find({})

    async def delete_user(self, user_id): # Veritabından bir kullanıcıyı siler.
        await self.col.delete_many({"id": int(user_id)})

    async def ban_user(self, user_id, ban_duration, ban_reason): # Veritabanınızdaki bir kullanıcıyı yasaklılar listesine ekler.
        ban_status = dict(
            is_banned=True,
            ban_duration=ban_duration,
            banned_on=datetime.date.today().isoformat(),
            ban_reason=ban_reason,
        )
        await self.col.update_one({"id": user_id}, {"$set": {"ban_status": ban_status}})

    async def remove_ban(self, id): # Veritabanınızdaki yasaklılar listesinde bulunan bir kullanıcın yasağını kaldırır.
        ban_status = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        await self.col.update_one({"id": id}, {"$set": {"ban_status": ban_status}})

    async def get_ban_status(self, id): # Bir kullanıcın veritabanınızda yasaklılar listesinde olup olmadığını kontrol eder.
        default = dict(
            is_banned=False,
            ban_duration=0,
            banned_on=datetime.date.max.isoformat(),
            ban_reason="",
        )
        user = await self.col.find_one({"id": int(id)})
        return user.get("ban_status", default)

    async def get_all_banned_users(self): # Veritabınızdaki yasaklı kullanıcılar listesini verir.
        return self.col.find({"ban_status.is_banned": True})


db = Database(DATABASE_URL, BOT_USERNAME)
mongo_db_veritabani = MongoClient(DATABASE_URL)
dcmdb = mongo_db_veritabani.handlers



################## KULLANICI KONTROLLERİ #############
async def handle_user_status(bot: Client, cmd: Message): # Kullanıcı kontrolü
    chat_id = cmd.chat.id
    if not await db.is_user_exist(chat_id):
        if cmd.chat.type == "private":
            await db.add_user(chat_id)
            await bot.send_message(LOG_CHANNEL,LAN.BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id))
        else:
            await db.add_user(chat_id)
            chat = bot.get_chat(chat_id)
            if str(chat_id).startswith("-100"):
                new_chat_id = str(chat_id)[4:]
            else:
                new_chat_id = str(chat_id)[1:]
            await bot.send_message(LOG_CHANNEL,LAN.GRUP_BILDIRIM.format(cmd.from_user.first_name, cmd.from_user.id, cmd.from_user.first_name, cmd.from_user.id, chat.title, cmd.chat.id, cmd.chat.id, cmd.message_id))

    ban_status = await db.get_ban_status(chat_id) # Yasaklı Kullanıcı Kontrolü
    if ban_status["is_banned"]:
        if int((datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])).days) > int(ban_status["ban_duration"]):
            await db.remove_ban(chat_id)
        else:
            if GROUP_SUPPORT:
                msj = f"@{GROUP_SUPPORT}"
            else:
                msj = f"[{LAN.SAHIBIME}](tg://user?id={OWNER_ID})"
            if cmd.chat.type == "private":
                await cmd.reply_text(LAN.PRIVATE_BAN.format(msj), quote=True)
            else:
                await cmd.reply_text(LAN.GROUP_BAN.format(msj),quote=True)
                await bot.leave_chat(cmd.chat.id)
            return
    await cmd.continue_propagation()




############### Broadcast araçları ###########
broadcast_ids = {}


async def send_msg(user_id, message): # Mesaj Gönderme
    try:
        if GONDERME_TURU is False:
            await message.forward(chat_id=user_id)
        elif GONDERME_TURU is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.x))
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id}: {LAN.NOT_ONLINE}\n"
    except UserIsBlocked:
        return 400, f"{user_id}: {LAN.BOT_BLOCKED}\n"
    except PeerIdInvalid:
        return 400, f"{user_id}: {LAN.USER_ID_FALSE}\n"
    except Exception:
        return 500, f"{user_id}: {traceback.format_exc()}\n"

async def main_broadcast_handler(m, db): # Ana Broadcast Mantığı
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text=LAN.BROADCAST_STARTED)
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total=total_users, current=done, failed=failed, success=success)
    async with aiofiles.open("broadcast-logs-g4rip.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success))
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(text=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    else:
        await m.reply_document(document="broadcast-logs-g4rip.txt", caption=LAN.BROADCAST_STOPPED.format(completed_in, total_users, done, success, failed), quote=True,)
    os.remove("broadcast-logs-g4rip.txt")



# Genelde müzik botlarının mesaj silme özelliği olur. Bu özelliği ReadMe.md dosyasındaki örnekteki gibi kullanabilirsiniz.
delcmdmdb = dcmdb.admins

async def delcmd_is_on(chat_id: int) -> bool: # Grup için mesaj silme özeliğinin açık olup olmadığını kontrol eder.
    chat = await delcmdmdb.find_one({"chat_id": chat_id})
    return not chat


async def delcmd_on(chat_id: int): # Grup için mesaj silme özeliğini açar.
    already_del = await delcmd_is_on(chat_id)
    if already_del:
        return
    return await delcmdmdb.delete_one({"chat_id": chat_id})


async def delcmd_off(chat_id: int): # Grup için mesaj silme özeliğini kapatır.
    already_del = await delcmd_is_on(chat_id)
    if not already_del:
        return
    return await delcmdmdb.insert_one({"chat_id": chat_id})



################# SAHİP KOMUTLARI #############

# Verileri listeleme komutu
@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def botstats(bot: Client, message: Message):
    g4rip = await bot.send_message(message.chat.id, LAN.STATS_STARTED.format(message.from_user.mention))
    all_users = await db.get_all_users()
    groups = 0
    pms = 0
    async for user in all_users:
        if str(user["id"]).startswith("-"):
            groups += 1
        else:
            pms += 1
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent
    total_users = await db.total_users_count()
    await g4rip.edit(text=LAN.STATS.format(BOT_USERNAME, total_users, groups, pms, total, used, disk_usage, free, cpu_usage, ram_usage, __version__), parse_mode="md")



# Botu ilk başlatan kullanıcıların kontrolünü sağlar.
@app.on_message()
async def G4RIP(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)



# Broadcast komutu
@app.on_message(filters.command("reklam") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)



# Bir kullanıcı yasaklama komutu
@app.on_message(filters.command("block") & filters.user(OWNER_ID))
async def ban(c: Client, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
        if len(m.command) <= 1:
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 2:
            ban_duration = 9999
            ban_reason = " ".join(m.command[1:])
    else:
        if len(m.command) <= 1:
            return await m.reply(LAN.NEED_USER)
        elif len(m.command) == 2:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = LAN.BAN_REASON.format(BOT_USERNAME)
        elif len(m.command) == 3:
            user_id = int(m.command[1])
            ban_duration = 9999
            ban_reason = " ".join(m.command[2:])
    
        if str(user_id).startswith("-"):
            try:    
                ban_log_text = LAN.BANNED_GROUP.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_GROUP.format(ban_reason))
                await c.leave_chat(user_id)
                ban_log_text += LAN.GROUP_BILGILENDIRILDI
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.GRUP_BILGILENDIRILEMEDI.format(traceback.format_exc())
        else:
            try:    
                ban_log_text = LAN.USER_BANNED.format(m.from_user.mention, user_id, ban_duration, ban_reason)
                await c.send_message(user_id, LAN.AFTER_BAN_USER.format(ban_reason))
                ban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                ban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.ban_user(user_id, ban_duration, ban_reason)
        await c.send_message(LOG_CHANNEL, ban_log_text)
        await m.reply_text(ban_log_text, quote=True)



# Bir kullanıcın yasağını kaldırmak komutu
@app.on_message(filters.command("unblock") & filters.user(OWNER_ID))
async def unban(c: Client, m: Message):
        if m.reply_to_message:
            user_id = m.reply_to_message.from_user.id
        else:
            if len(m.command) <= 1:
                return await m.reply(LAN.NEED_USER)
            else:
                user_id = int(m.command[1])
        unban_log_text = LAN.UNBANNED_USER.format(m.from_user.mention, user_id)
        if not str(user_id).startswith("-"):
            try:
                await c.send_message(user_id, LAN.USER_UNBAN_NOTIFY)
                unban_log_text += LAN.KULLANICI_BILGILENDIRME
            except BaseException:
                traceback.print_exc()
                unban_log_text += LAN.KULLANICI_BILGILENDIRMEME.format(traceback.format_exc())
        await db.remove_ban(user_id)
        await c.send_message(LOG_CHANNEL, unban_log_text)
        await m.reply_text(unban_log_text, quote=True)



# Yasaklı listesini görme komutu
@app.on_message(filters.command("blocklist") & filters.user(OWNER_ID))
async def _banned_usrs(_, m: Message):
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += LAN.BLOCKS.format(user_id, ban_duration, banned_on, ban_reason)
    reply_text = LAN.TOTAL_BLOCK.format(banned_usr_count, text)
    if len(reply_text) > 4096:
        with open("banned-user-list.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-user-list.txt", True)
        os.remove("banned-user-list.txt")
        return
    await m.reply_text(reply_text, True)



############## BELİRLİ GEREKLİ DEF'LER ###########
def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"



########### ÇOKLU DİL ##############
class LAN(object):

    if LANGAUGE == "TR":

        BILDIRIM = "```📣 Yeni Bildirim``` \n\n#YENI_KULLANICI **botu başlattı!** \n\n🏷 isim: `{}` \n📮 kullanıcı id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})"
        GRUP_BILDIRIM = "```📣 Yeni Bildirim``` \n\n#YENI_GRUP **botu başlattı!** \n\n🏷 Gruba Alan İsim: `{}` \n📮 Gruba Alan kullanıcı id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})\n Grubun Adı: {}\n Grubun ID: {}\n Grubun Mesaj Linki( sadece açık gruplar): [Buraya Tıkla](https://t.me/c/{}/{})"
        SAHIBIME = "sahibime"
        PRIVATE_BAN = "Üzgünüm, yasaklandınız! Bunun bir hata olduğunu düşünyorsanız {} yazın."
        GROUP_BAN = "Üzgünüm, grubunuz karalisteye alındı! Burada daha fazla kalamam. Bunun bir hata olduğunu düşünyorsanız {} yazın.'"
        NOT_ONLINE = "aktif değil"
        BOT_BLOCKED = "botu engellemiş"
        USER_ID_FALSE = "kullanıcı kimliği yanlış"
        BROADCAST_STARTED = "```📤 BroadCast başlatıldı! Bittiği zaman mesaj alacaksınız!"
        BROADCAST_STOPPED = "✅ ```Broadcast başarıyla tamamlandı.``` \n\n**Şu Kadar Sürede Tamamlandı:** `{}` \n\n**Kayıtlı Toplam Kullanıcı:** `{}` \n\n**Toplam Gönderme Denemesi:** `{}` \n\n**Başarıyla Gönderilen:** `{}` \n\n**Toplam Hata:** `{}`"
        STATS_STARTED = "{} **Lütfen bekleyiniz verileri getiriyorum!**"
        STATS = """**@{} Verileri**\n\n**Kullanıcılar;**\n» **Toplam Sohbetler:** `{}`\n» **Toplam Gruplar: `{}`\n» **Toplam PM's: `{}`\n\n**Disk Kullanımı;**\n» **Disk Alanı:** `{}`\n» **Kullanılan:** `{}({}%)`\n» **Boşta:** `{}`\n\n**🎛 En Yüksek Kullanım Değerleri;**\n» **CPU:** `{}%`\n» **RAM:** `{}%`\n**Sürümler;**\n» **Pyrogram:** {}\n\n\n__• By @BasicBots__"""
        BAN_REASON = "Bu sebep yasaklandığınız için @{} tarafından otomatik olarak oluşturulmuştur"
        NEED_USER = "**Lütfen Kullanıcı kimliği verin.**"
        BANNED_GROUP = "🚷 **Yasaklandı!\n\nTarafından:** {}\n**Grup ID:** `{}` \n**Süre:** `{}` \n**Sebep:** `{}`"
        AFTER_BAN_GROUP = "**Üzgünüm grubunuz kara listeye alındı! \n\nSebep:** `{}`\n\n**Daha fazla burada kalamam. Bunun bir hata olduğunu düşünüyorsanız destek grubuna gelin.**"
        GROUP_BILGILENDIRILDI = "\n\n✅ **Grubu bilgilendirdim ve gruptan ayrıldım.**"
        GRUP_BILGILENDIRILEMEDI = "\n\n❌ **Grubu bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        USER_BANNED = "🚷 **Yasaklandı! \n\nTarafından:** {}\n **Kullanıcı ID:** `{}` \n**Süre:** `{}` \n**Sebep:** `{}`"
        AFTER_BAN_USER = "**Üzgünüm kara listeye alındınız! \n\nSebep:** `{}`\n\n**Bundan sonra size hizmet veremeyeceğim.**"
        KULLANICI_BILGILENDIRME = "\n\n✅ Kişiyi bilgilendirdim."
        KULLANICI_BILGILENDIRMEME = "\n\n❌ **Kişiyi bilgilendirmeye çalışırken bir hata oluştu:** \n\n`{}`"
        UNBANNED_USER = "🆓 **Kullanıcının Yasağı Kaldırıldı !** \nTarafından: {} \n**Kullanıcı ID:**{}"
        USER_UNBAN_NOTIFY = "🎊 Müjde! Yasağınız kaldırıldı!"
        BLOCKS = "🆔 **Kullanıcı ID**: `{}`\n⏱ **Süre**: `{}`\n🗓 **Yasaklanan Tarih**: `{}`\n💬 **Sebep**: `{}`\n\n"
        TOTAL_BLOCK = "🚷 **Toplam Yasaklanan:** `{}`\n\n{}"

    elif LANGAUGE == "AZ":

        BILDIRIM = "```📣 Yeni İsmarıc``` \n\n#YENI_ISTIFADƏÇİ **botu başlatdı!** \n\n🏷 isim: `{}` \n📮 istifadəçi id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})"
        GRUP_BILDIRIM = "```📣 Yeni İsmarıc``` \n\n#YENI_QRUP **botu başlatdı!** \n\n🏷 Qrupa əlavə edən: `{}` \n📮 Qrupa əlavə edən istifadəçi id: `{}` \n🧝🏻‍♂️ profil linki: [{}](tg://user?id={})\n Qrupun adı: {}\n Qrupun ID: {}\n Qrupun mesaj kinki( sadəcə açıq qruplar): [Buraya Toxun](https://t.me/c/{}/{})"
        SAHIBIME = "sahibimə"
        PRIVATE_BAN = "Məyusam, əngəlləndiniz! Bunun bir xəta olduğunu düşünürsünüz isə {} yazın."
        GROUP_BAN = "Məyusam, qrupunuz qara siyahıya əlavə olundu! Artıq burada qala bilmərəm! Bunun bir xəta olduğunu düşünürsünüz isə {} yazın.'"
        NOT_ONLINE = "aktiv deyil"
        BOT_BLOCKED = "botu əngəlləyib"
        USER_ID_FALSE = "istifadəçi id'i yanlışdır."
        BROADCAST_STARTED = "```📤 BroadCast başladıldı! Bitəndə mesaj alacaqsınız."
        BROADCAST_STOPPED = "✅ ```Broadcast uğurla tamamlandı.``` \n\n**Bu qədər vaxtda tamamlandı** `{}` \n\n**Ümumi istifadəçilər:** `{}` \n\n**Ümumi göndərmə cəhdləri:** `{}` \n\n**Uğurla göndərilən:** `{}` \n\n**Ümumi xəta:** `{}`"
        STATS_STARTED = "{} **Zəhmət olmasa gözləyin, bilgiləri gətirirəm!**"
        STATS = """**@{} Məlumatları**\n\n**İstifadəçiləri;**\n» **Ümumi söhbətlər:** `{}`\n» **Ümumi qruplar: `{}`\n» **Ümumi PM's: `{}`\n\n**Disk İstifadəsi;**\n» **Disk'in Sahəsi:** `{}`\n» **İstifadə edilən:** `{}({}%)`\n» **Boş qalan:** `{}`\n\n**🎛 Ən yüksək istifadə dəyərləri;**\n» **CPU:** `{}%`\n» **RAM:** `{}%`\n**Versiyalar;**\n» **Pyrogram:** {}\n\n\n__• By @BasicBots__"""
        BAN_REASON = "Bu sebep yasaklandığınız için @{} tarafından otomatik olarak oluşturulmuştur"
        NEED_USER = "**Zəhmət olmasa istifadəçi id'si verin.**"
        BANNED_GROUP = "🚷 **Qadağan olundu!\n\nQadağan edən:** {}\n**Qrup ID:** `{}` \n**Vaxt:** `{}` \n**Səbəb:** `{}`"
        AFTER_BAN_GROUP = "**Məyusam, qrupunyz qara siyahıya əlavə edildi! \n\nSəbəb:** `{}`\n\n**Artıq burada qala bilmərəm. Bunun bir xəta olduğunu düşünürsünüzsə, dətək qrupuna gəlin.**"
        GROUP_BILGILENDIRILDI = "\n\n✅ **Qrupu bilgiləndirdim və qrupdan çıxdım.**"
        GRUP_BILGILENDIRILEMEDI = "\n\n❌ **Qrupu məlumatlandırarkən xəta yarandı:** \n\n`{}`"
        USER_BANNED = "🚷 **Qadağan olundu! \n\nQadağan edən:** {}\n **İstifadəçi ID:** `{}` \n**Vaxt:** `{}` \n**Səbəb:** `{}`"
        AFTER_BAN_USER = "**Məyusam, qara siyahıya əlavə edildiniz! \n\nSəbəb:** `{}`\n\n**Bundan sonra sizə xidmət etməyəcəyəm.**"
        KULLANICI_BILGILENDIRME = "\n\n✅ İstifadəçini məlumatlandırdım."
        KULLANICI_BILGILENDIRMEME = "\n\n❌ **İstifadəçini məlumatlandırarkən xəta yarandı:** \n\n`{}`"
        UNBANNED_USER = "🆓 **İstifadəçinin qadağası qaldırıldı !** \nQadağanı qaldıran: {} \n**İstifadəçi ID:**{}"
        USER_UNBAN_NOTIFY = "🎊 Sizə gözəl bir xəbərim var! Artıq əngəliniz qaldırıldı!"
        BLOCKS = "🆔 **İstifadəçi ID**: `{}`\n⏱ **Vaxt**: `{}`\n🗓 **Qadağan edildiyi tarix**: `{}`\n💬 **Səbəb**: `{}`\n\n"
        TOTAL_BLOCK = "🚷 **Ümumi əngəllənən:** `{}`\n\n{}"
	

	
@app.on_message(filters.command("delcmd") & ~filters.private)
async def delcmdc(bot: Client, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Bu əmrdən istifadə etmək üçün əmrinizin yanında 'off' və ya 'on' yazın.")
    durum = message.text.split(None, 1)[1].strip()
    durum = durum.lower()
    chat_id = message.chat.id

    if durum == "on":
        if await delcmd_is_on(message.chat.id):
            return await message.reply_text("Komandanın Silinməsi Artıq Aktivdir.")
        else:
            await delcmd_on(chat_id)
            await message.reply_text("Bu söhbət üçün Sil əmri uğurla aktivləşdirildi.")

    elif durum == "off":
        await delcmd_off(chat_id)
        await message.reply_text("Komanda Silmə funksiyası bu Söhbət üçün uğurla deaktiv edildi.")
    else:
        await message.reply_text("Bu əmrdən istifadə etmək üçün əmrinizin yanında 'off' və ya 'on' yazın.")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []



#edalet_22 terefinden elave edildi
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
  

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"**👋 Salam mən bir cox funksyalı OLD MULTİ botam\n\n💁🏻 Ətraflı məlumat üçün 'Aşaqıdakı Buttonlardan' baxa bilersiz əmirlərimə\n\n📨 Botu başladıqınza dayir sahibime bildiriş yolladım**", buttons=(
                     [Button.url('➕ Qrupa Əlavə Et ➕','http://t.me/OldMultiBot?startgroup=a')],
       # [Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
              # [Button.url('Qurup🛠', 'https://t.me/Bizim_Paytaxt'),
                    #  Button.url('💡 USTA Bots', 'https://t.me/ustabots')],
               [Button.inline(f"📮 Əmrlər", data="help"),
                Button.inline(f"📥 YÜKLƏMƏ", data="dhelp")],
               [Button.inline(f"🕹 GAME", data="game"),
                      Button.url('🇦🇿 Reklam', 'http://t.me/oldtaggerReklam')],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"**[@OldMultiBot](http://t.me/OldMultiBot)'un məlumatları**", buttons=(
                     [Button.url('💡 Bota Keç','https://t.me/OldMultiBot?start=start')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
          Button.url('🇦🇿 Reklam','https://t.me/oldtaggerReklam')],
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**👋 Salam mən bir cox funksyalı OLD MULTİ botam😇\n\n💁🏻 Ətraflı məlumat üçün 'Aşaqıdakı Buttonlardan' baxa bilersiz əmirlərimə\n\n📨 Botu başladıqınza dayir sahibime bildiriş yolladım**", buttons=(
                     [Button.url('➕ Qrupa Əlavə Et ➕','http://t.me/oldtaggerbot?startgroup=a')],
        # [Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               #[Button.url('Qurup🛠', 'https://t.me/Bizim_Paytaxt'),
                      #Button.url('🤖 USTA Bots', 'https://t.me/ustabots')],
               [Button.inline(f"📮 TAG Əmrlər", data="thelp"),
                Button.inline(f"📥 YÜKLƏMƏ", data="dhelp")],
               [Button.inline(f"🕹 GAME", data="game"),
                      Button.url('🇦🇿 Reklam', 'https://t.me/oldtaggerReklam')],
                    ),
                    link_preview=False)

# gece kusu
@client.on(events.callbackquery.CallbackQuery(data="thelp"))
async def handler(event): 
    await event.edit(f"**[@OldMultiBot](http://t.me/OldMultiBot)-un '📚 TAG Əmrlər' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🤖➪ /tag - 5-li tağ edər**\n**🤖➪ /etag - Emoji ilə tağ edər**\n**🤖➪ /stag - Sözlər ilə tağ edər**\n**🤖➪ /tektag - Tək-Tək tağ edər**\n**🤖➪ /usta - Usta tağ botuna aid tağ edər**\n**🤖➪ /admins - Adminləri tağ edər**\n**🤖➪ /cancel - Tağı dayandırar**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
              # [Button.url('➕ Məni Qrupa əlavə et ➕','http://t.me/UstaTagbot?startgroup=a')],
         #[Button.url('🎉 Sahib', 'https://t.me/Nehmedov')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('🇦🇿 Reklam','https://t.me/oldtaggerReklam')],
               [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="dhelp"))
async def handler(event): 
    await event.edit(f"**📌 [@OldMultiBot](http://t.me/OldMultiBot)-un '📥 YÜKLƏMƏ' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🎵 ➪ /bul - Musiqi yükleyir**\n**🖼 ➪ telegrap - bota şexside photo,video,gif ataraq telegrap linkin ala bilersiz**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
       #  [Button.url('🙇🏻 Sahib','https://t.me/AnonyumAz')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('🇦🇿 Reklam','https://t.me/oldtaggerReklam')],
               [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="game"))
async def handler(event): 
    await event.edit(f"**📌 [@OldMultiBot](http://t.me/OldMultiBot)-un '🕹 GAME' bölməsi ⤵**\n\n\n•━━━━━━━━•••━━━━━━━━•\n**🎲 ➪ /zer - zer atar**\n**🎯 ➪ /ox - Ox atar**\n**⚽️ ➪ /gol - qoal at**\n**🏀 ➪ /basket - basket atar**\n**🎰 ➪ /spin - sansini dene**\n**🎳 ➪ /bowling - bowling atar**\n**🧮 ➪ /quiz Hesablamani tap**\n•━━━━━━━━•••━━━━━━━━•", buttons=(
       #  [Button.url('🙇🏻 Sahib','https://t.me/AnonyumAz')],
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
                      Button.url('🇦🇿 Reklam','https://t.me/oldtaggerReklam')],
               [Button.inline(f"🔙 Geri", data="start")]
                    ),
                    link_preview=False)


  
  
  
    
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "😀 🐵 🍓 😃 🦁 🍒 😄 🐯 🍎 😁 🐱 🍉 😆 🐶 🍑 😅 🐺 🍊 😂 🐻 🥭 🤣 🐨 🍍 😭 🐼 🍌 😗 🐹 🌶 😙 🐭 🍇 😚 🐰 🥝 😘 🦊 🍐 🥰 🦝 🍏 🤩 🐮 🍈 🥳 🐷 🍋 🤗 🐽 🍄 🙃 🐗 🥕 🙂 🦓 🍠 ☺️ 🦄 🧅 😊 🐴 🌽 😏 🐸 🥦 😌 🐲 🥒 😉 🦎 🥬 🤭 🐉 🥑 😶 🦖 🥯 😐 🦕 🥖 😑 🐢 🥐 😔 🐊 🍞 😋 🐁 🌰 😛 🐀 🥔 😝 🐇 🧄 😜 🐈 🍆 🤪 🐩 🧇 🤔 🐕 🥞 🤨 🦮 🥚 🧐 🐕‍🦺 🧀 🙄 🐅 🥓 😒 🐆 🥩 😤 🐎 🍗 😠 🐖 🍖 🤬 🐄 🥙 ☹️ 🐂 🌯 🙁 🐃 🌮 😕 🐏 🍕 😟 🐑 🍟 🥺 🐐 🥨 😳 🦌 🥪 😬 🦙 🌭 🤐 🦥 🍔 🤫 🦘 🧆 😰 🐘 🥘 😨 🦏 🍝 😧 🦛 🥫 😦 🦒 🥣 😮 🐒 🥗 😯 🦍 🍲 😲 🦧 🍛 😱 🐪 🍜 🤯 🐫 🍢 😢 🐿️ 🥟 😥 🦨 🍱 😓 🦡 🍚 😞 🦔 🥡 😖 🦦 🍤 😣 🦇 🍣 😩 🐓 🦞 😫 🐔 🦪 🤤 🐣 🍘 🥱 🐤 🍡 😴 🐥 🥠 😪 🐦 🥮 🤢 🦉 🍧 🤮 🦅 🍨 🤧 🦜 🍫 🤒 🪱 🍪 😶‍🌫 🕊️ 🥜 🤠 🦢 🍭 🤑 🦩 🧈 🤤 🦃 🦚 🥵 🦆 🫑 🥶 🐧 🍥 🥸 🦈 🍦 🤓 🐳 🍳 😇 🐝 🥧 🤭 🐌 🥤 🤫 🦋 🍨".split(" ")
  
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
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Tag əməliyyatı uğurla dayandırıldı!**")
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
      usrtxt += f"↯ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
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
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
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
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond(" **Tag əməliyyatı uğurla dayandırıldı! **")
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
      usrtxt += f"**↯ [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"↯ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
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
"Qaş qabağın yerlə gedir",
"De görüm neyləmişəm",
"Ürəyim gup-gup edir",
"Bir günahım yoxdur, inan",
"Varsa – de, olum qurban!",
"Dözmərəm bu hala mən",
"Ölürəm az qala mən",

"Bir mənə bax, naz eyləmə",
"Qaş qabaq tökmə belə",
"Gəl mənə dağ çəkmə belə",

"Kim nə deyib, söylə, görüm",
"Səni yoldan eyləyib?",
"Kim sənə nə danışıb",
"Məni xortdan eyləyib?",
"Hardadır o mərdiməzar?",
"Onu qoy tutsun azar!..",

"Dağlarda duman gözəldir",
"Qaşların - kaman gözəldir",
"Sözünə heç bir söz olmaz",
"Gözlərin yaman gözəldir",
"Alıbdır ağlımı başdan",
"Keçmək olmaz bu göz-qaşdan",
"Səni mən yaman sevirəm",
"Ürəkdən, candan sevirəm",
"Mənə gəl eylə vəfa, yar",
"Aşiqə etmə cəfa, yar",
"Söyüdlər başın əyəndə",
"Sənə mən yarım deyəndə",
"Sanıram dünya mənimdir",
"Gözümə gözün deyəndə",
"Alıbdır ağlımı başdan",
"Keçmək olmaz bu göz-qaşdan",
"Səni mən yaman sevirəm",
"Ürəkdən, candan sevirəm",
"Mənə gəl eylə vəfa, yar",
"Aşiqə etmə cəfa, yar",
"O qara göz olmasaydı",
"Əhdimiz düz olmasaydı",
"Sənə heç könül verərdim",
"Sözümüz söz olmasaydı?",

"Gedirəm bu axşam, gedirəm gülüm",
"Bilirəm gül üzün solacaq mənsiz",
"Gedirəm gəlməsəm qalacaq sevgim",
"Bəlkə də gözlərin dolacaq mənsiz",
"Yaşadır sevdalı bir xəyal məni",
"Gedirəm gəlməsəm yada sal məni",
"Bürüyüb göyləri indi çən, duman",
"Torpaq dilə gəlib aman! ay aman!",
"Vətən gözü yaşlı qalsa o zaman",
"Ay Allah, sevgilim qalacaq mənsiz!",

"Axtarıb tapdım səni ",
"Sən dəmi sevdim, yar, məni? ",
"Gör nə haldır görmür gözüm Şadlığımdan dünyanı",
"Gəl gəl, maralım, gəl",
"Gəl, ceyranım, gəl",
"Halal olsun Süleyman",
"Sən nə kələkbazsan, şeytan!",
"Öyrədib məni yola saldın",
 "Mənə rast gəldi yarcan",
"Dünyaya sığdıra bilmədim inan dərdlərimi",
"Bu qədər dərd içində dərman olub neyləmisən?",
"Hər sözünə can deyən insandan əsər qalmadı Bax",
"Nə fayda Can deməyim canan olub neyləmisən?",
"Düşünrsənmi sən hərdən görəsən nə haldadır?",
"Bəlkə mənsiz çətindədir boranda ya Qardadır",
"Bəlkə də məndən uzağ ölümlərdədi dardadı",
"Düşünmədin nə fayda insan olub neyləmisən?",
"Yanımda yad biri ilə xoşbəxtliyi təsvir edir",
"Səni yadlarla görəndə ruh bədəni təslim edir",
"O qədər dərd içində əzab vermə bəsdi dedim",
"Sənə görə yar ürəyim al-qan olub neyləmisən?",
"Hər gecə xəyalınla yuxuya dalır bu gözlərim",
"Mən səni gecəni gözləyən ulduz qədər gözlədim",
"Bir dəfə heç olmasa yanıma qonaq gəl istədim",
"Hər gecə xəyalımda mehman olub neyləmisən?",
"Sənə çox can dedim ey can,can olub neyləmisən?",
"Demə canan özünə, canan olub neyləmisən?",
"Getmisən daima biganəni şad eyləmisən",
"Həsrətinlə ürəyim al-qan olub, neynəmisən?",
"Bax indi min cür əzab var başımın üstün duman",
"Mənsiz xoşbəxtdir uzaqlarda eylə güman",
"Mən sənə xəyanət etməm düşünmə əsla bir an" ,
"Xoşbəxtliyi bəxş etməyə fərman olub neyləmisən?",
"Həyatım səliqəlidir istəsən dağıt yenidən",
"Çox heyif gör kimləri qonağ eylədin yerimə",
"Artıq çox yorulmuşam dönürəm day geri mən",
"Biryerdə yolu yeriməyə imkan olub neyləmisən?",
"Gül olub neyləmisən bağçalarda qar borandı",
"Sevirəm söyləmə məni inandırma yar yalandı",
"Buludlar qan ağlayır hər gecələr bu nə qandı?",
"Ürəyim həsrətinlə viran olub neyləmisən?",
"Nə xəyalım var idi səninlə sən məhv elədin",
"O qədər qırmısan ki ürəyim səni əhv eləmir",
"Deyirsən qurban olum məni bağışla səhv elədim",
"Hər dəfə səhvinə görə qurban olub neyləmisən?",

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
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
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
      usrtxt += f"↯ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
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
        text += f" \n ↯ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

	
@client.on(events.NewMessage(pattern="^/rahid ?(.*)"))

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
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
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
      usrtxt += f"↯ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

usta = ('Buda kimmiş də miş miş👀😁😍','🙄👉🤲Aağil','🙄 Sən dediyim sözü elədin? 😐','Həyatımın dolması 🥲 nassın😍','Mənə niyə elə baxırsan? 🌝','İkinci planda olmaqdansa, plana daxil olmamağı seçərəm.  🎯','səni basqa qrublardada görmüsdüm ','Ac olanda sən o sən deyilsən','Niyə yalan danışırsan adamın üstündə patalok var','Həci necəsən ficuuu ','köhnə məkanın yeni sakini ','günün günnən durdun uzax de görüm haramı bəyənmədin','deyrlər ölübsən🤔','Güçlüyüm... Çünkü başka seçeneğim yok düşersem tutanım olmayacak biliyorum...🚬','gəl bir birimizi arka sokaklar bitənə qədər sevək❤️','corona belə böyüdü sən böyümədin','corona belə unduldu səni unuda bilmədim🚬','səni sevirəm sözündə neçə dənə samit var','oğlanlar niyə az yaşayır','bitkilər yaşlandıqcamı ölər yoxsa baxımsızlıqdanmı','isti havada çay içirsən hələdə','allah rəhmət eləsin','tez gəlin hədiyyəli yarışımız basladı','Benim hayelerim kelebeğin ömrü kadar yaşar 💔🥀','Çiçəklərə aşağıdan baxmağa gedirəm..➰','susмuş вir qadın üçün... вiтмiş вir adaмsan.! 🖤','𝚂ə𝚏𝚕ə𝚛𝚒𝚗𝚒 𝚞̈𝚣𝚕ə𝚛𝚒𝚗ə 𝚟𝚞𝚛𝚖𝚊𝚍𝚒𝚐̆𝚒𝚖𝚒𝚣 𝚞̈𝚌̧𝚞̈𝚗 𝚘̈𝚣𝚕𝚎𝚛𝚒𝚗𝚒 𝚚𝚞̈𝚜𝚞𝚛𝚜𝚞𝚣 𝚜𝚊𝚗𝚊𝚗 𝚒𝚗𝚜𝚊𝚗𝚕𝚊𝚛 𝚟𝚊𝚛😒','Güclü olmağa məndən daha çox ehtiyacın var, çünki haqsız olduğunu ürəyinin bir yerində bilirsən.🤙','Makiyaj və üz boyalarınıza güvənməyin. Yollar da gözəldir, lakin altından kanalizasiya keçir.👋😉','𝙸̇𝚝𝚒𝚛𝚍𝚒𝚢𝚒𝚗 𝚟𝚊𝚡𝚝𝚒 𝚚𝚊𝚢𝚝𝚊𝚛𝚊 𝚋𝚒𝚕𝚖ə𝚍𝚒𝚢𝚒𝚗 𝚔𝚒𝚖𝚒 𝚎𝚕ə𝚍𝚒𝚢𝚒𝚗 𝚙𝚒𝚜𝚕𝚒𝚢𝚒 𝚍ə 𝚑𝚎𝚌̧ 𝚟𝚊𝚡𝚝 𝚍𝚞̈𝚣ə𝚕𝚍ə 𝚋𝚒𝚕𝚖𝚎𝚢ə𝚌𝚎𝚔𝚜ən😐','𝙱𝚒𝚛𝚊𝚣 𝚒𝚗𝚜𝚊𝚗 𝚘𝚕 𝚍𝚎𝚢e𝚌ə𝚖 𝚊𝚖𝚖𝚊 𝚜ə𝚗𝚒 𝚍ə 𝚌̧ə𝚝𝚒𝚗 𝚟ə𝚣𝚒𝚢𝚢ə𝚝𝚍ə 𝚚𝚘𝚢𝚖𝚊𝚐̆ 𝚒𝚜𝚝ə𝚖𝚒𝚛ə𝚖🤧','İnsanlığa dəvət etdikdə yolu soruşan insanlar var.🔥😂','Qoyduğum şeyləri öz yerində tapa bilmirəm. Bəzilərini adam yerinə qoydum, indi gəl tap görün necə tapırsan✊','Ayə biri bunu aparsın🫢','Əgər bu həyatda öz tayını tapa bilmirsənsə üzülmə, deməli sən tayı bərabəri olmayan birisən.Qabriel Qarsia Markuez (Meksikalı yazıçı)🥲','Xoş Gəldim Nəfəs🥲','Gəlmirsən Balaca😒','Kimə Yazısan??? 🤨','Çirkin Çocuq Gəl😌','Cikolatam😍','Aaa Səndə Burdasan😳','Al Sənə Çikolata🤓👉🍫','Sevmirsən Məni?🙁 Onda Ol🙂','Haa Düz derisən?🧐','Bu Kimdir😁','Gəl Dava Edəx😁💪','Bax Sənə Nə Aldım😌👉🐒','Nə Gözəlsən🤢 Çirkin Ördək Yavrusu','Sən Kimsən🙄A Gədə👀','Gəl Sənə Sürpürüzüm var🤫','Ooo Çox Gözəlsin🤌🤐Bal','Şəxsiyə Yaz😌dünbələx','Gəl Görüm Hələ🧐 Nə demisən Mənə😬','Ayib Olsun😫 Niyə Yazmırsan😑','Bezdim Səndən🥲','Bu Neçədir✌️🙂','Nömrəni ver də Vpda yazışa🙊','👉👀 Gözün Çıxsın gəl😒','ımmm Gəl yogo yapalım🧘‍♀🤭','gəl sənə bıra süzdüm😪🍻','Ağlımı Başımdan ala şəxs😵‍💫gəl mənə doğru','Səni gördüm qızmam qalxdə🤒',) 

@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
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
      usrtxt += f"↯ [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Tag əməliyyatı uğurla dayandırıldı!**")
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
      usrtxt += f"↯ [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

bayrag = ['🏳️‍🌈','🏳️‍⚧️','🇦🇫','🇦🇽','🇦🇱','🇩🇿','🇦🇸','🇦🇩','🇦🇴','🇦🇮','🇦🇶','🇦🇬','🇦🇷','🇦🇲','🇦🇼','🇦🇺','🇦🇹','🇦🇿','🇧🇸','🇧🇭','🇧🇩','🇧🇧','🇧🇾','🇧🇪','🇧🇿','🇧🇯','🇧🇲','🇧🇹','🇧🇴','🇧🇦','🇧🇼','🇧🇷','🇻🇬','🇧🇳','🇧🇬','🇧🇫','🇧🇮','🇰🇭','🇨🇲','🇨🇦','🇮🇨','🇨🇻','🇧🇶','🇰🇾','🇨🇫','🇹🇩','🇮🇴','🇨🇱','🇨🇳','🇨🇽','🇨🇨','🇨🇴','🇰🇲','🇨🇬','🇨🇩','🇨🇰','🇨🇷','🇨🇮','🇭🇷','🇨🇺','🇨🇼','🇨🇾','🇨🇿','🇩🇰','🇩🇯','🇩🇲','🇩🇴','🇪🇨','🇪🇬','🇸🇻','🇬🇶','🇪🇷','🇪🇪','🇪🇹','🇸🇿','🇪🇺','🇫🇰','🇫🇴','🇫🇯','🇫🇮','🇫🇷','🇬🇫','🇵🇫','🇹🇫','🇬🇦','🇬🇲','🇬🇪','🇩🇪','🇬🇭','🇬🇮','🇬🇷','🇬🇱','🇬🇩','🇬🇵','🇬🇺','🇬🇹','🇬🇬','🇬🇳','🇬🇼','🇬🇾','🇭🇹','🇭🇳','🇭🇰','🇭🇺','🇮🇸','🇮🇳','🇮🇩','🇮🇷','🇮🇶','🇮🇪','🇮🇲','🇮🇱','🇮🇹','🇯🇲','🇯🇵','🎌','','🇯🇪','🇯🇴','🇰🇿','🇰🇪','🇰🇮','🇽🇰','🇰🇼','🇰🇬','🇱🇦','🇱🇻','🇱🇧','🇱🇸','🇱🇷','🇱🇾','🇱🇮','🇱🇹','🇱🇺','🇲🇴','🇲🇬','🇲🇼','🇲🇾','🇲🇻','🇲🇱','🇲🇹','🇲🇭','🇲🇶','🇲🇷','🇲🇺','🇾🇹','🇲🇽','🇫🇲','🇲🇩','🇲🇨','🇲🇳','🇲🇪','🇲🇸','🇲🇦','🇲🇿','🇲🇲','🇳🇦','🇳🇷','🇳🇵','🇳🇱','🇳🇨','🇳🇿','🇳🇮','🇳🇪','🇳🇬','🇳🇺','🇳🇫','🇰🇵','🇲🇰','🇲🇵','🇳🇴','🇴🇲','🇵🇰','🇵🇼','🇵🇸','🇵🇦','🇵🇬','🇵🇾','🇵🇪','🇵🇭','🇵🇳','🇵🇱','🇵🇹','🇵🇷','🇶🇦','🇷🇪','🇷🇴','🇷🇺','🇷🇼','🇼🇸','🇸🇲','🇸🇹','🇸🇦','🇸🇳','🇷🇸','🇸🇨','🇸🇱','🇸🇬','🇸🇽','🇸🇰','🇸🇮','🇬🇸','🇸🇧','🇸🇴','🇿🇦','🇰🇷','🇸🇸','🇪🇸','🇱🇰','🇧🇱','🇸🇭','🇰🇳','🇱🇨','🇵🇲','🇻🇨','🇸🇩','🇸🇪','🇸🇷','🇨🇭','🇸🇾','🇹🇼','🇹🇯','🇹🇿','🇹🇭','🇹🇱','🇹🇬','🇹🇰','🇹🇴','🇹🇹','🇹🇳','🇹🇷','🇹🇲','🇹🇨','🇹🇻','🇺🇬','🇺🇦','🇦🇪','🇬🇧','🏴󠁧󠁢󠁥󠁮󠁧󠁿','🏴󠁧󠁢󠁳󠁣󠁴󠁿','🏴󠁧󠁢󠁷󠁬󠁳󠁿','🇺🇸','🇺🇾','🇻🇮','🇺🇿','🇻🇺','🇻🇦','🇻🇪','🇻🇳','🇼🇫','🇪🇭','🇾🇪','🇿🇲','🇿🇼',]

@client.on(events.NewMessage(pattern="^/ftag ?(.*)"))

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
      usrtxt += f"↯ [{random.choice(futbol)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
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
      usrtxt += f"↯ [{random.choice(futbol)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

futbol = ('Maldonado', 'Lionel Messi', 'Bobô', 'Matías Delgado', 'Márcio Nobre1', 'Rodrigo Tello', 'Federico Higuaín', 'Lamine Diatta', 'Édouard Cissé', 'Gordon Schildenfeld', 'Filip Hološko', 'Anthony Šerić', 'Tomáš Sivok', 'Tomáš Zápotočný', 'Fabian Ernst', 'Michael Fink', 'Matteo Ferrari', 'Rodrigo Tabata', 'Ricardo Quaresma', 'Roberto Hilbert', 'Guti', 'Marco Aurélio1', 'Manuel Fernandes', 'Simao Sabrosa', 'Hugo Almeida', 'Sidnei', 'Bébé', 'Júlio Alves', 'Edú', 'Julien Escudé', 'Allan McGregor', 'Dentinho', 'Mamadou Niang', 'Pedro Franco', 'Michael Eneramo', 'Atiba Hutchinson', 'Ramon Motta', 'Jermaine Jones', 'Dany Nounkeu', 'Demba Ba', 'José Sosa', 'Alexander Milošević', 'Daniel Opare', 'Duško Tošić', 'Andreas Beck', 'Luiz Rhodolfo', 'Mario Gómez', 'Denis Boyko', 'Aras Özbiliz', 'Alexis Delgado', 'Marcelo Guedes', 'Fabri', 'Adriano Correia', 'Talisca', 'Vincent Aboubakar', 'Ryan Babel', 'Matej Mitrović', 'Pepe', 'Álvaro Negredo', 'Jeremain Lens', 'Gary Medel', 'Cyle Larin', 'Vágner Love', 'Domagoj Vida', 'Enzo Roco', 'Loris Karius', 'Adem Ljajić', 'Nicolas Isimat-Mirin', 'Shinji Kagawa', 'Tyler Boyd', 'Douglas', 'Víctor Ruiz', 'Pedro Rebocho', "Georges-Kévin N'Koudou", 'Muhammed Elneni', 'Abdoulay Diaby', 'Ajdin Hasić', 'Kevin-Prince Boateng', "Fabrice N'Sakala", 'Bernard Mensah', 'Welinton', 'Francisco Montero', 'Josef de Souza', 'Valentin Rosier', 'Raşit Gezzal', 'Alex Teixeira', 'Michy Batshuayi', 'Miralem Pjanić', 'Gedson Fernandes', 'Romain Saïss', 'Mert Günok', 'Ersin Destanoğlu', 'Emre Bilgin', 'Goktug Baytekin', 'Domagoj Vida', 'Welinton', 'Douglas', 'Fabrice NSkala', 'Umut Meras', 'Francisco Montero', 'Valentin Rosier', 'Kerem Kalafat', 'Rıdvan Yılmaz', 'Serdar Saatçi', 'Serkan Emrecan Terzi', 'Aytug Batur Komec', 'Atiba Hutchinson', 'Mehmet Topal', 'Miralem Pjanic', 'Adem Ljajic', 'Alex Teixeira', 'Necip Uysal', 'Gökhan Töre', 'Rachid Ghezzal', 'Oğuzhan Özyakup', 'Georges-Kevin Nkoudou', 'Muhayer Oktay', 'Can Bozdogan', 'Berkay Vardar', 'Emirhan İlkhan', 'Emirhan Delibas', 'Demir Tiknaz', 'Jeremain Lens', 'Michy Batshuayi', 'Kenan Karaman', 'Cyle Larin', 'Güven Yalçın', 'Koray Yagci', 'Ariel Ortega', 'Robert Enke', 'Vladimir Beschastnykh', 'Ivaylo Petkov', 'Sergiy Rebrov', 'Stjepan Tomas', 'Pierre van Hooijdonk', 'Marco Aurelio', 'Fábio Luciano', 'Mert Nobre', 'Fabiano', 'Alex De Souza', 'Stephen Appiah', 'Nicolas Anelka', 'Mateja Kežman', 'Edu Dracena', 'Diego Lugano', 'Deivid', 'Roberto Carlos', 'Wederson', 'Claudio Maldonado', 'Josico', 'Daniel Güiza', 'Fábio Bilica', 'André Santos', 'Cristian Baroni', 'Miroslav Stoch', 'Issiar Dia', 'Mamadou Niang', 'Joseph Yobo', 'Emmanuel Emenike', 'Reto Ziegler', 'Henri Bienvenu', 'Moussa Sow', 'Dirk Kuyt', 'Miloš Krasić', 'Raul Meireles', 'Pierre Webó', 'Bruno Alves', 'Michal Kadlec', 'Samuel Holmén', 'Diego', 'Simon Kjær', 'Fernandão', 'Abdoulaye Ba', 'Fabiano Ribeiro', 'Nani', 'Josef de Souza', 'Robin van Persie', 'Lazar Marković', 'Aatif Chahechouhe', 'Gregory van der Wiel', 'Roman Neustädter', 'Martin Škrtel', 'Jeremain Lens', 'Oleksandr Karavayev', 'Mathieu Valbuena', 'Nebil Dirar', 'Carlos Kameni', 'Mauricio Isla', 'Elif Elmas', 'Roberto Soldado', 'Giuliano', 'Luís Neto', 'Vincent Janssen', 'André Ayew', 'Islam Slimani', 'Michael Frey', 'Diego Reyes', 'Jailson', 'Yassine Benzia', 'Victor Moses', 'Miha Zajc', 'Max Kruse', 'Allahyar Seyyadmeneş', 'Vedat Muriqi', 'Garry Rodrigues', 'Zanka', 'Adil Rami', 'Luiz Gustavo', 'Simon Falette', 'Filip Novák', 'Mame Thiam', 'José Sosa', 'Mauricio Lemos', 'Enner Valencia', 'Marcel Tisserand', 'Mbwana Samatta', 'Papiss Cissé', 'Kemal Ademi', 'Dimitris Pelkas', 'Diego Perotti', 'Attila Szalai', 'Bright Osayi-Samuel', 'Mesut Özil', 'Steven Caulker', 'Kim Min-jae', 'Diego Rossi', 'Mërgim Berisha', 'Max Meyer', 'Miguel Crespo', 'Erol Bulut', 'Saffet Akbaş', 'Tayfun Korkut', 'Elvir Bolić', 'Mustafa Doğan', 'Samuel Johnson', 'Abdullah Ercan', 'Ogün Temizkanoğlu', 'Semih Şentürk', 'Ali Güneş', 'Serhat Akın', 'Ümit Özat', 'Volkan Demirel', 'Tuncay Şanlı', 'Selçuk Şahin', 'Fabio Luciano', 'Mehmet Yozgatlı', 'Mehmet Aurelio', 'Serkan Balcı', 'Önder Turacı', 'Uğur Boral', 'Gökhan Gönül', 'Gökçek Vederson', 'Colin Kâzım Richards', 'Emre Belözoğlu', 'Mehmet Topuz', 'Bekir İrtegün', 'Caner Erkin', 'Hasan Ali Kaldırım', 'Mehmet Topal', 'Alper Potuk', 'Şener Özbayraklı', 'Ozan Tufan', 'Aykut Erçetin', 'Çağlar Birinci', 'Gökhan Zan', 'Ceyhun Gülselam', 'Aydın Yılmaz', 'Selçuk İnan', 'Johan Elmander', 'Felipe Melo', 'Dida', 'Cafu', 'Stam', 'Nesta', 'Maldini', 'Pirlo', 'Gattuso', 'Seedorf', 'Kaka', 'Shevchenko', 'Inzaghi', 'Crespo', 'Diego Altube', 'Thibaut Courtois', 'Alphonse Areola', 'Andriy Lunin', 'Lucas Canizares', 'Luis Lopez', 'Toni Fuidias', 'Diego Del Alamo', 'Luis Federico', 'Sergio Ramos', 'Raphael Varane', 'Daniel Carvajal', 'Adrian De La Fuente', 'Ferland Mendy', 'Marcelo', 'Eder Militao', 'Alvaro Odriozola', 'Victor Chust', 'Sergio Santos', 'Pablo Ramon Parra', 'Miguel Gutierrez', 'David Alaba', 'Jesus Vallejo', 'Rafa Marin', 'Mario Gila', 'Reinier', 'Marco Asensio', 'Federico Valverde', 'Brahim Diaz', 'Luka Modric', 'Toni Kroos', 'Isco', 'Carlos Casemiro', 'Lucas Vazquez', 'Martin Odegaard', 'Marvin Park', 'Sergio Arribas', 'Antonio Blanco', 'Hugo Duro', 'Eduardo Camavinga', 'Dani Ceballos', 'Peter Gonzalez', 'Karim Benzema', 'Luka Jovic', 'Eden Hazard', 'Gareth Bale', 'Vinicius Junior', 'Rodrygo', 'James Rodriguez', 'Mariano Diaz', 'Borja Mayoral', 'Oscar Aranda', 'Juan Latasa', 'Neto', 'Marc-Andre Ter Stegen', 'Inaki Pena', 'Arnau Tenas', 'Lazar Carevic', 'Jordi Alba', 'Sergi Roberto', 'Ronald Araujo', 'Samuel Umtiti', 'Nelson Semedo', 'Clement Lenglet', 'Dani Morer', 'Junior Firpo', 'Gerard Pique', 'Sergio Akieme', 'Santiago Ramos', 'Arnau Comas', 'Sergino Dest', 'Oscar Mingueza', 'Eric Garcia', 'Emerson', 'Alejandro Balde', 'Dani Alves', 'Mika Marmol', 'Sergio Busquets', 'Hiroki Abe', 'Alex Collado', 'Frenkie De Jong', 'Ivan Rakitic', 'Arturo Vidal', 'Riqui Puig', 'Guillem Jaime', 'Miralem Pjanic', 'Philippe Coutinho', 'Carles Alena', 'Konrad De La Fuente', 'Ilaix Moriba', 'Matheus Fernandes', 'Yusuf Demir', 'Nico Gonzalez', 'Abde Ezzalzouli', 'Alvaro Sanz', 'Ferran Jutgla', 'Matheus Pereira', 'Lucas De Vega', 'Estanis Pedrola', 'Adama Traore', 'Luis Suarez', 'Ousmane Dembele', 'Antoine Griezmann', 'Ansu Fati', 'Lionel Messi', 'Rey Manaj', 'Martin Braithwaite', 'Memphis Depay', 'Sergio Agüero', 'Luuk De Jong', 'Ilias Akhomach', 'Ferran Torres', 'Pierre Aubameyang', 'Albert Riera', 'Milan Baroš', 'Tomáš Ujfaluši', 'Mehmet Batdal', 'Serkan Kurtuluş', 'Yiğit Gökoğlan', 'Hakan Balta', 'Fernando Muslera', 'Semih Kaya', 'Emmanuel Eboué', 'Yekta Kurtuluş', 'Engin Baytar', 'Emre Çolak', 'Sabri Sarıoğlu', 'Servet Çetin', 'Necati Ateş', 'Ufuk Ceylan', 'Sercan Yıldırım', 'Fernando Muslera', 'Felipe Melo', 'Hamit Altıntop', 'Gökhan Zan', 'Blerim Džemaili', 'Aydın Yılmaz', 'Selçuk İnan', 'Umut Bulut', 'Wesley Sneijder', 'Bruma', 'Alex Telles', 'Burak Yılmaz', 'Sinan Gümüş', 'Goran Pandev', 'Aurélien Chedjou', 'Fernando Muslera', 'Mariano', 'Maicon', 'Serdar Aziz', 'Ahmet Çalık', 'Tolga Ciğerci', 'Yasin Öztekin', 'Selçuk İnan', 'Eren Derdiyok', 'Younès Belhanda', 'Sinan Gümüş', 'Martin Linnes', 'Ryan Donk', 'Cédric Carrasso', 'Şener Özbayraklı', 'Omar Elabdellaoui', 'Taylan Antalyalı', 'Henry Onyekuru', 'Ryan Babel', 'Radamel Falcao', 'Halil Dervişoğlu', 'Oghenekaro Etebo', 'Martin Linnes', 'Ryan Donk', 'Oğulcan Çağlayan', 'Kerem Aktürkoğlu', 'Ömer Bayram', 'Emre Akbaba', 'Cristiano Ronaldo', 'Pele', 'Maradona', 'Ronaldo', 'Thierry Henry', 'Kaka', 'Sergio Agüero', 'Xavi', 'Ruud Gullit', 'Arthur Zico', 'Lev Yashin', 'Iniesta', 'Lothar Matthäus', 'Giuseppe Meazza', 'Franz Beckenbauer', 'George Best', 'Roberto Baggio', 'Johan Cruyff', 'Luis Figo', 'Andrea Pirlo', 'Marco Van Basten', 'Zlatan Ibrahimovic', 'Sandro Mazzola', 'Ferenc Puskas', 'Zinedine Zidane', 'Alfredo Di Stéfano', 'Rio Ferdinand', 'Paolo Maldini', 'Robin van Persie', 'Iker Casillas', 'Neymar', 'Fabio Cannavaro', 'Yaya Toure', 'Edinson Cavani', 'Gabriel Batistuta', 'Thiago Silva', 'Dennis Bergkamp', 'Franck Ribery', 'Carles Puyol', 'Mesut Özil', 'Dani Alves', 'David Silva', 'Karim Benzema', 'Javier Zanetti', 'Radamel Falcao', 'Bastian Schweinsteiger', 'Gianluigi Buffon', 'Arjen Robben', 'Wayne Rooney', 'Luis Suarez', 'Mbappe', 'Juan Román Riquelme', 'Sergio Ramos', 'Muhammed Salah', 'Cesc Fabregas', 'Gerard Pique', 'Pepe', 'Didier Drogba', 'Robert Lewandowski', 'David Villa', 'Wesley Sneijder', 'Philipp Lahm', "Samuel Eto'o", 'Carlos Tevez', 'Sergio Busquets', 'Samir Nasri', 'Eden Hazard', 'Diego Forlan', 'Klaas Jan Huntelaar', 'Sabri Sarıoğlu')
 

@client.on(events.NewMessage(pattern="^/mafia ?(.*)"))

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
      usrtxt += f"↯ [{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
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
      usrtxt += f"↯ [{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

mafia = (
"Sənin oyundakı rolun 👮🏼 Çavuş!",
"Sənin oyundakı rolun 🐺 Oboroten!",
"Sənin oyundakı rolun 🤓 Satqın!",
"Sənin oyundakı rolun 💃 Məşuqə!",
"Sənin oyundakı rolun 🤵🏼 Mafia!",
"Sənin oyundakı rolun 🧙‍ Maq!",
"Sənin oyundakı rolun 🤞🏼 Şanslı Vətəndaş!",
"Sənin oyundakı rolun 💣 Kamikadze!",
"Sənin oyundakı rolun 👩🏼‍💻 Jurnalist!",
"Sənin oyundakı rolun 🤹🏻 Aferist!",
"Sənin oyundakı rolun 👨🏼 Vətəndaş!",
"Sənin oyundakı rolun 🕵🏼 Komissar Kattani!",
"Sənin oyundakı rolun 🎖 Mer!",
"Sənin oyundakı rolun 🔪 Manyak!",
"Sənin oyundakı rolun 👨🏼‍⚕️️Doktor!",
"Sənin oyundakı rolun 🤵🏻 Don!",
"Sənin oyundakı rolun 🧙🏼 Bomj!",
"Sənin oyundakı rolun 👨🏼‍💼 Vəkil!",
"Sənin oyundakı rolun 🧟 Arsonist!",
"Sənin oyundakı rolun 🕴️ Qatil!",
"Sənin oyundakı rolun 🧝🏻‍♀️Şəhzadə!",
"Sənin oyundakı rolun 🧟‍♀️Cadugar!",
"Sənin oyundakı rolun 🧛🏻‍♂️Vampir!",
"Sənin oyundakı rolun 🧚🏻‍♀️Mələk!",
"Sənin oyundakı rolun 🦹🏻‍♂️BOSS!",
"Sənin oyundakı rolun 🦦Köstəbək!",
"Sənin oyundakı rolun 🦎Buqələmun!",
"Sənin oyundakı rolun 🤡Joker!",
"Sənin oyundakı rolun 🙍🏻‍♂️Məhbus!",
"Sənin oyundakı rolun 🙇🏻‍♂️Oğru!",
"Sənin oyundakı rolun 🕵️Suiqəstçi!",
"Sənin oyundakı rolun 🔮Reviver!",
"Sənin oyundakı rolun 👷🏻‍♂️Mədənçi!",
"Sənin oyundakı rolun 💂Killer!",
"Sənin oyundakı rolun 👻Ruh!",
"Sənin oyundakı rolun 👳🏻‍♂️Satıcı!",
"Sənin oyundakı rolun 👨🏻‍🦱Dedektiv!",
"Sənin oyundakı rolun  👨🏻‍🎤Specialist!",
"Sənin oyundakı rolun ⭐️General!",
"Sənin oyundakı rolun 🥷Ninja!"
)

@client.on(events.NewMessage(pattern="^/adtag ?(.*)"))

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
      usrtxt += f"↯ [{random.choice(ad)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! **")
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
      usrtxt += f"↯ [{random.choice(ad)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Əməliyyat Uğurla Dayandırıldı! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

ad = ['Üzümlü kek ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu panda 🐼', 'Ay pare 🌛', 'Ballı lokma ✨', 'Lale 🌷', 'Ahtapot 🐙', 'Zambak ⚜️', 'Akasya 🌿', 'Akşam Sefası 🌛', 'Begonvil 🥀', 'Begonya 🪴', 'Bambu 🎍', 'Fesleğen 🌿', 'Kasımpatı 🌸', 'Manolya 🌾', 'Boncuk 🧿', 'Badem 🥭', 'Minnoş 🐹', 'Ponçik 🐣', 'Pofuduk 🐼', 'Unicorn 🦄', 'Karamel 🍫', 'Fındık 🌰', 'Fıstık 🥜', 'Pamuk ☁️', 'Minnoş 🥰', 'Zeytin 🫒', 'Afrodit 🧚🏻', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare 🌺', 'Reyhan 🌷', 'Kaktüs 🌵', 'Buket 💐', 'Başak 🌾', 'Kar Tanesi ❄️', 'Tospik 🐢', 'Kelebek 🦋', 'Tavşan 🐰', 'Şeker 🍬', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği 🌻', 'Tweety 🐥', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨']

@client.on(events.NewMessage(pattern='/offline'))
async def handler(event):
    # Kimsə "Salam" və başqa bir şey deyəndə cavab verin
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("Sən mənim sahibim deyilsən😒")
    await event.reply('Bot Mükəmməl İşləyir 🚀',
         buttons=(
               [Button.url('🔮 Kanalım','https://t.me/TEAMABASOFcom'),
               Button.url('🇦🇿 Reklam','https://t.me/oldtaggerReklam')],
                    ),
                    link_preview=False)


#pyrogram
@app.on_message(filters.command("info"))
async def info(bot, update):
    
    text = f"""--**Information**--

**🙋🏻‍♂️ AD :** {update.from_user.first_name}
**🧖‍♂️ Szin Soy Adınız :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**🧑🏻‍🎓 Sizin Username :** {update.from_user.username}
**🆔 Sizin Telegram ID :** {update.from_user.id}
**🔗 Sizin Profile Linkiniz :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )



#mahnı yükləmə#

@app.on_message(filters.command("song") & ~filters.edited)
def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>Mahnınız Axtarılır ... 🔍</b>")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("<b>❌ Bunu deməliyəm üzürlü say 😔 mahnı tapılmadı.\n\n Zəhmət Olmasa başqa mahnı adı deyin @oldsupport 🍷.</b>")
        print(str(e))
        return
    m.edit("<b>📥 Yükləmə Prosesi Başladı...</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**╭───────────────**\n**├▷ ♬ Adı: [{title[:35]}]({link})**\n**├───────────────**\n**├▷🤍 BOT @OldMultiBot**\n**╰───────────────**"
        res = f"**╭───────────────**\n**├▷ ♬ Adı: [{title[:35]}]({link})**\n**├───────────────**\n**├▷👤 İstəyən** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n**├───────────────**\n**├▷🌀 Bot: @{Config.BOT_USERNAME}**\n**╰───────────────**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("📤 Yüklenir..")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="@OldMultiBot")
        m.delete()
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=res, performer="@AzeSongRobot", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit("<link Xətanın, düzelmesini gözləyin.</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)




#Pyrogram comand
@app.on_message(filters.command("zer"))
async def roll_dice(bot, message):
    await bot.send_dice(message.chat.id, "🎲")

@app.on_message(filters.command("ox"))                                      
async def roll_arrow(bot, message):
    await bot.send_dice(message.chat.id, "🎯")

@app.on_message(filters.command("gol"))
async def roll_goal(bot, message):
    await bot.send_dice(message.chat.id, "⚽️")

@app.on_message(filters.command("spin"))
async def roll_luck(bot, message):
    await bot.send_dice(message.chat.id, "🎰")

@app.on_message(filters.command("basket"))
async def roll_throw(bot, message):
    await bot.send_dice(message.chat.id, "🏀")

@app.on_message(filters.command(["bowling", "tenpins"]))
async def roll_bowling(bot, message):
    await bot.send_dice(message.chat.id, "🎳") 

### Quiz command
@client.on(events.NewMessage(pattern='/(?i)quiz')) 
async def quiz(event):
    # get the sender
    sender = await event.get_sender()
    SENDER = sender.id

    # Start a conversation
    async with client.conversation(await event.get_chat(), exclusive=True) as conv:
        # get two random numbers between 1 and 10
        rand1 = randint(1,10)
        rand2 = randint(1,10)
        # make the sum
        sum = rand1+rand2
        # make another sum based on two different random numbers. This will be used for the wrong option
        sum_not_true = randint(1,10) + randint(1,10)

        # To make the position of the button random, let's define two keyboard that activates with 50% probability
        if(bool(random.getrandbits(1))):
            keyboard = [[Button.inline("{}".format(sum), sum)], [Button.inline("{}".format(sum_not_true), sum_not_true)]]
        else:
            keyboard = [[Button.inline("{}".format(sum_not_true), sum_not_true)],[Button.inline("{}".format(sum), sum)]]

        text = "<b>OLD MULTI</b> 🤖\n{} + {} = ?\n".format(str(rand1), str(rand2))
        await conv.send_message(text, buttons=keyboard, parse_mode='html')
        press = await conv.wait_event(press_event(SENDER))
        choice = str(press.data.decode("utf-8"))

        if(choice == str(sum)):
            await conv.send_message("Correct Answer!", parse_mode='html')
        else:
            await conv.send_message("Nope, i won!", parse_mode='html')

        await conv.cancel_all()
        return 
 

#telethon xos geldin mesaj 
@client.on(events.ChatAction) 
async def handler(event): # Welcome every new user 
    if event.user_joined: 
       await event.reply('Salam xos geldiniz groupa!')


#pyrogram telegrap
@app.on_message(filters.private & filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`YÜKLƏNİR GÖZLƏYİN`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`YENİLENİR GÖZLƏYİN.....`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@app.on_message(filters.private & filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`YÜKLƏNİR GÖZLƏYİN`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`YENİLENİR GÖZLƏYİN.....`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@app.on_message(filters.private & filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`YÜKLƏNİR GÖZLƏYİN`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`YENİLENİR GÖZLƏYİN.....`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")


  
#@client.on(events.NewMessage(pattern='/reklam'))
#async def handler(event):	
 #    await event.reply('🤖 [USTA Tag Bot](http://t.me/UstaTagbot)-unda Reklam Almaq Üzçün [ɴᴀᴋʜɪᴅ ᴜsᴛᴀ ¦ 🇧🇻🦅](https://t.me/UstaNakhid)-ilə Әlaqә Saxlayın.')
 

print(">> Bot işləyir narahat olmayın. @edalet_22 Məlumat almaq üçün <<")
app.start()
client.run_until_disconnected()
