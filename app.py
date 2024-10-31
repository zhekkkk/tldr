import asyncio
from handlers import dp
from loader import bot

from utils.set_bot_commands import set_default_commands

async def on_startup(dp):
    set_default_commands(dp)

async def main(dp, bot):
    await dp.start_polling(bot, on_startup=on_startup)

if __name__=='__main__':
    asyncio.run(main(dp, bot))