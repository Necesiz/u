import pyrogram
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


@rehim.on_message(filters.private & filters.command("id"))
def userinfo(client, message):
    if message.text == "/id":
        user = rehim.get_users(message.from_user.id)
        client.send_message(
            chat_id=message.chat.id,
            text="Salam {0[first_name]}!\nSənin ID: {0[id]}".format(user),
            parse_mode="HTML"
        )



@rehim.on_message(filters.command("info"))
def userinfo(client, message): 
 user_id = message.chat.id # getting the user_id 
  
 user = app.get_users(user_id) # getting the user object 
 name = user.first_name + " " + user.last_name # name 
 username = user.username # username 
 bio = user.about # bio 
 is_verified = user.is_verified # is_verified 
 is_bot = user.is_bot # is_bot 
 photo = user.photo # photo 
 message.reply_text(f"Name: {name}\nUsername: {username}\nBio: {bio}\nis_verified: {is_verified}\nis_bot: {is_bot}\nPhoto: {photo}") 






rehim.run()
