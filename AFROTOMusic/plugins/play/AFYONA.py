import asyncio
from pyrogram import Client, filters
from strings.filters import command
from AFROTOMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨*"




REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
        ("الاوامر")
    ],
    
    [
        ("العكس"),
        ("احرف")
    ],
    [
        ("مطور السورس"),
        ("مطور البوت")
    ],
   
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب")
    ],
    [
        ("نكته"),
        ("كتابات")
    ],
    [
        ("اذكار")
    ],
    [
        ("زخارف"),
        ("انصحني")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("لو خيروك"),
        ("احساب العمر")
    ],    
    [
        ("اخفاء الازرار")
    ]
  
]



  

@app.on_message(filters.regex("^/AFRO"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار"))
async def down(client, message):
          m = await message.reply("**تم قفل الكيبورد بنجاح**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/04b2f1f1c808dc49db35b.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("ᯓ 𝚂𝙾𝚞𝚁𝚂 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 𖠛", url=f"https://t.me/UI_VM"),
            ]
         ]
     )
  )

