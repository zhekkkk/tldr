from aiogram import types
from aiogram.filters.command import Command
from loader import dp

@dp.message(Command("help"))
async def command_start(message: types.Message):
    await message.answer(f'hello {message.from_user.full_name}! \n'
                         f"write /summarize, send me a document and get a summary of it")