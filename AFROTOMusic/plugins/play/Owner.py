import asyncio
import os
import time
import requests
from pyrogram import enums
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic import app
from AFROTOMusic.plugins.play.filters import command
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait










#المالك ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(command(["المالك", "صاحب الخرابه", "المنشي"]), group=95)
async def ownner(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await app.get_users(int(x[0]))
       if m.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"<b>╭✪ᚐɴᴧᴍᴇ : {m.first_name}\n│᚜✦ᴜsᴇꝛ : @{m.username}\n╰✪ᚐɪᴅ : <code>{m.id}</code>\n╭✪ᚐᴄʜᴧᴛ : {message.chat.title}\n╰✪ᚐɪᴅ.ᴄʜᴧᴛ : <code>{message.chat.id}</code></b>",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"b>╭✪ᚐɴᴧᴍᴇ : {m.first_name}\n│᚜✦ᴜsᴇꝛ : @{m.username}\n╰✪ᚐɪᴅ : <code>{m.id}</code>\n╭✪ᚐᴄʜᴧᴛ : {message.chat.title}\n╰✪ᚐɪᴅ.ᴄʜᴧᴛ : <code>{message.chat.id}</code></b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("عزيزي المالك هذا حساب محذوف\n༄")

                        
                    
                    
   

   
@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""❤️‍🔥 اسمك »»  {message.from_user.mention()}""")



