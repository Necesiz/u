import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("23860620"))
    API_HASH = os.environ.get("347c94d92d0bbcfbc223651b73d71345")
    BOT_TOKEN = os.environ.get("5740066159:AAElPxUgEPtC7aJbAkFpSIFcwzVPoA9IeBA")
    BOT_USERNAME = os.environ.get("oldtaggerbot")
    BOT_NAME = os.environ.get("OLD TAGGER")
    BOT_ID = int(os.environ.get("5740066159"))
    SUDO_USERS = os.environ.get("5508658149").split()
    SUPPORT_CHAT = os.environ.get("oldtaggersup1")
    OWNER_ID = int(os.environ.get("5508658149"))
    OWNER_USERNAME = os.environ.get("oldteamabasof")
    IMG_1 = os.environ.get("IMG_1", "https://telegra.ph/file/cce7cc0f861e755ab775e.jpg")
