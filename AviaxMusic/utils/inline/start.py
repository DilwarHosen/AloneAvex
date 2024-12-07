from pyrogram.types import InlineKeyboardButton

import config
from AviaxMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=" Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⛦",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+",
            )
        ],
        [
            InlineKeyboardButton(
                text=" Hᴇʟᴩ ",
                callback_data="settings_back_helper"
            ),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="+ Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ +",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+",
            )
        ],
        [
            InlineKeyboardButton(
                text="Hᴇʟᴩ", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="Uᴘᴅᴀᴛᴇs", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="Oᴡɴᴇʀ", user_id=config.OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="[❄️] Iɴᴛʀᴏᴅᴜᴄᴛɪᴏɴ [❄️]", url=f"https://t.me/addlist/MFlGJNbdpco3NTll"
            )
        ],
     ]
    return buttons
