import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "A3kon-CallMubot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "A3kon")
ALIVE_NAME = getenv("ALIVE_NAME", "Aekan")
BOT_USERNAME = getenv("BOT_USERNAME", "Aekmusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𓆰CALL MUSIC GIRL🎶")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Aeko500k")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SoalfLove")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8e659a7ee1cec74b1d942.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/A3EK/Call")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/643897a898c7d37ded7cb.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a4b71012dc158fc02eec7.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/767178105c88caa8a286c.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/353a8e168e4d65314d4b8.png")
