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










@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(Config.BOT_ID):
            await msg.reply(
                f'''`Salam` {msg.from_user.mention} `Məni` {msg.chat.title} `Qrupa əlavə etdiyiniz üçün təşəkkürlər⚡️` \n\n **🤖Qruplardakı Userləri Tag Edmə üçün Yaradıldım.\n🤖Kömək üçün /help yazmaq kifayətdir.✨**''')

        elif str(new_user.id) == str(Config.OWNER_ID):
            await msg.reply('🤖 [𝕆𝕃𝔻 TAGGER BOT](https://t.me/oldtaggerBot)-un Sahibi, Qrupa Qatıldı.\n Xoş Gəldin  Aramıza Sahib, Necəsən?🥰.')




@app.on_message(filters.command("id"))
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