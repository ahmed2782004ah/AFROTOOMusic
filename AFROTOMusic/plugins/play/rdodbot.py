import asyncio

import random

from AFROTOMusic import app

from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)


from pyrogram import filters, Client





txt = [


"ها عايز اي 🙄",
"ايوااا جااااي 😂",
"عاوزني اشقطلك مين يروحي 🥺",
"لو خيروك |  بين إمكانية ",
"قلب البوت 🥺",
"يعم تعبتنا معاك 🙁",
"استنا يعم بشقط وجايبك علطول 😂",

        ]


        


@app.on_message(filters.command(["بوت","يا بوت"], ""))

async def khyrok(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
