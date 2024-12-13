import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ... import __version__, app, bot
from ...modules.helpers.buttons import paginate_plugins
from ...modules.helpers.wrapper import cb_wrapper

@app.on_message(filters.command("help"))
async def inline_help_menu(client, message):
    """
    Displays the inline help menu with optional logo or text-based interface.
    """
    try:
        bot_results = await app.get_inline_bot_results(
            f"@{bot.me.username}", "help_menu_logo" if image else "help_menu_text"
        )
        await app.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=bot_results.query_id,
            result_id=bot_results.results[0].id,
        )
    except Exception as e:
        print(f"Error while sending help menu: {e}")
        return

    try:
        await message.delete()
    except Exception as e:
        print(f"Error deleting help message: {e}")


@bot.on_callback_query(filters.regex(r"help_(.*?)"))
@cb_wrapper
async def help_button(client, query):
    """
    Handles callback queries for help menu navigation.
    """
    match = re.match(r"help_(plugin|prev|next|back)(?:(.*?))?", query.data)
    if not match:
        return

    action, param = match.groups()
    top_text = f"""
**💫 Welcome to Help Menu**
Shukla Userbot » {__version__} ✨

❤️ Click the buttons below to explore commands ❤️

🌹 Powered by ♡ [Updates](https://t.me/SHIVANSH474) 🌹**
"""

    if action == "plugin":
        plugin = param
        plugin_text = f"""
**💫 Welcome to the Help Menu for Plugin**
✨ **{plugs[plugin].__NAME__}** ✨

{plugs[plugin].__MENU__}
"""
        await bot.edit_inline_text(
            query.inline_message_id,
            text=plugin_text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("↪️ Back", callback_data="help_back")]
            ]),
            disable_web_page_preview=True,
        )

    elif action == "prev":
        current_page = int(param)
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(current_page - 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif action == "next":
        next_page = int(param)
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(next_page + 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif action == "back":
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(0, plugs, "help")
            ),
            disable_web_page_preview=True,
        )
