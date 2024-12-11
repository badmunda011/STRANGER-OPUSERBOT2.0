import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Setup Logging
logging.basicConfig(
    format="[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10),
        logging.StreamHandler(),
    ],
)

# Suppress noisy loggers
for module in ["apscheduler", "asyncio", "httpx", "pyrogram", "pytgcalls"]:
    logging.getLogger(module).setLevel(logging.ERROR)

LOGGER = logging.getLogger("SYSTEM")


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", 25742938))
API_HASH ="b35b715fe8dc0a58e8048988286fc5b6"
BOT_TOKEN ="7454086236:AAEY9IfwBZqV5KTvWkqYS_GGLa6SdKcCCAc"
STRING_SESSION ="BQGIzloACZocsvGOU9YrE3Ru2-HPg80fe_T4U20F_HZA44PqWEMdxsuLJFtpzfPJ6XAs4KzhbzNj6MZNW-M3AIVt90-G_QPhgWkiDFDiCyzSxn8m1OrdAyoGuvlf8w4DnHJ2CAw7V6nBsqjrl1ZZCpLdXBUqJp87ewBUX3PuSv2o3oyYwJji4JWNmr1AzZ1P0-H7Q0__9dFFk98WafLqwdqADCgd4GhzzYnvhX3cVWIDdE7YskN4CaoNl4QfSRUpgpkTzJos_qBWWwZ6YgorPbg3oN_trQy5C9gmQ33lEgrOvcjeRu5GTQ2xK5WQ7-xi6IkYsol16cbkG77-PEaw5lwa06CgGgAAAAF-_9otAA"
MONGO_DB_URL ="mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1002356967761))
OWNER_ID = int(getenv("OWNER_ID", "7009601543"))
OWNER_USERNAME ="@II_BAD_BABY_II"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7009601543").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://files.catbox.moe/uufiry.jpg")


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 ʜᴇʏ, ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ & ꜱᴜᴘᴇʀꜰᴀꜱᴛ ʜɪɢʜ Qᴜᴀʟɪᴛʏ ᴜꜱᴇʀʙᴏᴛ ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴡɪᴛʜ ᴀɴ ᴜᴘɢʀᴀᴅᴇᴅ ᴠᴇʀꜱɪᴏɴ ꜱᴇᴄᴜʀɪᴛʏ ꜱʏꜱᴛᴇᴍ.\n\n🌿 ɪ ᴄᴀɴ'ᴛ ʟᴇᴛ ʏᴏᴜ ᴍᴇꜱꜱᴀɢᴇ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴅᴍ ᴡɪᴛʜᴏᴜᴛ ᴍʏ ᴏᴡɴᴇʀ'ꜱ ᴘᴇʀᴍɪꜱꜱɪᴏɴ.\n\n❤️ ᴍʏ ᴏᴡɴᴇʀ ɪꜱ ᴏꜰꜰʟɪɴᴇ ɴᴏᴡ, ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ᴏᴡɴᴇʀ ᴀʟʟᴏᴡꜱ ʏᴏᴜ.\n\n🍂 ᴘʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ʜᴇʀᴇ, ʙᴇᴄᴀᴜꜱᴇ ꜱᴘᴀᴍᴍɪɴɢ ᴡɪʟʟ ꜰᴏʀᴄᴇ ᴍᴇ ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ ꜰʀᴏᴍ ᴍʏ ᴏᴡɴᴇʀ ɪᴅ 👍🏻**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))


# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://files.catbox.moe/r58nec.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("main")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')
