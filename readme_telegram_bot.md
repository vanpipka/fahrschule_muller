# 🤖 Telegram Notification Bot для Django

Этот проект реализует асинхронного Telegram-бота на базе [Aiogram v3](https://docs.aiogram.dev/en/dev-3.x/) с интеграцией в Django. 
Бот предоставляет систему подписки/отписки на уведомления, сохраняя данные пользователей в базе Django.

---

## 📦 Стек технологий

- **Python 3.10+**
- **Django**
- **Aiogram v3**
- **python-decouple**
- **asgiref** (`sync_to_async` для доступа к ORM из async-контекста)

---

## 🚀 Возможности

- `/start` — подписка на уведомления (сохраняет chat_id и username).
- `/stop` — отписка (удаляет пользователя из базы).
- Обработка любых других текстовых сообщений — отправляет справочную информацию.
- Интеграция с Django ORM без блокировки asyncio.

---

## 🧱 Структура проекта

- your_project/
- ├── fahrschule_muller/
- │ ├── init.py
- │ ├── settings.py
- │ └── models.py # Модель TelegramSubscriber
- ├── telegram_bot/
- │ └── telegram_bot.py # Основной скрипт бота
- ├── .env # Конфигурация токена бота

---

## ⚙️ Переменные окружения

- Создай файл .env в корне проекта: TELEGRAM_BOT_API_TOKEN=your_telegram_bot_token

---

## 🏁 Запуск бота

- python telegram_bot/telegram_bot.py

---