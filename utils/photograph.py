from io import BytesIO
import aiohttp
from aiogram import types
from loader import bot
from telegraph import upload_file
async def photo_link(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        get = upload_file(file)

    link = 'http://telegra.ph' + get[0]
    return link