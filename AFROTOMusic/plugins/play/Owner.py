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
                
@app.on_message(command(["المالك", "صاحب الخرابه", "المنشي"]), group=222)
async def ownner(client: Client, message: Message):
    x = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
         if m.status == ChatMemberStatus.OWNER:
            x.append(m.user.id)
    if len(x) != 0:        
       m = await app.get_users(int(x[0]))
       if m.photo:
         async for photo in app.get_chat_photos(x[0],limit=1):
          await message.reply_photo(photo.file_id,caption=f"⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:{message.from_user.id}\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : {message.chat.id}",reply_markup=InlineKeyboardMarkup(
             [              
               [          
                 InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")
               ],             
             ]                 
            )                     
          )
       else:
        await message.reply_text(f"⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:{message.from_user.id}\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : {message.chat.id}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.first_name, url=f"https://t.me/{m.username}")],]))
    else:
        await message.reply_text("الاك محذوف يقلب")
                        
                    
                    
   

   
@app.on_message(command(["اسمي", "اسمي اي"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""❤️‍🔥 اسمك »»  {message.from_user.mention()}""")



