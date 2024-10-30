from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "  "
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text=['Text', 'text'])
async def first_message(message):
    print("first_message")

@dp.message_handler(commands=["start"])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

"""
C:\module_13\mvenv\Scripts\python.exe C:\module_13\module_13_2.py 
Updates were skipped successfully.
Введите команду /start, чтобы начать общение.
Привет! Я бот помогающий твоему здоровью.
first_message
Goodbye!

Process finished with exit code 0
"""