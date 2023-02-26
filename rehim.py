from telethon import TelegramClient
from telethon import events

#pyrogram

from pyrogram import Client, filters


from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)


@rehim.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")
			
    
#TELETHON SETRİ

abasov = TelegramClient('abasov', api_id, api_hash).start(bot_token=bot_token)

@abasov.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(random.choice(userjoin))


@abasov.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply("Davay gelme day")

userjoin = (

    "Xoş gəlmisininiz",
    "",
)




print(">> Bot işləyir <<")
rehim.run()
abasov.run_until_disconnected()
