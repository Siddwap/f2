# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, I am SD File Stream Bot. Send me any telegram file to get an instant Download and Stream link. You can directly download any file or Watch online. ',
                  reply_markup=InlineKeyboardMarkup(
                      [[
                            InlineKeyboardButton(
                                  f'{emoji.STAR} Made by Shuaib Siddiqui  {emoji.STAR}',
                                  url='https://t.me/shuaib_siddiqui')
                        ]]
                  ))
