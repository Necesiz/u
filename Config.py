import os
from os import environ

class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    admins = {}
    API_ID = int(os.environ.get("API_ID","15954332"))
    API_HASH = os.environ.get("API_HASH","85adea6f1eaf068b707703b4846a9ced")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5740066159:AAEPcU0_CXKsRUynXCsl-lDVKlyMbq11hFc")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "oldtaggerbot")
    BOT_NAME = os.environ.get("BOT_NAME", "OLD TAGGER")
    BOT_ID = int(os.environ.get("BOT_ID", "5508658149"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "5134595693").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "oldsupport")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5134595693"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "AnonyumAz")
    GONDERME_TURU = os.environ.get("GONDERME_TURU","False")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL",-1001737573985))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mirge1:mirge1@cluster0.tebyent.mongodb.net/?retryWrites=true&w=majority")
    LANGAUGE = os.environ.get("LANGAUGE", "AZ")
    GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "TEAMABASOFcom")
    

