import os
import sys
import asyncio
from pyrogram import Client
from pyrogram import filters
from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from pytgcalls import PyTgCalls, filters as pytgfl
from pytgcalls.types import Call, MediaStream, AudioQuality, VideoQuality
from motor.motor_asyncio import AsyncIOMotorClient

from ...console import (
    API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, LOGGER,
    MONGO_DB_URL, LOG_GROUP_ID, SUDOERS
)

# Async configuration function to check required variables
def async_config():
    LOGGER.info("Checking Variables ...")
    required_vars = [API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URL, LOG_GROUP_ID]
    if not all(required_vars):
        missing = [var for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_DB_URL", "LOG_GROUP_ID"] 
                   if not eval(var)]
        LOGGER.info(f"Missing required variables: {', '.join(missing)}")
        sys.exit()
    LOGGER.info("All Required Variables Collected.")

# Directory initialization function
def async_dirs():
    LOGGER.info("Initializing Directories ...")
    for folder in ["downloads", "cache"]:
        if folder not in os.listdir():
            os.mkdir(folder)
    for file in os.listdir():
        if file.endswith((".session", ".session-journal")):
            os.remove(file)
    LOGGER.info("Directories Initialized.")

# Initializing directories
async_dirs()

# Pyrogram Client Instances
app = Client(
    name="Assistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,  # Use same session for Userbot
    plugins=dict(root="SHUKLA.plugins")
)

# Helper Bot Client for Pyrogram
bot = Client(
    name="Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="SHUKLA.plugins")
)

# Telethon Client using the Pyrogram string session
telethon_client = TelegramClient(
    "userbot_session",  # Use a session file name for Telethon
    API_ID,
    API_HASH
)

# Override the Telethon client session to use Pyrogram's string session
telethon_client.session = telethon_client.session.from_string(STRING_SESSION)

# PyTgCalls instance
call = PyTgCalls(app)

# MongoDB connection function
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

# Initialize database
mongodbase()

# Load sudo users from the database
async def sudo_users():
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if sudoers:
        for user_id in sudoers:
            SUDOERS.append(int(user_id))
    LOGGER.info(f"Sudo Users Loaded: {len(SUDOERS)}")

# Start the clients and necessary actions
async def run_async_clients():
    LOGGER.info("Starting Userbot ...")
    await app.start()
    LOGGER.info("Userbot Started.")
    await telethon_client.start()  # This starts the Telethon Userbot
    LOGGER.info("Telethon Client Started.")
    
    try:
        # Send message from Pyrogram
        await app.send_message(LOG_GROUP_ID, "**sʜᴜᴋʟᴀ ᴜsᴇʀʙᴏᴛ ɪs ᴀʟɪᴠᴇ**")
        # Send message from Telethon
        await telethon_client(SendMessageRequest(LOG_GROUP_ID, "**Telethon Client Active**"))
    except Exception as e:
        LOGGER.error(f"Message Send Error: {e}")

    try:
        # Join group using Pyrogram and Telethon
        await app.join_chat("MASTIWITHFRIENDSXD")
        await telethon_client(SendMessageRequest("MASTIWITHFRIENDSXD", "Joined via Telethon!"))
    except:
        pass

    # Starting Assistant (Pyrogram) if SESSION_STRING is provided
    if STRING_SESSION:
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
    
    # Start the call client
    LOGGER.info("Starting PyTgCalls Client...")
    await call.start()
    LOGGER.info("PyTgCalls Client Started.")
    
    # Load sudo users
    await sudo_users()
