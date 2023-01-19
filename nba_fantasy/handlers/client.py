from keyboards import kb_start
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from actions.match import match, standings


async def cmd_start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'🏀{name}, что посмотрим?🏀', reply_markup=kb_start)
    await message.delete()

async def cmd_calendar(message: types.Message):
    await message.answer(match())
    await message.delete()

async def cmd_table(message: types.Message):
    await message.answer(standings())
    await message.delete()



def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_calendar, Text(equals='Календарь'))
    dp.register_message_handler(cmd_table, Text(equals='Таблицы'))