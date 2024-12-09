import html
from config import BOT_USERNAME
import random
from math import ceil
from re import compile

from telethon import Button, functions
from telethon.events.inlinequery import InlineQuery
from telethon.events.callbackquery import CallbackQuery
from telethon.tl.functions.users import GetFullUserRequest

mybot = config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


elif event.query.user_id in auth and query == "repo":
result = builder.article(
    title="Repository",
    text=f"**👻 🕊️⃝‌ᴘʙx ❤️ᥫ᭡፝֟፝֟ 👻 **",
    buttons=[
        [Button.url("💫 𝐑ᴇᴘᴏ ✨", "https://github.com/Badhacker98/PbXbot/fork")],
        [Button.url("𝐏ʙx 𝐒ᴜᴘᴘᴏʀᴛ", "https://t.me/ll_THE_BAD_BOT_ll")],
                ],
            )
