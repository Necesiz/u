import os
from os import getenv
admins = {}
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Teamabasof/OLD-TAGGER-BOT")
BOT_USERNAME = getenv("BOT_USERNAME", "OldMultiBot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
