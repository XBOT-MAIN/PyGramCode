from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from StringGenBot import sessionCli

START_MESSAGE = (
        '𝘏𝘦𝘺 𝘞𝘦𝘭𝘊𝘰𝘮𝘦 𝘛𝘰 𝘋𝘦𝘊𝘰𝘥𝘦 𝘚𝘦𝘚𝘴𝘪𝘰𝘯-𝘎𝘦𝘯𝘉𝘰𝘵\n𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘜𝘴 𝘍𝘰𝘳 𝘔𝘰𝘳𝘦 𝘉𝘦𝘴𝘵 𝘉𝘰𝘵𝘴' 
    )

KEYBOARD = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text='Sᴜᴘᴘᴏʀᴛ', callback_data='sele_support')],
        [InlineKeyboardButton(text='Sᴇssɪᴏɴʙᴏᴛ', callback_data='sele_generator')]
    ]
)

@sessionCli.on_message(filters.command('start'))
async def start(sessionCli, message):
    await message.reply(
        text=START_MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=True
    )
