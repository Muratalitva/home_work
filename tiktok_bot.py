from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, FSMContext
from config import token
import os,time,requests.logging

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage = storage)
logging.basicConfig(level = logging.INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет! {message.from_user.full_name}")

@dp.message_handler()
async def download_send_video(message:types.Message):
    await message.answer("Скачивание видео...")

executor.start_polling(dp)