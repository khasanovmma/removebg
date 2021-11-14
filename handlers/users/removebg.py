from aiogram import types

from loader import dp
from utils.photograph import photo_link


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    request_link = 'https://roughs.ru/api/remove-bg?url='
    await msg.reply_document(request_link + link, caption="Bu fayl")
    await msg.reply_photo(request_link + link, caption="Bu rasm")
