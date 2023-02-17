import asyncio
import logging
from create_bot import dp, bot
from handlers import register_handlers_client

logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")


async def main():
    print('Бот вышел в онлайн!')
    register_handlers_client(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
