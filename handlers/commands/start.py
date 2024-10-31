from aiogram import types
from aiogram.filters.command import Command

from loader import dp

@dp.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f'hello {message.from_user.full_name}! \n'
                         f'bot is started! write /help for info')