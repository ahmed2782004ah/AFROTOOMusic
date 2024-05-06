from pyrogram.enums import ParseMode

from AFROTOMusic import app
from AFROTOMusic.utils.database import is_on_off
from config import OWNER_ID

class Zelzaly(Client):
    def __init__(self):
        OWNER_ID("ميــوزك عفرتو").info(f"جارِ بدء تشغيل البوت . . .")
        super().__init__(
            name="AFROTOMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.OWNER_ID,
                text=f"<u><b>» تم تشغيل الميـوزك لـ البوت {self.mention} :</b><u>\n\n- ɪᴅ : <code>{self.id}</code>\n- ɴᴀᴍᴇ : {self.name}\n- ᴜsᴇʀɴᴀᴍᴇ : @{self.username}",
            )
            exit()
            OWNER_ID("ميــوزك عفرتو").info(f" تم بدء تشغيل البوت {self.name} ...✓")

    async def stop(self):
        await super().stop()
