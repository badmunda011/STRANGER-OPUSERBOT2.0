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
STRING_SESSION ="BQGIzloAS8aDcjKd8zRdYkAXdQA1FLXOF1S2cERCELpbw5PKX95SDUH1pc8BqkMSm-KJkp2yAtOgHk4JOfjgiuoDFbAE91UCnkCpfZq9dN7HkxCXTw4gis9hpXuDW5xqSXYdxBiI8UxQEk2X430-CVhPBUshzEP3wJj4fP31gN_ffbPZcJytSoC2e1SS0vBHWkUUJITqtLYpObavXaEbFPK0e7o6OtpKnfCzlH4q19K0xY3UqJmNIYAXYkNcse1zbPRu-4n0F6Rcfcd8iIxwm7XlUt5Sf84_T4QGYgvGCjFVWO4cHs-zCHhgtJMkYTyWVoOgQyH9vcuGOBaFntjxOrKTScflRwAAAAF5XDOMAA"
MONGO_DB_URL ="mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1002356967761))
OWNER_ID = int(getenv("OWNER_ID", "7009601543"))
OWNER_USERNAME ="@II_BAD_BABY_II"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7009601543").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://files.catbox.moe/uufiry.jpg")


# OPTIONAL VARIABLES
SESSION_STRING = "1BZWaqwUAUEvGg3IynfM0XWJAF3UANRS1zhdUtnBEQhC6W8OTyl_eUg1B9aXPAapDEpviiZKdsgLToB5OCTn44IrqAxWwBPdVAp5AqX2avXTex5MQl08OIIrPYaV7g1ucakl2HcQYiPFMUBJNl-N9PglYTwVLIcxD98CY-Hz99YDf332z2XCcrUqAtntUktLwR1pFFCSE6rS2KTm2r12hGxTytHu6OjraSp3ws5R-KtfStMWN1KiZjSGAF2JDXLHtc2z0bvuJ9BekXH3HfIiMcJu15VLeUn_OP0-EBmILxgoxVVjuHB7Pswh4YLSTJGE8llaDoEMh_b3LhjgWhZ7Y8Tqyk0nH5Uc="
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

