import os
import time
from pprint import pprint

import aiohttp
import requests
from aiogram import types

from loader import dp, bot
from utils.photograph import photo_link


@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    start = time.time()
    pprint(msg.as_json())
    photo = msg.photo[-1]
    link = await photo_link(photo)
    with open('image.png', mode='wb') as file:
        response = requests.get(f'https://roughs.ru/api/remove-bg?url={link}').content
        file.write(response)
    with open('image.png', mode='rb') as file:
        
    await msg.reply_document(f'https://roughs.ru/api/remove-bg?url={link}')
    print(time.time() - start)
