from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from StringGenBot import sessionCli

START_MESSAGE = (
        '๐๐ฆ๐บ ๐๐ฆ๐ญ๐๐ฐ๐ฎ๐ฆ ๐๐ฐ ๐๐ฆ๐๐ฐ๐ฅ๐ฆ ๐๐ฆ๐๐ด๐ช๐ฐ๐ฏ-๐๐ฆ๐ฏ๐๐ฐ๐ต\n๐๐ถ๐ฑ๐ฑ๐ฐ๐ณ๐ต ๐๐ด ๐๐ฐ๐ณ ๐๐ฐ๐ณ๐ฆ ๐๐ฆ๐ด๐ต ๐๐ฐ๐ต๐ด' 
    )

KEYBOARD = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text='Sแดแดแดแดสแด', callback_data='sele_support')],
        [InlineKeyboardButton(text='Sแดssษชแดษดสแดแด', callback_data='sele_generator')]
    ]
)

@sessionCli.on_message(filters.command('start'))
async def start(sessionCli, message):
    await message.reply(
        text=START_MESSAGE,
        reply_markup=KEYBOARD,
        disable_web_page_preview=True
    )
