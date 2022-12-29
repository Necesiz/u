import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","15954332"))
    API_HASH = os.environ.get("API_HASH","85adea6f1eaf068b707703b4846a9ced")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5964973513:AAGZ0ly-qF0DS3--WKdggswTa7KpRZ35PzM")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "OldMultiBot")
    BOT_NAME = os.environ.get("BOT_NAME", "OLD MULTİ BOT 🤖")
    BOT_ID = int(os.environ.get("BOT_ID", "5964973513"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "5134595693").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "oldsupport")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5134595693"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "AnonyumAz")
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5134595693").split())]


ADMINS.extend((5134595693))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

