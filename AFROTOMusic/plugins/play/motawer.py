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


@app.on_message(command(["مطور البوت", "مطور", "المطور"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    bio = user.bio
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ee99f5b99514304efeffd.jpg",
        caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
            ],[
              InlineKeyboardButton("•✯ ᴢᴛʜᴏɴ_ᴍᴜsɪᴄ ✯•", url="https://t.me/Zelzal_Music"),
            ],
          ]
       )                 
    )                    
