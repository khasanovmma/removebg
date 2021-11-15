from io import BytesIO

from aiogram import types
from telegraph import upload_file


async def photo_link(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        get = upload_file(file)

    link = 'http://telegra.ph' + get[0]
    return link
