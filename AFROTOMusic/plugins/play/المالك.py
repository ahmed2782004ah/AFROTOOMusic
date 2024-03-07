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





@app.on_message(command(["المالك", "صاحب الخرابه", "المنشي"]) & filters.group)
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 2:
         return 
      else:
            chat_id = message.chat.id
            f = "administrators"
            async for member in client.iter_chat_members(chat_id, filter=f):
               if member.status == "creator":
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"**- 𝒈𝒓𝒐𝒖𝒑 𝒐𝒘𝒏𝒆𝒓 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 : \n\n⌁︙ 𝒏𝒂𝒎𝒆 : {m.first_name}\n\n⌁︙ 𝒖𝒔𝒆𝒓 : @{m.username}\n\n⌁︙ 𝒃𝒊𝒐 :\n{m.bio}",reply_markup=key)
                 else:
                    return await message.reply("• " + member.user.mention)
                    
                    
