import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

ADMIN = os.environ.get("ADMIN", "5134595693")

DB_URL = os.environ.get("DB_URL", "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DB_NAME", "music")
