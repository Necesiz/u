import os
from pyrogram import Client, filters
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied


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
    
    
@app.on_message(filters.command("restart") & filters.user(Config.OWNER_ID))
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply_text("`Bot yeniden basladilir...`")
        LOGGER(__name__).info("BOT serverde yeniden basladildi !!")
    except BaseException as err:
        LOGGER(oldtaggerlog).info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n")
    os.system(f"kill -9 {os.getpid()} && bash start")

    
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


@app.on_message(filters.command("ping"))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄\n**Ping: {round(ms)}**")
    
app.start()
print(f"Bot pyrogram ( {pyrogram.__version__} sürümü ile başlatıldı. ")
idle()
