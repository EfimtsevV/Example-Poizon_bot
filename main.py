from aiogram import Bot, types, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
import asyncio
import logging

from src.config import TOKEN
from src.text import start_message_text

logging.basicConfig(level=logging.INFO)
router = Router()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
dp.include_router(router)

keyboard = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Наши отзывы!📖', url='https://t.me/re_stylee', type='url')
urlButton2 = InlineKeyboardButton(text='Тех.поддержка 👨🏻‍💻', url='@n1let7', type='url')
urlButton3 = InlineKeyboardButton(text='Наш Telegram', url='https://t.me/restyle_shop', type='url')
urlButton4 = InlineKeyboardButton(text='Мы есть на Авито!', url='https://www.avito.ru/brands/fb5ec54987ddf9def727470a228c2d1b?src=sharing', type='url')
keyboard.add(urlButton, urlButton2, urlButton3, urlButton4)

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.finish()
    await msg.answer(start_message_text, reply_markup=keyboard)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())