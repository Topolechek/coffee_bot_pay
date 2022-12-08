from aiogram import types

from data.config import barista_id
from loader import dp
from states import Test


@dp.message_handler(user_id=barista_id, text='/open', state=Test.test_x)
async def command_open(message: types.Message):
    await message.answer('Вы вошли как Бариста')
