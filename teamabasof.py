from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime
import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrobot import COMMAND_HAND_LER, TG_MAX_SELECT_LEN
from pyrobot.helper_functions.cust_p_filters import admin_fliter

app = Client(
    "OLD-TAGGER-BOT",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

@app.on_message(filters.command("start"))
async def _py(client: Client, message: Message):
    await message.reply_text('Pyrogram is a Python library for Telegram bots.')

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Hey` {msg.from_user.mention} `beni` {msg.chat.title} `grubuna eklediğin için teşekkürler⚡️`\n\n**Grublarda 10k yakın üye etiketleme özelliğim vardır komutlar için /help yazmanız yeterlidir✨**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('İşte bu gelen benim sahibim.')


@app.on_message(filters.command("alive") & filters.user(Config.OWNER_ID))
async def live(client: Client, message: Message):
    livemsg = await message.reply_text('`Salam Sahibim Mən Aktiv Olaraq Çalışıram 💎`')            

            
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
