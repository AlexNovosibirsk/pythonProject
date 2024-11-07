from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоимость"),
            KeyboardButton(text="О нас")
        ]
    ], resize_keyboard=True)


catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Средняя игра", callback_data='medium')],
        [InlineKeyboardButton(text="Большая игра", callback_data='big')],
        [InlineKeyboardButton(text="Очень боьшая игра", callback_data='mega')],
        [InlineKeyboardButton(text="Другое предложение", callback_data='other')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", url='http://ya.ru')]
    ]
)