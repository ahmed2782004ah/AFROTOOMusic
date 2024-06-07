from strings.filters import command
from AFROTOMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode, ChatMemberStatus
photolok =[]

@app.on_message(filters.command(["قفل الصور"], ""))
async def close_send_photo(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in photolok:
            return await message.reply_text(f"يا {message.from_user.mention} الصور مقفله من قبل")
        photolok.append(message.chat.id)
        return await message.reply_text(f"تم قفل الصور \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")
        
