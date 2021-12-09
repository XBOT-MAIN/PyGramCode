from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from StringGenBot import sessionCli

@sessionCli.on_callback_query(filters.create(lambda _, __, query: 'sele_telethon' in query.data))
async def HardGen(sessionCli, callback_data):
    user_id = callback_data.from_user.id

    await sessionCli.edit_messages(
            chat_id=user_id,

            text=f"Please Choose Your Option From Below\n__Powered By - @DeCodeSupport__", 
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                    InlineKeyboardButton(text="Telethon", callback_data='sele_telethon'),
                    InlineKeyboardButton(text="Pyrogram", callback_data='sele_pyrogram')
                 ]
                ]
            ), 
        ) 
