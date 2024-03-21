import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AFROTOMusic import app
from random import  choice, randint

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@app.on_message(command(["اقتله ", "تخ", "قتل"]))
async def zdatsr(client: Client, message: Message):
    await message.reply_animation(
        animation=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
    )
    reply_markup=InlineKeyboardMarkup(

       [
           [
               InlineKeyboardButton(
                   "‹ : 𝖬𝖺𝖳𝗋𝗂x 𝖳𝖾𝖠𝗆 : ›", url=f"https://t.me/XMATTMX"),
           ],
       ]
    ),
