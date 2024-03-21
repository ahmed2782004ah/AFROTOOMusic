import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait





@app.on_message(command(["مطور البوت", "المالك", "المنشئ"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(creator)
    name = usr.first_name
    usrnam = usr.username
    photo = usr.photo.big_file_id
    photo = await client.download_media(photo)
    
    await message.reply_photo(
        photo=photo,
        caption=f"""ٴ<b>•─‌‌‏ 𝚂𝙾𝚞𝚁𝙲𝙴 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ‌─‏─•</b>
                    
- o𝚆𝙽𝙴𝚁 :[{name}]
- 𝚄𝚂𝙴𝚁 :@{usrnam} 
- 𝙸𝙳 :`{usr.id}`
 
ٴ<b>•──‌‌𝚂𝙾𝚞𝚁𝙲𝙴 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ──‌‌‏─‌•</b> """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
            ],[
              InlineKeyboardButton(" 𝚂𝙾𝚞𝚁𝙲𝙴 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ‌", url="https://t.me/UI_VM"),
            ],
          ]
       )                 
    )                    
                    
