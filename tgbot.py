mport asyncio
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command

TOKEN = '8046896929:AAEiWp2D7-6quUqVFxOhn96HwHzchIwsDpg'
tg_channel = ''
user_data = {}

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message:types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    await message.answer(f"Assalomu alaykum! Iltimos ismingizni kiriting:")
    await ask_phone(message)
    print(user_data)
