from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards import kb_start, ikb_table
from data import eastern, western, atlantic, central, northwest, pacific, southeast, southwest


async def cmd_start(message: types.Message):
    await message.answer(f'🏀что посмотрим?🏀', reply_markup=kb_start())
    await message.delete()


# async def cmd_calendar(message: types.Message):
#     await message.answer('Календарь')
#     await message.delete()


async def cmd_table(message: types.Message):
    await message.answer('🏀Выберите таблицу🏀', reply_markup=ikb_table())
    await message.delete()


async def callback_table(callback: types.CallbackQuery):
    action = callback.data.split('_')[1]
    if action == 'eastern':
        await callback.message.answer(eastern())
    elif action == 'western':
        await callback.message.answer(western())
    elif action == 'atlantic':
        await callback.message.answer(atlantic())
    elif action == 'central':
        await callback.message.answer(central())
    elif action == 'northwest':
        await callback.message.answer(northwest())
    elif action == 'pacific':
        await callback.message.answer(pacific())
    elif action == 'southeast':
        await callback.message.answer(southeast())
    elif action == 'southwest':
        await callback.message.answer(southwest())
    await callback.answer()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    # dp.register_message_handler(cmd_calendar, Text(equals='Календарь'))
    dp.register_message_handler(cmd_table, Text(equals='Таблицы'))
    dp.register_callback_query_handler(callback_table, Text(startswith='bt_'))
