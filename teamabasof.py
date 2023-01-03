import os
import sys
from pyrogram import Client, filters
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied
import asyncio
import random, re
from pyrogram.types import Message
from driver.filters import command
from pyrogram import Client, filters
from os import system, execle, environ
from Teamabasof.decorators import sudo_users_only
from git.exc import InvalidGitRepositoryError
from varabiles import UPSTREAM_REPO, BOT_USERNAME

ydl_opts = {
    'format': 'best',
    'keepvideo': True,
    'prefer_ffmpeg': False,
    'geo_bypass': True,
    'outtmpl': '%(title)s.%(ext)s',
    'quite': True
}  
  
app = Client(
    "OLD-TAGGER-BOT",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="💞 SUPPORT", url=f"https://t.me/oldsupport")]])


@app.on_message(filters.command("start"))
async def _py(client: Client, message: Message):
    await message.reply_text('Pyrogram is a Python library for Telegram bots.')

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `Məni` {msg.chat.title} `qrubuna əlavə etdiyin üçün təşəkkürlər⚡️`\n\n**Qruplarda 10k yaxın user tag prosesi edə bilirəm komutlar için /help yazmanız yetərlidir✨**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('İşte bu gelen benim sahibim.')


@app.on_message(filters.command("alive") & filters.user(Config.OWNER_ID))
async def live(client: Client, message: Message):
    livemsg = await message.reply_text('`Salam Sahibim Mən Aktiv Olaraq Çalışıram 💎`')            


@app.on_message(filters.command("id"))
async def id(bot, update):
    await update.reply_text(        
        text=f"💞 **Sizin Telegram idiniz :** {update.from_user.id}",
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )
    

@app.on_message(filters.command("info"))
async def info(bot, update):
    
    text = f"""--**OLD TAGGER MELUMAT**--
**💞 AD :** {update.from_user.first_name}
**😎 İkinci adınız :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**🥳 İsdifadeçi Adınız :** {update.from_user.username}
**😜 Telegram ID :** {update.from_user.id}
**🤫 Profil Linkiniz :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )
    

@app.on_message(filters.command("zer"))
async def roll_dice(bot, message):
    await bot.send_dice(message.chat.id, "🎲")

@app.on_message(filters.command("ox"))                                      
async def roll_arrow(bot, message):
    await bot.send_dice(message.chat.id, "🎯")

@app.on_message(filters.command("goal"))
async def roll_goal(bot, message):
    await bot.send_dice(message.chat.id, "⚽️")

@app.on_message(filters.command("luck"))
async def roll_luck(bot, message):
    await bot.send_dice(message.chat.id, "🎰")

@app.on_message(filters.command("pota"))
async def roll_throw(bot, message):
    await bot.send_dice(message.chat.id, "🏀")

@app.on_message(filters.command(["bowling", "tenpins"]))
async def roll_bowling(bot, message):
    await bot.send_dice(message.chat.id, "🎳")


@app.on_message(filters.command("brain", ".") & filters.me)
async def pijtau(client: Client, message: Message):
    if message.forward_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    await message.edit("brain")
    animation_chars = [          
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
              "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
          ]
    for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await message.edit(animation_chars[i %14 ])


@app.on_message(filters.command("ping"))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄\n**Ping: {round(ms)}**")
 

@app.on_message(command(["restart", f"restart@OldMultiBot"]) & ~filters.edited)
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`bot yeniden basladilir...`")
    args = [sys.executable, "start"]
    await msg.edit("✅ bot yeniden basladılır\n\n• indi bu botu yenidən istifadə edə bilərsiniz.")
    execle(sys.executable, *args, environ)
    return
   
    

app.start()
print(f"Bot pyrogram ( {pyrogram.__version__} sürümü ile başlatıldı. ")
idle()
