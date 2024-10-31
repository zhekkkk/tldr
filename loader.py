from aiogram import Bot, types, Dispatcher

from data import config 

bot = Bot(token=config.BOT_TOKEN)

dp = Dispatcher()
