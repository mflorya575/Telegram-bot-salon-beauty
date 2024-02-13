from aiogram import Bot, Dispatcher, executor, types
import asyncio
import logging
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Импортируем созданные ранее файлы
from config import *
from keyboards import *
import texts


# --------------------------------------------------------#
# Ваш API токен
api = API
logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
# --------------------------------------------------------#

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'✅ Добро пожаловать!\n\n' + texts.start, reply_markup=start_kb)

# Обработчик нажатия на кнопку 'О нас'
@dp.message_handler(Text(equals=['ℹ️ О нас']))
async def aboutas(message):
    await message.answer(texts.about_us, parse_mode='HTML', reply_markup=start_kb)

# Обработчик нажатия на кнопку 'Прейскурант'
@dp.message_handler(Text(equals=['📝 Прейскурант']))
async def aboutas(message):
    await message.answer('<b>Выберите интересующую вас услугу</b>', parse_mode='HTML', reply_markup=catalog_kb)

# Обработка кнопки "Маникюр"
@dp.callback_query_handler(text='Маникюр')
async def manikur(call):
    await call.message.answer(texts.manikur, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "Педикюр"
@dp.callback_query_handler(text='Педикюр')
async def pedikur(call):
    await call.message.answer(texts.pedikur, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "Наращивание"
@dp.callback_query_handler(text='Наращивание')
async def narast(call):
    await call.message.answer(texts.narast, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

# Обработка кнопки "Другие предложения"
@dp.callback_query_handler(text='Другие предложения')
async def other(call):
    await call.message.answer(texts.other, parse_mode='HTML', reply_markup=buy_kb)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

