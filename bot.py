import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv

from routers.user_handler import user_private_router

load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message, edited_message']
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(user_private_router)


async def on_startup(bot):
    print('Bot start')


async def on_shutdown(bot):
    print('Bot end')

async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES),


asyncio.run(main())
