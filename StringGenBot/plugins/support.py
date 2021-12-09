from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from StringGenBot import sessionCli

@sessionCli.on_callback_query(filters.create(lambda _, __, query: 'sele_support' in query.data))
async def HelpGen(sessionCli, callback_data):
    user_id = callback_data.from_user.id
    
    await sessionCli.edit_messages(
            chat_id=user_id,

            text=f"𝘏𝘦𝘳𝘦 𝘐𝘴 𝘋𝘦𝘵𝘢𝘪𝘭𝘴 𝘈𝘣𝘰𝘶𝘵 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘈𝘯𝘥 𝘊𝘩𝘢𝘯𝘯𝘦𝘭\𝘯__𝘗𝘰𝘸𝘦𝘳𝘦𝘥𝘉𝘺 - @𝘛𝘦𝘢𝘮𝘋𝘦𝘦𝘊𝘰𝘥𝘦__", 
            reply_markup=InlineKeyboardMarkup(
                [
                 [
                  InlineKeyboardButton(text='𝘎𝘳𝘰𝘶𝘱', url="t.me/decodesupport"), 
                  InlineKeyboardButton(text='Channel', url="t.me/DeeCodeBots")
                 ], 
                 [
                  InlineKeyboardButton(text='𝘋𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳𝘴', url="t.me/DeeCodeDevs"),
                 ]
                ]
            ), 
        ) 
