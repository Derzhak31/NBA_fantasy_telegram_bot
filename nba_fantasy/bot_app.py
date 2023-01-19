import asyncio
import logging
from handlers import client
from create_bot import dp, bot

logging.basicConfig(level=logging.DEBUG, filename='py_log.log', filemode='w', format="%(asctime)s %(levelname)s %(message)s")


async def main():
    
    client.register_handlers_client(dp)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())