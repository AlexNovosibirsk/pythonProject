from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio
from config import API
import re

str_warning = "Задавайте только целые числа"
tuple_data = dict()

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Информация")
        ]
    ], resize_keyboard=True)


inline_menu = InlineKeyboardMarkup(resize_keyboard=True)
inl_button1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inl_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_menu.row(inl_button1, inl_button2)


def calories_calculate(data: dict):
    calories_for_male = 10 * data['weight'] + 6.25 * data['growth'] + 5 * data['age'] + 5
    calories_for_female = 10 * data['weight'] + 6.25 * data['growth'] + 5 * data['age'] - 161
    return calories_for_male, calories_for_female


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=start_menu)


@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_menu)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес(кг)+6,25 x рост(см)–5 x возраст(г)–161\n'
                              '10 x вес(кг)+6,25 x рост(см)–5 x возраст(г)–5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer("Укажите свой возраст:")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()

    match = re.match(r'\d{1,3}', data['age'])
    if match is not None:
        tuple_data['age'] = int(match[0])
        await message.answer(f"Ваш возраст: {match[0]}. Укажите свой рост:")
        await UserState.growth.set()
    else:
        await message.answer(str_warning)


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()

    match = re.match(r'\d{1,3}', data['growth'])
    if match is not None:
        tuple_data['growth'] = int(match[0])
        await message.answer(f"Ваш рост: {match[0]}, Укажите свой вес:")
        await UserState.weight.set()
    else:
        await message.answer(str_warning)


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    match = re.match(r'\d{1,3}', data['weight'])
    if match is not None:
        await message.answer(f"Ваш вес: {match[0]}")
        tuple_data['weight'] = int(match[0])
        calories_for_male, calories_for_female = calories_calculate(tuple_data)
        await message.answer(f"Норма калории для мужчин: {calories_for_male}")
        await message.answer(f"Норма калории для женщин: {calories_for_female}")
        await state.finish()
    else:
        await message.answer(str_warning)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
