import os
import sys
import asyncio
from pyrogram import Client
from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from pytgcalls import PyTgCalls
from motor.motor_asyncio import AsyncIOMotorClient

from ...console import (
    API_ID, API_HASH, STRING_SESSION, BOT_TOKEN, SESSION_STRING, LOGGER,
    MONGO_DB_URL, LOG_GROUP_ID, SUDOERS
)

def async_config():
    LOGGER.info("Checking Variables ...")
    required_vars = [API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, MONGO_DB_URL, LOG_GROUP_ID]
    if not all(required_vars):
        missing = [var for var in ["API_ID", "API_HASH", "BOT_TOKEN", "STRING_SESSION", "MONGO_DB_URL", "LOG_GROUP_ID"] 
                   if not eval(var)]
        LOGGER.info(f"Missing required variables: {', '.join(missing)}")
        sys.exit()
    LOGGER.info("All Required Variables Collected.")

def async_dirs():
    LOGGER.info("Initializing Directories ...")
    for folder in ["downloads", "cache"]:
        if folder not in os.listdir():
            os.mkdir(folder)
    for file in os.listdir():
        if file.endswith((".session", ".session-journal")):
            os.remove(file)
    LOGGER.info("Directories Initialized.")

async_dirs()

# Pyrogram Client Instances
app = Client(
    name="Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    plugins=dict(root="SHUKLA.plugins")
)

ass = Client(
    name="ShuklaPlayer",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

bot = Client(
    name="Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="SHUKLA.plugins")
)

# Telethon Userbot Session Initialization
telethon_client = TelegramClient(
    session=SESSION_STRING,  # Using the STRING_SESSION for the userbot
    api_id=API_ID,
    api_hash=API_HASH
)

call = PyTgCalls(app)

def mongodbase():
    global mongodb
    try:
        LOGGER.info("Connecting To Your Database ...")
        async_client = AsyncIOMotorClient
        mongobase = async_client(MONGO_DB_URL)
        mongodb = mongobase.SHUKLA
        LOGGER.info("Connected To Your Database.")
    except Exception as e:
        LOGGER.error(f"Failed To Connect, Error: {e}")
        sys.exit()

mongodbase()

async def sudo_users():
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if sudoers:
        for user_id in sudoers:
            SUDOERS.append(int(user_id))
    LOGGER.info(f"Sudo Users Loaded: {len(SUDOERS)}")

async def run_async_clients():
    LOGGER.info("Starting Userbot ...")
    await app.start()
    LOGGER.info("Pyrogram Userbot Started.")
    try:
        await telethon_client.start()
        LOGGER.info("Telethon Userbot Started.")
        await telethon_client(SendMessageRequest(LOG_GROUP_ID, "**Telethon Userbot is Active.**"))
    except Exception as e:
        LOGGER.error(f"Telethon Userbot Error: {e}")
    try:
        await app.send_message(LOG_GROUP_ID, "**sʜᴜᴋʟᴀ ᴜsᴇʀʙᴏᴛ ɪs ᴀʟɪᴠᴇ**")
    except Exception as e:
        LOGGER.error(f"Pyrogram Message Send Error: {e}")
    try:
        await app.join_chat("MASTIWITHFRIENDSXD")
        await telethon_client(SendMessageRequest("MASTIWITHFRIENDSXD", "Joined via Telethon!"))
    except:
        pass
    if SESSION_STRING:
        LOGGER.info("Starting Assistant ...")
        await ass.start()
        LOGGER.info("Assistant Started.")
        try:
            await ass.send_message(LOG_GROUP_ID, "**Assistant Started.**")
        except:
            pass
    LOGGER.info("Starting Helper Robot ...")
    await bot.start()
    LOGGER.info("Helper Robot Started.")
    try:
        await bot.send_message(LOG_GROUP_ID, "**sʜᴜᴋʟᴀ ʀᴏʙᴏᴛ ɪs ᴀʟɪᴠᴇ.**")
    except:
        pass
    LOGGER.info("Starting PyTgCalls Client...")
    await call.start()
    LOGGER.info("PyTgCalls Client Started.")
    await sudo_users()
