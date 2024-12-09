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
    image = None
    try:
        if image:
            bot_results = await app.get_inline_bot_results(
                f"@{bot.me.username}", "help_menu_logo"
            )
        else:
            bot_results = await app.get_inline_bot_results(
                f"@{bot.me.username}", "help_menu_text"
            )
        await app.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=bot_results.query_id,
            result_id=bot_results.results[0].id,
        )
    except Exception:
        bot_results = await app.get_inline_bot_results(
            f"@{bot.me.username}", "help_menu_text"
        )
        await app.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=bot_results.query_id,
            result_id=bot_results.results[0].id,
        )
    except Exception as e:
        print(e)
        return

    try:
        await message.delete()
    except:
        pass
      


@bot.on_callback_query(filters.regex(r"help_(.*?)"))
@cb_wrapper
async def help_button(client, query):
    plug_match = re.match(r"help_plugin(.+?)", query.data)
    prev_match = re.match(r"help_prev(.+?)", query.data)
    next_match = re.match(r"help_next(.+?)", query.data)
    back_match = re.match(r"help_back", query.data)
    
    image_url = "https://files.catbox.moe/83d5lc.jpg"
    
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
            client.send_photo,
            query.inline_message_id,
            photo=image_url,
            text=text,
            reply_markup=key,
            disable_web_page_preview=True
        )
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await bot.edit_inline_text(
            client.send_photo,
            query.inline_message_id,
            photo=image_url,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(curr_page - 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await bot.edit_inline_text(
            client.send_photo,
            query.inline_message_id,
            photo=image_url,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(next_page + 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await bot.edit_inline_text(
            client.send_photo,
            query.inline_message_id,
            photo=image_url,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(0, plugs, "help")
            ),
            disable_web_page_preview=True,
        )
