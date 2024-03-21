import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["عفرتو","مطور السورس","مبرمج السورس"],"")
)
async def yas(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ْ𓆩⧛ َ 𝘼َِ𝙁َِ𝙍َِ𝙊َِ𝙊َِ𝙏َِ𝙊ِ ┇ عـ๋͜‏ـۂفــ͡ـࢪتوُ ⧚𓆪](https://t.me/IIUll_l)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @IIUll_l ❫
◉ 𝙸𝙳      : ❪ `5904216848` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@UI_VM)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ْ𓆩⧛ َ 𝘼َِ𝙁َِ𝙍َِ𝙊َِ𝙊َِ𝙏َِ𝙊ِ ┇ عـ๋͜‏ـۂفــ͡ـࢪتوُ ⧚𓆪", url=f"https://t.me/IIUll_l"), 
                 ],[
                   InlineKeyboardButton(
                        "「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」", url=f"https://t.me/UI_VM"),
                ],

            ]

        ),

    )
