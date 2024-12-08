import asyncio
import importlib
import logging
import os
import sys
from functools import partial
from datetime import datetime
from logging.handlers import RotatingFileHandler

from pytgcalls import idle
from pytgcalls.exceptions import NoActiveGroupCall
from pytgcalls.types import GroupCallConfig
from pyrogram import Client, idle as pyrogram_idle
from pyrogram.enums import ChatType
from pyrogram.errors import (
    ChatAdminRequired,
    FloodWait,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from platform import python_version

from SHUKLA import __version__ as version
from SHUKLA import app, bot, call
from pytgcalls.__version__ import __version__ as pytgcalls_version
from pyrogram import __version__ as pyrogram_version
from os import getenv

from SHUKLA.console import LOG_GROUP_ID
from . import logs, plugs, vars
from .plugins import ALL_PLUGINS
from .modules.clients.clients import run_async_clients
from .modules.clients.enums import run_async_enums
from .modules.helpers.inline import run_async_inline

# Load environment variables
load_dotenv()

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
LOGGER = logging.getLogger("SYSTEM")

# Suppress noisy loggers
for module in ["apscheduler", "asyncio", "httpx", "pyrogram", "pytgcalls"]:
    logging.getLogger(module).setLevel(logging.ERROR)


async def import_plugins():
    """Import all plugins and populate the plugs dictionary."""
    for all_plugin in ALL_PLUGINS:
        imported_plugin = importlib.import_module("SHUKLA.plugins" + all_plugin)
        if hasattr(imported_plugin, "__NAME__") and imported_plugin.__NAME__:
            imported_plugin.__NAME__ = imported_plugin.__NAME__
            if hasattr(imported_plugin, "__MENU__") and imported_plugin.__MENU__:
                plugs[imported_plugin.__NAME__.lower()] = imported_plugin


async def start_clients():
    """Start both bot and assistant clients."""
    try:
        await bot.start()
        LOGGER.info("✅ Bot Started.")
    except Exception as e:
        LOGGER.error(f"🚫 Bot Error: {e}")
        sys.exit()

    try:
        await app.start()
        LOGGER.info("✅ Assistant Started.")
    except Exception as e:
        LOGGER.error(f"🚫 Assistant Error: {e}")
        sys.exit()


async def send_startup_messages(version: dict):
    """Send startup messages to the log group if applicable."""
    log_group_id = getattr(console, "LOG_GROUP_ID", -1002356967761)  # Fixed 'console' to 'config'
    if log_group_id != 0:
        try:
            await bot.send_animation(
                log_group_id,
                "https://files.catbox.moe/zvwx1y.mp4",
                f"**✅ Userbot is Online!**\n\n"
                f"**🔹 Version ➠ ** `{version['CakeMusic']}`\n"
                f"**🔹 Pyrogram ➠ ** `{version['pyrogram']}`\n"
                f"**🔹 Python ➠ ** `{version['python']}`\n\n"
                f"**🔹 Pytgcalls ➠ ** `{version['pytgcalls']}`\n"
                f"**</> @ll_THE_BAD_BOT_ll**",
                disable_notification=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "💫 Start Me",
                                url=f"https://t.me/{bot.me.username}?start=start",
                            ),
                            InlineKeyboardButton(
                                "💖 Repo",
                                url="https://github.com/Badhacker98/PBX_2.0/fork",
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "💬 Support", url="https://t.me/ll_THE_BAD_BOT_ll"
                            )
                        ],
                    ]
                ),
            )
            await app.send_message(log_group_id, "**🦋 Userbot assistant Started.**")
        except Exception as e:
            LOGGER.warning(f"Could not send startup messages: {e}")


async def main():
    LOGGER.info("🌐 Checking Required Variables ...")
    required_env_vars = [
        "API_ID",
        "API_HASH",
        "BOT_TOKEN",
        "STRING_SESSION",
        "MONGO_DB_URL",
    ]
    missing_vars = [var for var in required_env_vars if not getenv(var)]
    if missing_vars:
        LOGGER.error(f"❌ Missing Environment Variables: {', '.join(missing_vars)}")
        sys.exit()

    LOGGER.info("✅ Required Variables Collected.")
    await asyncio.sleep(1)

    LOGGER.info("🌀 Starting Clients ...")
    await start_clients()

    LOGGER.info("🌀 Importing Plugins ...")
    await import_plugins()

    LOGGER.info("🌀 Sending Startup Messages ...")
    version_info = {
        "CakeMusic": version,
        "pyrogram": pyrogram_version,
        "python": python_version(),
        "pytgcalls": pytgcalls_version,
    }
    await send_startup_messages(version_info)

    LOGGER.info("🌀 Starting PyTgCalls ...")
    try:
        await call.start()
        LOGGER.info("✅ PyTgCalls Started.")
    except Exception as e:
        LOGGER.error(f"🚫 PyTgCalls Error: {e}")
        sys.exit()

    LOGGER.info("✅ Successfully Hosted Your Bot !!")
    LOGGER.info("✅ Visit @AdityaServer for Updates !!")
    await idle()


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        LOGGER.info("💤 Shutting Down ...")
