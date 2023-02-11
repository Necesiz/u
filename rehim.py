from pyrogram import Client, filters
from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



#-#-#-# Pyrogram Başlanğıc #-#-#-#
rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)

@rehim.on_message(filters.command("start"))
async def hello(client, message): 
    await message.reply("Hello from Pyrogram!")



@rehim.on_message(filters.command("botlist"))
def botlist(client, message):
    bots = [     # List of Bots
        {
            "name": "Besty",
            "username": "BestyBot"
        },
        {
            "name": "Robbie",
            "username": "RobbieBot"
        },
        {
            "name": "Cally",
            "username": "CallyBot"
        }
    ]
    response_text = ""
    for bot in bots:
        response_text += f"{bot['name']}: @{bot['username']}\n"
    message.reply(response_text)


adminList = ['teamabasov', 'anonyumaz', 'anonyumAzbot']

def get_admin_list():
  return adminList

@rehim.on_message(filters.command(["adminlist"]))
def adminlist(client, message):
  text = f"The current admins are: {', '.join(get_admin_list())}"
  client.send_message(
    chat_id=message.chat.id, 
    text=text, 
    reply_to_message_id=message.message_id
  )






rehim.run()
