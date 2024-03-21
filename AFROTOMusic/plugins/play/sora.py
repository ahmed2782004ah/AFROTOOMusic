import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AFROTOMusic import app
import random
    

@app.on_message(command([f"صوره", "صورة", "صور"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الصوره لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )

listmu = []
@Client.on_message(filters.command(["اغاني", "غنيلي", "غ", "اغنيه","اغنية عشوائية"], ""))
async def voece(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(listmu) == 0:
   user = await get_userbot(client.me.username)
   async for msg in user.get_chat_history("ELNQYBMUSIC"):
      if msg.media:
        listmu.append(msg.id)
  audi = random.choice(listmu)
  audio = f"https://t.me/ELNQYBMUSIC/{audi}"
  await message.reply_audio(audio=audio, caption="**♪ 𝑱𝒐𝒊𝒏 ➧ @UI_VM  💎 .**")
    
