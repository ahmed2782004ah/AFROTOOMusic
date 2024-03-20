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

                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    senderuser = message.from_user.username
                    sender_user = "@{senderuser}" if senderuser else "لا يوجـد"
                    await app.send_message(OWNER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
                    return await app.send_message(LOGGER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
