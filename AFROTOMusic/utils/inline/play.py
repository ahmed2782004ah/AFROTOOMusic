import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
import math
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified

import config
from AFROTOMusic import app 
from config import OWNER_ID, LOGGER_ID

from pyrogram.types import InlineKeyboardButton

from AFROTOMusic.utils.formatters import time_to_seconds
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username


def track_markup(_, videoid, user_id, channel, fplay):
   
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "◉—————————"
    elif 10 < umm < 20:
        bar = "—◉————————"
    elif 20 <= umm < 30:
        bar = "——◉———————"
    elif 30 <= umm < 40:
        bar = "———◉——————"
    elif 40 <= umm < 50:
        bar = "————◉—————"
    elif 50 <= umm < 60:
        bar = "—————◉————"
    elif 60 <= umm < 70:
        bar = "——————◉———"
    elif 70 <= umm < 80:
        bar = "———————◉——"
    elif 80 <= umm < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],[
            InlineKeyboardButton(text="𝚁𝙴𝚂𝚞𝙼𝙴 ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝙿𝙰𝚞𝚂𝙴 ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="𝚁𝙴𝙿𝙻𝙰𝚈 ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],[
            InlineKeyboardButton(text="𝚂𝙺𝙸𝙿 ‌", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="𝚂𝚃𝙾𝙿 ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],[    
            InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
        ],[
            InlineKeyboardButton(text=" اضف البوت الي مجموعتك او قناتك ", url=f"https://t.me/{app.username}?startgroup=true")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="𝚁𝙴𝚂𝚞𝙼𝙴  ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝙿𝙰𝚞𝚂𝙴 ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="𝙴𝙿𝙻𝙰𝚈 ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],[
            InlineKeyboardButton(text="𝚂𝙺𝙸𝙿 ‌", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="𝚂𝚃𝙾𝙿 ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],[
            InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
        ],[
            InlineKeyboardButton(text="داضف البوت الي مجموعتك او قناتك ", url=f"https://t.me/{app.username}?startgroup=true")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"ModyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text=" 𝒓𝒆𝒔𝒖𝒎𝒆 ",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
