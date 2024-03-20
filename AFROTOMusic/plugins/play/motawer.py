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
async def kimmyy(client: Client, message: Message):
    usr = await client.get_users(OWNER)
    name = usr.first_name
    async for photo in client.iter_profile_photos(OWNER, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛**
                    
🔥 ¦𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{OWNER})
📀 ¦𝚄𝚂𝙴𝚁 :@{OWNER} 
🆔 ¦𝙸𝙳 :`{usr.id}`
 
**ᯓ 「𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾」، ⦃𓏛** """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{OWNER}")
            ],                   
          ]              
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(OWNER, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
                    return await app.send_message(config.LOG_GROUP_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")

