import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from AFROTOMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["مطور", "المطور"]) & filters.group)
async def zilzal(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    photo = user.photo.big_file_id
     photo = await client.download_media(photo)       caption=f"""ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b>
                    
- 𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{OWNER})
- 𝚄𝚂𝙴𝚁 :@{usrnam} 
- 𝙸𝙳 :`{usr.id}`
 
ٴ<b>•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•</b> """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
            ],[
              InlineKeyboardButton("•✯ ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛 ✯•", url="https://t.me/T_Y_E_X"),
            ],
          ]
       )                 
    )                    
