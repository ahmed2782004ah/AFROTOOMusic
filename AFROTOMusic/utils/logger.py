from pyrogram.enums import ParseMode

from AFROTOMusic import app
from AFROTOMusic.utils.database import is_on_off
from config import OWNER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""━━━━ılıı❚𝚂𝙾𝚄𝚁𝙲𝙴 𝙰𝙵𝚁𝙾𝚃𝙾𝙾❚ıılı━━━━
<b>╭⦿<b>{app.mention}
<b>╰⦿ ᴘʟᴧʏ ⸢ɢꝛᴏᴜᴘ⸥ ᴍᴜsɪᴄ♪</b>

<b>╭⦿ ᴄʜᴧᴛ ɴᴧᴍᴇ :</b> {message.chat.title}
<b>│᚜⦿ᴄʜᴧᴛ ᴜsᴇꝛ :</b> @{message.chat.username}
<b>│᚜⦿ɴᴧᴍᴇ :</b> {message.from_user.mention}
<b>╰⦿ ᴜsᴇꝛɴᴧᴍᴇ :</b> @{message.from_user.username}

<b>╭⦿ ǫᴜᴇꝛʏ :</b> {message.text.split(None, 1)[1]}
<b>╰⦿ sᴛꝛᴇᴧᴍᴛʏᴘᴇ :</b> {streamtype}
━ılıılıılıılıılıılıılıılıılıılıılıılılıılıılıılıılıılıılıılı━"""
        if message.chat.id != OWNER_ID:
            try:
                await app.send_message(
                    chat_id=OWNER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
