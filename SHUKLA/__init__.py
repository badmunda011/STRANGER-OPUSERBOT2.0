from typing import Union, List, Pattern
from SHUKLA.console import  SUDO_USERS, OWNER_ID, OWNER_USERNAME
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_async_
from pytgcalls import PyTgCalls, filters as pytgfl
from pytgcalls.types import ChatUpdate, Update, GroupCallConfig
from pytgcalls.types import Call, MediaStream, AudioQuality, VideoQuality

# Ai-Userbot Version
__version__ = "v2.1.0"

spam_chats = []
SUDO_USER = SUDO_USERS
OWNER_USERNAME = OWNER_USERNAME
SUDO_USERS.append(OWNER_ID)


# Command filters for bot and app
def cdx(commands: Union[str, List[str]]):
    """Filter commands starting with /, !, or ."""
    return pyrofl.command(commands, prefixes=["/", "!", "."])


def cdz(commands: Union[str, List[str]]):
    """Filter commands starting with no prefix or /, !, ."""
    return pyrofl.command(commands, prefixes=["", "/", "!", "."])


def rgx(pattern: Union[str, Pattern]):
    """Filter messages matching a regex pattern."""
    return pyrofl.regex(pattern)


from SHUKLA.console import *

mongo_async_cli = _mongo_async_(console.MONGO_DB_URL)
mongodb = mongo_async_cli.badmundaxdb

# All Clients
from .modules.clients.clients import (
    app, bot, call
)
app = app
bot = bot
call = call


# Command Handlers
from .modules.helpers.filters import (
    commandx, commandz
)
cdx = commandx
cdz = commandz


# Edit Or Reply
from .modules.helpers.events import (
    edit_or_reply
)
eor = edit_or_reply


# Logger
from .console import LOGGER
logs = LOGGER


# Plugins
from .console import PLUGINS
plugs = PLUGINS


# Variables
from . import console as config
vars = config


# Decorators
from .modules.helpers.wrapper import (
    super_user_only, sudo_users_only
)
super_user_only = super_user_only
sudo_users_only = sudo_users_only
