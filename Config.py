import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","8953338"))
    API_HASH = os.environ.get("API_HASH","fe21f223cb02d8f7c1cbda651f553a45")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5910888289:AAEe33s2DNAr_hG6fK0jcAKIeH4hbb6Y8z0")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "HusiRobot")
    BOT_NAME = os.environ.get("BOT_NAME", "Husi")
    BOT_ID = int(os.environ.get("BOT_NAME", "5910888289"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "5508658149").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Xiyar")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5508658149"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Husii")
    IMG_1 = os.environ.get("IMG_1", "https://telegra.ph/file/cce7cc0f861e755ab775e.jpg")
