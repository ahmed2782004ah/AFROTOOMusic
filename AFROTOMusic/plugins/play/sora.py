import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AFROTOMusic import app
import random
    

@app.on_message(command([f"صوره", "صورة", "صور", "{BOT_USERNAME} صوره"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/TTTTRTTRT/{rl}"
    await client.send_photo(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الصوره لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
