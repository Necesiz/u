import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

ADMIN = os.environ.get("ADMIN", "5134595693")
