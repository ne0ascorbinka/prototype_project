from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
from utils import geometric_progression_value

API_TOKEN = '7147813660:AAEvpcci79JHLiA45Q6VXYq_3xkyZ4RGHy0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Placeholder for storing user goals
user_goals = {}

@dp.message(F.text.lower().startswith("day"))
async def read_day(message: Message):
    day = int(message.text.split()[1])
    min, max = user_goals[message.from_user.id]

    try: 
        daily_goal = geometric_progression_value(min, max, day)
        await message.answer(f"Day #{day}:\n{daily_goal}")
    except:
        await message.answer("Error! :(\nCheck your input data more thoroughly")
        

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Welcome! Please send me your starting (minimal) daily goal and your end (maximal) daily goal, separated by a space.")

@dp.message()
async def set_goals(message: Message):
    user_id = message.from_user.id
    try:
        start_goal, end_goal = map(int, message.text.split())
        user_goals[user_id] = (start_goal, end_goal)
        await message.answer(f"Got it! Your starting goal is {start_goal} and your end goal is {end_goal}.")
    except ValueError:
        await message.answer("Please enter your goals correctly, separated by a space.")

async def main():
    # Start polling
    print("starting...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
