import os

from os import getenv
from io import BytesIO
from dotenv import load_dotenv
from pyrogram import Client, filters

# config variables
if os.path.exists("Config.env"):
    load_dotenv("Config.env")

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002356967761"))
