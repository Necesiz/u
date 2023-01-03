import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    admins = {}
    API_ID = int(os.environ.get("API_ID","15954332"))
    API_HASH = os.environ.get("API_HASH","85adea6f1eaf068b707703b4846a9ced")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5964973513:AAF6yLfaKrz597y7mNwt3QIw-kHU1cthVBs")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "OldMultiBot")
    BOT_NAME = os.environ.get("BOT_NAME", "OLD MULTİ BOT 🤖")
    BOT_ID = int(os.environ.get("BOT_ID", "5964973513"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "5134595693").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "oldsupport")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5134595693"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "AnonyumAz")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME","azesongplaylist")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID",-1001852777229))
