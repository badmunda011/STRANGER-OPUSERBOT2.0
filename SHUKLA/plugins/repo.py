from ... import *
from telethon import TelegramClient
from telethon.tl.custom import Button
from telethon.tl.types import InputPeerUser

from telethon import TelegramClient, events
from telethon.tl.custom import Button


# The repository link
repo_link = "https://github.com/username/repository"

# Command handler for '/repo'
@client.on(events.NewMessage(pattern='/repo'))
async def send_repo_message(event):
    # Send a message with a button when the '/repo' command is received
    await event.respond(
        'Here is the repository you requested:',
        buttons=[
            [Button.url('Visit Repository', repo_link)]  # Button with the repository link
        ]
    )
