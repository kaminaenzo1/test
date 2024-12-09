import asyncio
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
async def ask_phone(message:types.Message):
    user_id = message.from_user.id
    name = message.text
    user_data[user_id]['name'] = name
    button = [
        [types.KeyboardButton(text='Share Contact',request_contact=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button,one_time_keyboard=True,resize_keyboard=True)
    await message.answer(f"Iltimos telefon raqamingizni jo'nating",reply_markup=keyboard)
    print(user_data)
     await ask_age(message)




async def ask_age(message:types.Message):
    user_id = message.from_user.id
    if message.contact is not None:
        phone = message.contact,phone_number
    else:
        phone=message.text
    user_data[user_id]['phone'] = phone
    await message.answer(f"Iltimos yoshingizni kiriting")
    print(user_data)
