from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio

API_TOKEN = '5957089360:AAH8fzbYxyZN1zGXkCJCV2cmWGn8P5K6Px0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Placeholder for storing user goals
user_goals = {}

@dp.message(commands=['start'])
async def send_welcome(message: Message):
    await message.answer("Welcome! Please send me your starting (minimal) daily goal and your end (maximal) daily goal, separated by a space.")

@dp.message()
async def set_goals(message: Message):
    user_id = message.from_user.id
    try:
        start_goal, end_goal = map(int, message.text.split())
        user_goals[user_id] = {'start_goal': start_goal, 'end_goal': end_goal}
        await message.answer(f"Got it! Your starting goal is {start_goal} and your end goal is {end_goal}.")
    except ValueError:
        await message.answer("Please enter your goals correctly, separated by a space.")

async def main():
    # Start polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
