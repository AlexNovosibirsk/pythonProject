from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = " "
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=["Calories", "Калории"])
async def set_age(message):
    await message.answer("Укажите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer(f"Ваш возраст: {data['age']}. Укажите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer(f"Ваш рост: {data['growth']}, Укажите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories_for_male   = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    calories_for_female = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) - 161
    await message.answer(f"Калории для мужчин: {calories_for_male}")
    await message.answer(f"Калории для женщин: {calories_for_female}")
    await state.finish()

# 1. Упрощенный вариант формулы Миффлина-Сан Жеора:
# для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
# для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
