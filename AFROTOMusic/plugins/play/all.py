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
from AFROTOMusic  import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AFROTOMusic  import app
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait








array = []
@app.on_message(filters.command(["@all", "تاك","all"], "") & ~filters.private, group=88)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text("♪ التاك قيد التشغيل الان  💎 .")
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .")
    return
  await message.reply_text("♪ جاري بدأ المنشن ، لايقاف الامر اضغط /cancel  💎 .")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("all","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.get_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ›"
       if i == 20:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@app.on_message(filters.command(["/cancel", "ايقاف التاك"], ""), group=822)
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .")
    return
  if message.chat.id not in array:
     await message.reply("♪ المنشن متوقف بي الفعل  💎 .")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("♪ تم ايقاف المنشن عزيزي  💎 .")
    return

@Client.on_message(filters.new_chat_members)
async def wel__come(client: Client, message):
	chatid= message.chat.id
	await client.send_message(text=f"• لا تسئ اللفظ وان ضاق عليك الرد\nٌٍ𝘠ُُ𝘖ٍٰ𝘜ًٍ𝘙 ٍَ𝘕ٍَّ𝘈ٍّٰ𝘔ٍٓ𝘌 » {message.from_user.mention}\nٌٕ𝘎ًٍ𝘙ُُ𝘖ٍٰ𝘜ٍَ𝘗 » {message.chat.title}",chat_id=chatid)
	
@Client.on_message(filters.left_chat_member)
async def good_bye(client: Client, message):
	chatid= message.chat.id
	await client.send_message(text=f"كنت راجل محترم يا  {message.from_user.mention} ",chat_id=chatid)
