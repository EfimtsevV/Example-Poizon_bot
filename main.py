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
# keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [
#                 InlineKeyboardButton(text='Наши отзывы!📖', url='https://t.me/re_stylee', type='url'),
#                 InlineKeyboardButton(text='Тех.поддержка 👨🏻‍💻', url='https://t.me/n1let7', type='url'),
#                 InlineKeyboardButton(text='Наш Telegram', url='https://t.me/restyle_shop', type='url'),
#                 InlineKeyboardButton(text='Мы есть на Авито!', url='https://www.avito.ru/brands/fb5ec54987ddf9def727470a228c2d1b?src=sharing', type='url')
#             ]
#         ]
#     )

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Наши отзывы!📖', url='https://t.me/re_stylee', type='url'),
            InlineKeyboardButton(text='Тех.поддержка 👨🏻‍💻', url='https://t.me/n1let7', type='url')
        ],
        [
            InlineKeyboardButton(text='Наш Telegram', url='https://t.me/restyle_shop', type='url'),
            InlineKeyboardButton(text='Мы есть на Авито!', url='https://www.avito.ru/brands/fb5ec54987ddf9def727470a228c2d1b?src=sharing', type='url')
        ]
    ],
    row_width=2  # Set the row width to 2
)

@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    await state.set_state(None)  # Устанавливаем состояние в None
    await msg.answer(start_message_text, reply_markup=keyboard)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())