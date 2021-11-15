import os
import time
import requests
from loader import dp
from pathlib import Path
from aiogram import types

BASE_DIR = Path(__file__).resolve().parent.parent.parent


@dp.message_handler(content_types=['photo'])
async def photo_handler(msg: types.Message):
    start = time.time()
    get_url = await msg.photo[-1].get_url()
    with open(f'remove_img_{msg.from_user.id}.png', mode='wb') as file:
        response = requests.get(f'https://roughs.ru/api/remove-bg?url={get_url}').content
        file.write(response)

    path_img = os.path.join(BASE_DIR, f'remove_img_{msg.from_user.id}.png')

    img = open(path_img, 'rb')
    await msg.reply_photo(img)
    time.sleep(0.5)
    await msg.reply_document(img)
    img.close()
    os.remove(path_img)
    print(time.time() - start)
