import os
import time
from io import BytesIO
from pprint import pprint

import aiohttp
import requests
from aiogram import types
from loader import dp, bot
from utils.photograph import photo_link


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    start = time.time()
    chat_id = msg.from_user.id
    photo = msg.photo[-1]
    link = await photo_link(photo)
    image_content = requests.get(f'https://roughs.ru/api/remove-bg?url={link}').content
    with open(f'image_{chat_id}.png', mode='wb') as file:
        file.write(image_content)

    with open(f'image_{chat_id}.png', 'rb') as file:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=file,
        )
        async with bot.session.post('https://telegra.ph/upload', data=form) as response:
            img_src = await response.json()
    pprint(img_src)
    # with open(f'image_{chat_id}.png', mode='rb') as file:
    #     await msg.reply_photo(file)
    #     await msg.reply_document(document=file)
    # print(time.time() - start)