from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from Config import Config
from datetime import datetime


app = Client(
    "OLD-TAGGER-BOT",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)




@app.on_message(filters.command("info"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**İsdifadəçi İd'si:**\n"
    out_str += f" ⚡️ __Qrup İd'si__ : `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f" 🙋🏻‍♂️ __Cavab verən İstifadəçi Adı__ : {msg.from_user.first_name}\n"
    out_str += f" 💬 __Mesaj İd'si__ : `{msg.forward_from_message_id or msg.message_id}`\n"
    if msg.from_user:
        out_str += f" 🙋🏻‍♂️ __Cavab verən İstifadəçi İd'si__ : `{msg.from_user.id}`\n"

    await message.reply(out_str)
    
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
