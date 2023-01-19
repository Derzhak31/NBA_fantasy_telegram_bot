from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder=f'🏀что посмотрим?🏀')
start_b1 = KeyboardButton('Календарь')
start_b2 = KeyboardButton('Таблицы')
kb_start.add(start_b1, start_b2)

