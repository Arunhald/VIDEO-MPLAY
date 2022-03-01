import asyncio

from pytgcalls import idle
from pyrogram.types import Message
from pyrogram.errors import BotInlineDisabled

from program import LOGS
from config import BOT_USERNAME, OWNER_ID
from driver.core import calls, bot, user


peer = f"@{BOT_USERNAME}"

async def start_bot(message):
    await bot.start()
    LOGS.info("[INFO]: BOT & USERBOT CLIENT STARTED !!")
    await calls.start()
    LOGS.info("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("VeezSupportGroup")
    await user.join_chat("levinachannel")
    await asyncio.sleep(1)
    await user.send_message(peer, "/start") # this help to prevent peer_id_invalid issue
    await asyncio.sleep(1)
    try:
        inline = await user.get_inline_bot_results(BOT_USERNAME, "music")
        result = await user.send_inline_bot_result(
            message.chat.id,
            query_id=inline.query_id,
            result_id=inline.results[0].id,
            hide_via=True
        )
    except BotInlineDisabled:
        LOGS.info("[WARN]: The inline mode of your bot is disabled, enable it to use the inline feature !")
        await user.send_message(OWNER_ID,
                                f"The inline mode of {peer} is disabled, and to be able use the inline feature of your bot, please enable the inline mode from @BotFather.",
                                "\n\nstart @BotFather > type /mybots and choose your bot > click on Bot Settings button > click on Inline Mode button > and click on Turn inline mode on")
        return

    await idle()
    LOGS.info("[INFO]: BOT & USERBOT STOPPED !!")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot(message))
