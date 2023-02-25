import os
from os import environ

class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    admins = {}
    API_ID = int(os.environ.get("API_ID","15954332"))
    API_HASH = os.environ.get("API_HASH","85adea6f1eaf068b707703b4846a9ced")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5350952995:AAEnEMuabPz1jwXZY4lbZDHXOiH3hEblRuM")
    
