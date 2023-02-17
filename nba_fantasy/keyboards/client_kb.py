from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def kb_start():
    buttons = [
        [
            # KeyboardButton('Календарь'),
            KeyboardButton('Таблицы')
        ]
    ]
    kb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder=f'🏀что посмотрим?🏀')
    return kb


def ikb_table():
    buttons = [
        [
            InlineKeyboardButton(text='Eastern', callback_data='bt_eastern'),
            InlineKeyboardButton(text='Western', callback_data='bt_western')
        ],
        [
            InlineKeyboardButton(text='Atlantic', callback_data='bt_atlantic'),
            InlineKeyboardButton(text='Northwest', callback_data='bt_northwest')
        ],
        [
            InlineKeyboardButton(text='Central', callback_data='bt_central'),
            InlineKeyboardButton(text='Pacific', callback_data='bt_pacific')
        ],
        [
            InlineKeyboardButton(text='Southeast', callback_data='bt_southeast'),
            InlineKeyboardButton(text='Southwest', callback_data='bt_southwest')
        ]
    ]
    ikb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return ikb
