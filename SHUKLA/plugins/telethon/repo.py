from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from telethon.errors.rpcerrorlist import YouBlockedUserError
from SHUKLA.plugins.telethon.inline import *
from config import BOT_USERNAME
from ... import *

msg = f"""
**💫 ᴘʙxᴜsᴇʀ ʙᴏᴛ  💫**
  •        [✨ Repo ✨](https://github.com/Badhacker98/PbXbot/fork)
  •        [𝐏ʙx 𝐒ᴜᴘᴘᴏʀᴛ ](https://t.me/ll_THE_BAD_BOT_ll)
  •  ©️ {Pbx_channel} ™
"""


@app.on(events.NewMessage(pattern="/repo"))
async def repo(event):
    II_BAD_BBY_II, _, _ = await client_id(event)
    try:
        Pbx = await event.client.inline_query(Config.BOT_USERNAME, "repo")
        await Pbx[0].click(event.chat_id)
        if event.sender_id == II_BAD_BBY_II:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)
      
