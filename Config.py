import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","15954332"))
    API_HASH = os.environ.get("API_HASH","85adea6f1eaf068b707703b4846a9ced")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5740066159:AAF358Qc2PKTQsFJoqcITBobgVyrIxJbV6c")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "oldtaggerbot")
    BOT_NAME = os.environ.get("BOT_NAME", "OLD TAGGER")
    BOT_ID = int(os.environ.get("BOT_ID", "5740066159"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "5134595693").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "oldsupport")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5134595693"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "AnonyumAz")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001737573985"))
    LANGUAGE = os.environ.get("LANGUAGE", "AZ")
    GONDERME_TURU = os.environ.get("GONDERME_TURU", "False")
    GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "oldsupport")
