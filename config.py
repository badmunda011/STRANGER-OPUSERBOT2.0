import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002356967761"))
