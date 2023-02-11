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



@rehim.on_message(filters.command('pin'))
def pin_message(client, message):
    replied = message.reply_to_message
    if replied:
        client.pin_chat_message(message.chat.id, replied.message_id)
    else:
        message.reply("Lütfen cevaplayarak mesajınızı sabitlemeyi deneyin")




@rehim.on_message(filters.command("unpin"))
def unpin_message(client, message):
 reply_to = message.reply_to_message
 
 if reply_to != None:
  client.unpin_chat_message(message.chat.id, reply_to.message_id)
  client.send_message(message.chat.id, "Mesaj başarıyla kaldırıldı.")
 else:
  client.send_message(message.chat.id, "Bir mesaj seciniz")




@rehim.on_message(filters.command('fileid')) 
def fileid(client, message): 
    reply_text = "File ID: {}".format(message.document.file_id) 
    message.reply_text(reply_text) 




rehim.run()
