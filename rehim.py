import pyrogram
import random
from pyrogram import Client, filters
from pyrogram import Client, emoji, filters
from Config import Config

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN



#-#-#-# Pyrogram Başlanğıc #-#-#-#
rehim = Client(":memory:", api_id, api_hash, bot_token=bot_token)







@rehim.on_message(filters.command("zer"))
def send_dice(client, message):
    result = random.randint(1, 6)
    dice = str(result)
    if message.chat.type in ["group", "supergroup"]:
        client.send_message(message.chat.id, f"{message.from_user.first_name} sanırım {dice} geldi!", parse_mode="html")


@rehim.on_message(filters.command('list'))
def chat_members(client, message):
    members = client.get_chat_members(message.chat.id)

    # Gruplardaki üyeleri listeleme
    text = "Gruptaki Üyeler:\n\n"
    for x in members:
        text += f"""\U0001f464 {x.user.username}\n"""
    message.reply_text(text)



# Target chat. Can also be a list of multiple chat ids/usernames
TARGET = -1001724090128
# Welcome message template
MESSAGE = "{} XOW GELDIN  [Pyrogram](https://t.me/rehimbottest)'SOHBET QROUPUNA {}!"




# Filter in only new_chat_members updates generated in TARGET chat
@rehim.on_message(filters.chat(TARGET) & filters.new_chat_members)
async def welcome(client, message):
    # Build the new members list (with mentions) by using their first_name
    new_members = [u.mention for u in message.new_chat_members]
    # Build the welcome message by using an emoji and the list we built above
    text = MESSAGE.format(emoji.SPARKLES, ", ".join(new_members))
    # Send the welcome message, without the web page preview
    await message.reply_text(text, disable_web_page_preview=True)




@rehim.on_message(filters.command(["promote"]))
def promote_member(client, message):
    if len(message.command) == 2:
        member_id = message.command[1]
        status = client.promote_chat_member(chat_id=message.chat.id, user_id=member_id)
        message.reply(f"{member_id} Başarıyla Yükseltildi.")







@rehim.on_message(filters.command("unpinall"))
def unpin_all_chat_messages(client, message):
    chat_id = message.chat.id
    client.unpin_all_chat_messages(chat_id)
    message.reply("Tüm mesajlar başarıyla unpin edildi.")



@rehim.on_message(filters.command('aye'))
def send_voice(client, message):
    rehim.send_voice(message.chat.id, voice='AwACAgQAAx0Cb5j5qAACITpj6VD0_jjbXkOZ307AwYF8rNw5UwACswIAAs0m_VKAQ7xZ5hdPpx4E', caption="Test")


@rehim.on_message(filters.command("rehim"))
async def hello(client, message): 
    await message.reply("NEDI EEEEEEEEEE!")



@rehim.on_message(filters.command("botlist"))
def botlist(client, message):
    bots = [     # List of Bots
        {
            "name": "OldMulti",
            "username": "OldMultiBot"
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
    if not message.reply_to_message: 
        message.reply("Lütfen bir mesaj yanıtlayarak pinleme yapın!") 
    else: 
        message.reply_to_message.pin() 
        message.reply("Mesajınız başarıyla pinlendi!") 





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





@rehim.on_message(filters.voice)
def anything(client, message):
    message.reply(message.voice.file_id)






rehim.run()
