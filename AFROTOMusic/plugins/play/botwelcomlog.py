# This code is written by (C) TheTeamAlexa bot will send message to log group when someone add
# this bot to new group make sure to star all projects
# Copyright (C) 2021-2022 by Alexa_Help@ Github, < TheTeamAlexa >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki

from pyrogram import Client, filters
from pyrogram.types import Message
from AFROTOMusic import app
from AFROTOMusic.utils.database import get_served_chats
from config import OWNER_ID


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        lemda_text = f"مرحبا عزيزي المطور لقد تم اضافه البوت لمجموعه جديده ..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ الاسم › : {matlabi_jhanto}\n┣★ايدي الدردشة › : {chat_id}\n┣★ يوزر الدردشه › : {chatusername}\n┣★مجموع الدردشات › : {bot_chats}\n┣★اضيف بواسطة › :\n┗━━━ {added_by}"
        await lul_message(OWNER_ID, lemda_text)
