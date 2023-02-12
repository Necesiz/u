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





@rehim.on_message(filters.command('info'))
def user_info(client, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else :
        user = message.from_user

    user_id = user.id 
    first_name = user.first_name 
    last_name = user.last_name 
    user_name = user.username
    language_code = user.language_code  

    message.reply_text(
        f"User ID : {user_id}\n"
        f"First Name : {first_name}\n"
        f"Last Name : {last_name}\n"
        f"User Name : {user_name}\n"
        f"Language Code : {language_code}"        
    )





@rehim.on_message(filters.command("ses"))
def get_voice(client, message):
    if message.audio:
        message.download_media(file_name="voice.ogg")
        print("Voice code saved.")





@Client.on_message(filters.command("ship"))
def ship(client, message):
    # Ship someone
    if message.text == "ship":
        # Find two people in the message
        users = message.mentions 
        if len(users) == 2:
            client.send_message(
                chat_id=message.chat.id, 
                text="{} and {} are now together!".format(
                    users[0].first_name, 
                    users[1].first_name
                )
            )
        else:
            client.send_message(
                chat_id=message.chat.id, 
                text="You need to mention two people to ship them!"
            )




@rehim.on_message(filters.command(["sil"]))
def delete_message(client, message):
    # silinecek mesajın ID'si
    message_to_delete = message.reply_to_message.message_id

    client.delete_messages(
        chat_id=message.chat.id,
        message_ids=message_to_delete
    )

    message.reply_text("Mesaj başarıyla silindi!")



@rehim.on_message(filters.text)
def text_delete(client, message):
    soz = ['sim','sikdir','göt','qəhbə']
    if message.text in soz:
        rehim.delete_messages(message.chat.id, message_ids=message.message_id)






rehim.run()
