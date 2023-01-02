from aiogram import types, F
from aiogram.filters import Text

from ..bot import dp


@dp.message()
async def unknown(message: types.Message):
    await message.answer(message.text)

