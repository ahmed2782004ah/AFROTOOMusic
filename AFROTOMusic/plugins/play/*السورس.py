import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›", "السورس", "سورس عفرتو"])
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/0913f5246d0532e170e21.mp4",
        caption=f"""
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        " 𝙲𝙷𝙰𝙽𝙽𝙴𝙻  ", url=f"https://t.me/UI_VM"),
                   InlineKeyboardButton(
                    
                    " 𝙶𝚁𝙾𝚄𝙿 ", url=f"https://t.me/YR_HX"), 
                ],[    
                    InlineKeyboardButton(
                        "𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ", url=f"https://t.me/VVYVVJ"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )

