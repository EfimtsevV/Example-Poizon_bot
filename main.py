from aiogram import Bot, types, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F


import asyncio
import logging



from src.config import TOKEN
from take_curs import cny_rate
from src.text import start_message_text, pozion_text, instruction_text, delivery_text, place_order_text


logging.basicConfig(level=logging.INFO)
router = Router()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
dp.include_router(router)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Наши отзывы📖', url='https://t.me/re_stylee', type='url'),
            InlineKeyboardButton(text='Тех.поддержка👨🏻‍💻', url='https://t.me/n1let7', type='url')
        ],
        [
            InlineKeyboardButton(text='Наш Telegram🔥', url='https://t.me/restyle_shop', type='url'),
            InlineKeyboardButton(text='Мы есть на Авито📦', url='https://www.avito.ru/brands/fb5ec54987ddf9def727470a228c2d1b?src=sharing', type='url')
        ]
    ],
    row_width=2  # Set the row width to 2
)

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Что такое POIZON❓'), KeyboardButton(text='Инструкция по заказу📜')],
        [KeyboardButton(text='Доставка🚚✈️'), KeyboardButton(text='Актуальный курс💹')],
        [KeyboardButton(text='Калькулятор💸'),KeyboardButton(text='Оформить заказ🛒')]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.set_state(None)  # Reset state if needed
    # Send start message with inline keyboard
    await msg.answer(start_message_text, reply_markup=inline_keyboard)
    # Send a separate message to ensure the reply keyboard is set
    await msg.answer("Выберите опцию из меню-клавиатуры:", reply_markup=reply_keyboard)

@router.message(F.text.startswith('Что такое POIZON❓'))
async def send_poizon(message: types.Message, state: FSMContext):
    await state.set_state(None)  # Reset state if needed
    await message.reply(pozion_text)
    

@router.message(F.text.startswith('Инструкция по заказу📜'))
async def send_poizon(message: types.Message, state: FSMContext):
    await state.set_state(None)  # Reset state if needed
    await message.reply(instruction_text, reply_markup=inline_keyboard)
    


@router.message(F.text.startswith('Доставка🚚✈️'))
async def send_poizon(message: types.Message, state: FSMContext):
    await state.set_state(None)  # Reset state if needed
    await message.reply(delivery_text, reply_markup=inline_keyboard)

@router.message(F.text.startswith('Оформить заказ🛒'))
async def send_poizon(message: types.Message, state: FSMContext):
    await state.set_state(None)  # Reset state if needed
    await message.reply(place_order_text, reply_markup=inline_keyboard)
    
@router.message(F.text.startswith('Актуальный курс💹'))
async def send_poizon(message: types.Message, state: FSMContext):
    await state.set_state(None)  # Reset state if needed
    await message.reply(f"Актуальный курс юаня: {(cny_rate+float(1.2)):.2f}₽")
    
class CalculatorStates(StatesGroup):
    waiting_for_price = State()  # Состояние ожидания цены
    
@router.message(F.text.startswith('Калькулятор💸'))
async def calculator_handler(message: types.Message, state: FSMContext):
    await state.set_state(CalculatorStates.waiting_for_price)  # Установить состояние ожидания
    await message.reply("Пожалуйста, введите стоимость позиции в юанях:")

@router.message(CalculatorStates.waiting_for_price)
async def process_price(message: types.Message, state: FSMContext):
    try:
        price_in_cny = float(message.text)  # Преобразовать текст в число
        total_price = price_in_cny * (cny_rate+float(1.2))  # Умножить на курс
        await message.reply(f"Стоимость в рублях: {total_price:.2f}₽")  # Отправить результат
    except ValueError:
        await message.reply("Пожалуйста, введите число.")  # Обработка ошибки
    finally:
        await state.clear()  # Очистить состояние после обработки

async def main():
     try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
     except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())