from telethon import TelegramClient, events
from ... import *


@telethon_client.on(events.NewMessage(pattern=r'\.pingg'))  # Trigger for the ".ping" command
async def ping(event):
    """
    Responds to the .ping command with 'Pong!' and latency.
    """
    start = event.message.date  # Get the message's timestamp
    reply = await event.reply("Pong!")  # Send initial response
    end = reply.date  # Get the reply's timestamp
    
    # Calculate latency
    latency = (end - start).total_seconds() * 1000
    await reply.edit(f"Pong! 🏓\nLatency: {latency:.2f} ms")
