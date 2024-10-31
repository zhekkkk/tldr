from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'start bot'),
        types.BotCommand('help', 'help me'),
        types.BotCommand('summ', 'summarize text')
    ])
