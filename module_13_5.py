from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

api = "   "
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb.row(button1, button2)

str_warning = "Задавайте только целые числа"


def calories_calculate(data):
    calories_for_male = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    calories_for_female = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) - 161
    return calories_for_male, calories_for_female


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=["Информация"])
async def information(message):
    await message.answer("Я бот помогающий твоему здоровью.")


@dp.message_handler(text=["Рассчитать"])
async def set_age(message):
    await message.answer("Укажите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()

    if not data['age'].isdigit():
        await message.answer(str_warning)
    else:
        await message.answer(f"Ваш возраст: {data['age']}. Укажите свой рост:")
        await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()

    if not data['growth'].isdigit():
        await message.answer(str_warning)
    else:
        await message.answer(f"Ваш рост: {data['growth']}, Укажите свой вес:")
        await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    if not data['weight'].isdigit():
        await message.answer(str_warning)
    else:
        calories_for_male, calories_for_female = calories_calculate(data)
        await message.answer(f"Норма калории для мужчин: {calories_for_male}")
        await message.answer(f"Норма калории для женщин: {calories_for_female}")
        await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
