import os
import sys
import django
from pathlib import Path
from asgiref.sync import sync_to_async

# --- Django setup ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fahrschule_muller.settings')
django.setup()

from fahrschule_muller.models import TelegramSubscriber
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.client.default import DefaultBotProperties
from decouple import config

# --- Aiogram v3 ---
API_TOKEN = config("TELEGRAM_BOT_API_TOKEN")

bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
router = Router()

# --- Обработчик команды /start ---
@router.message(CommandStart())
async def handle_start(message: Message):

    print(f"%TG_BOT% Subscribing user: {message.from_user.username or message.from_user.id} (chat_id: {message.chat.id})")
    chat_id = message.chat.id
    username = message.from_user.username or ""

    # Обертываем Django ORM в sync_to_async
    subscriber, created = await sync_to_async(TelegramSubscriber.objects.get_or_create)(chat_id=chat_id)
    subscriber.username = username
    await sync_to_async(subscriber.save)()

    await message.answer("✅ Вы подписаны на уведомления.")

# --- Обработчик команды /stop ---
@router.message(Command("stop"))
async def handle_stop(message: Message):
    print(f"%TG_BOT% Unsubscribing user: {message.from_user.username or message.from_user.id} (chat_id: {message.chat.id})")
    await sync_to_async(TelegramSubscriber.objects.filter(chat_id=message.chat.id).delete)()
    await message.answer("❌ Вы отписались от уведомлений.")

# --- Обработчик текстовых сообщений ---
@router.message(F.text)
async def echo(message: Message):
    print(f"%TG_BOT% Received message: {message.text} from {message.from_user.username or message.from_user.id}")
    await message.answer("Это бот рассылки. Используйте /start для подписки или /stop для отписки.")

# --- Регистрация роутера ---
dp.include_router(router)

# --- Запуск бота ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    print("%TG_BOT% Starting Telegram bot...")
    asyncio.run(main())
