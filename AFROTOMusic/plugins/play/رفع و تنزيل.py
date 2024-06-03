import asyncio
import re
from pyrogram import Client, filters
from datetime import datetime
from pyrogram import enums
from config import OWNER_ID
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from AFROTOMusic import app
from AFROTOMusic.plugins.play.filters import command
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatPermissions, ChatPrivileges
from config import *
from pyrogram.enums import ChatMembersFilter
import asyncio
import requests
from AFROTOMusic import app
from AFROTOMusic.core.call import Zelzaly
from AFROTOMusic.utils.database import set_loop
from AFROTOMusic.utils.decorators import AdminRightsCheck
from datetime import datetime
from config import BANNED_USERS, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from AFROTOMusic.utils import bot_sys_stats
from AFROTOMusic.utils.decorators.language import language
import random
import time
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
from aiohttp import ClientSession
from traceback import format_exc
import config
import re
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton, ChatPermissions, InlineKeyboardMarkup, Message, User)
from pyrogram import Client, filters
from AFROTOMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
import os
from pyrogram.errors import PeerIdInvalid
from os import getenv
from AFROTOMusic.misc import SUDOERS
from pyrogram import filters, Client
from telegraph import upload_file
from dotenv import load_dotenv
from AFROTOMusic.utils.database import (set_cmode,get_assistant) 
from AFROTOMusic.utils.decorators.admins import AdminActual
from AFROTOMusic import app
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)

mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)

welcome_enabled = True


def is_owner(_, __, message):

    return message.from_user.id == OWNER_ID



chat_locked = False
mention_locked = False
video_locked = False
link_locked = False
sticker_locked = False
smsim_locked = False
forward_locked = False
reply_locked = False
photo_locked = False
saap_locked = False
rdods_locked = False


@app.on_chat_member_updated()
async def welcome(client, chat_member_updated):
    if not welcome_enabled:
        return
    
    if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            messagee = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nعذرًا، لم استطع حظر الإداري بسبب: {str(e)}"
            else:
                message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"
            
            
        
        await client.send_message(chat_member_updated.chat.id, message)


mutorn = {}

def is_mutor(user_id):
    return user_id in mutorn and mutorn[user_id] > 0


        
        
        
@app.on_message(command(['رتبتي']), group=2889933100)
async def ororhe(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    bot_name = me.first_name
    italy = message.from_user.mention
    button = InlineKeyboardButton("AFROTOO", url=f"https://t.me/UI_VM")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 6988786007:
             rank = "رتبتك ⊱ صاحب سورس عفرتو\n༄"
        elif is_malleka(user_id):    
             rank = "رتبتك ⊱ مالك في الجروب\n༄"
        elif user_id == OWNER_ID:
             rank = "رتبتك ⊱ مطور البوت\n༄"
        elif is_mutornn(user_id):    
             rank = "رتبتك ⊱ ادمن\n༄ "     
        elif ChatMemberStatus.ADMINISTRATOR:
             rank = "حجي انت عضو حقير\n༄"            
        elif ChatMemberStatus.OWNER:
             rank = "رتبتك ⊱ مالك الجروب\n༄"
        else:
             rank = "حجي انت عضو حقير\n༄"
    except Exception as e:
        print(e)
        rank = "مش عرفنلو مله ده😒"
    await message.reply_text(f"{rank}")       
        
        
