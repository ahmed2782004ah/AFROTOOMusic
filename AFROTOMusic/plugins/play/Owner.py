import asyncio
import os
import time
import requests
import aiohttp
from strings.filters import command
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait

@app.on_message(command(["المنشئ", "المالك"]) & filters.group )
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 5:
         return 
      else:
            chat_id = message.chat.id
            f = "administrators"
            async for member in client.get_chat_members(chat_id, filter=f):
               if member.status == "creator":
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"🕷 ¦𝙽𝙰𝙼𝙴 :{m.first_name}\n🐉 ¦𝚄𝚂𝙴𝚁 :@{m.username}\n🐰 ¦𝙸𝙳 :`{m.id}`\n🎬 ¦𝙱𝙸𝙾 :{m.bio}\n💎 ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n🗿 ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :`{message.chat.id}`",reply_markup=key)
                 
                    
                    
   

   
@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""❤️‍🔥 اسمك »»  {message.from_user.mention()}""")



