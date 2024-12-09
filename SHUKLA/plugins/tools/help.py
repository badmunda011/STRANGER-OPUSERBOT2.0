import re
from pyrogram import *
from pyrogram.types import *

from ... import *
from ... import __version__
from ...modules.helpers.buttons import *
from ...modules.helpers.inline import *
from ...modules.helpers.wrapper import *


@app.on_message(cdx(["help"]))
@sudo_users_only
async def inline_help_menu(client, message):
    try:
        # Check if an image is provided or use text-based results
        bot_results = await app.get_inline_bot_results(
            f"@{bot.me.username}", 
            "help_menu_logo" if image else "help_menu_text"
        )
        # Send the inline bot result
        await app.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=bot_results.query_id,
            result_id=bot_results.results[0].id,
        )
    except Exception as e:
        print(f"Error fetching inline bot results: {e}")
        # Fallback to text-based help menu
        try:
            bot_results = await app.get_inline_bot_results(
                f"@{bot.me.username}", "help_menu_text"
            )
            await app.send_inline_bot_result(
                chat_id=message.chat.id,
                query_id=bot_results.query_id,
                result_id=bot_results.results[0].id,
            )
        except Exception as fallback_error:
            print(f"Fallback error: {fallback_error}")
    finally:
        # Try deleting the original message for cleanup
        try:
            await message.delete()
        except Exception as del_error:
            print(f"Error deleting message: {del_error}")


@bot.on_callback_query(filters.regex(r"help_(.*?)"))
@cb_wrapper
async def help_button(client, query):
    plug_match = re.match(r"help_plugin(.+?)", query.data)
    prev_match = re.match(r"help_prev(.+?)", query.data)
    next_match = re.match(r"help_next(.+?)", query.data)
    back_match = re.match(r"help_back", query.data)
    
    top_text = f"""
**💫 Welcome to the Help Menu Op.  
Shukla UserBot » {__version__} ✨  

❤️ Click on the buttons below to get UserBot commands ❤️.  

🌹 Powered by ♡  [ Update ](https://t.me/SHIVANSH474) 🌹**
"""

    if plug_match:
        plugin = plug_match.group(1)
        text = (
            f"💫 Welcome to the Help Menu of \n💕 Plugin ✨ ** {plugs[plugin].__NAME__}**\n"
            + plugs[plugin].__MENU__
        )
        key = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("↪️ Back", callback_data="help_back")],
            ]
        )

        await bot.edit_inline_text(
            query.inline_message_id,
            text=text,
            reply_markup=key,
            disable_web_page_preview=True
        )
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(curr_page - 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(next_page + 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(0, plugs, "help")
            ),
            disable_web_page_preview=True,
        )
