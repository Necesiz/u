from pyrogram import Client, filters
from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



#-#-#-# Pyrogram Başlanğıc #-#-#-#
rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)

@rehim.on_message(filters.private)
async def hello(client, message): 
    await message.reply("Hello from Pyrogram!")









rehim.run()
