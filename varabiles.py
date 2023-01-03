import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5964973513:AAGrzLdwqM1ZzcIKkvO4--vC8ZlqrsGb57s")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5134595693').split()]

FORCE_SUB = os.environ.get("FORCE_SUB", None)           













