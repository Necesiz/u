import re
import os
from os import environ

import variables

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5740066159:AAF358Qc2PKTQsFJoqcITBobgVyrIxJbV6c")

API_ID = int(os.environ.get("API_ID",15954332))

API_HASH = os.environ.get("API_HASH","85adea6f1eaf068b707703b4846a9ced")

ADMIN = os.environ.get("ADMIN", "5134595693")

DB_URL = os.environ.get("DB_URL", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DB_NAME", "music")
