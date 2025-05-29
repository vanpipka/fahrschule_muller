import requests
import json
from fahrschule_muller.models import Message, TelegramSubscriber
from decouple import config

TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_API_TOKEN")
TELEGRAM_CHAT_ID = config("TELEGRAM_BOT_CHAT_ID")

def send_telegram_message(message: Message, subscribers: list[TelegramSubscriber]) -> tuple[bool, str]:

    if not subscribers:
        return (False, "No subscribers found.")
    
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'

    headers = {'Content-Type': 'application/json'}
    data = {'text': build_admin_notification_message(message)}

    result = (False, "Unspecified error")

    for subscriber in subscribers:

        data['chat_id'] = subscriber.chat_id

        try:
            response = requests.post(url, headers=headers, data=json.dumps(data))       
            response.raise_for_status()
        except requests.RequestException as e:
            result = (False, e)
        else:
            if response.status_code == 200:
                result = (True, "message sent successfully")
            else:
                result = (False, f'{response.status_code} - {response.text}')
            
    return result


def build_admin_notification_message(message: Message) -> str:
    
    return (
        f"📨 Новое сообщение с сайта!\n\n"
        f"🧾 Форма: {message.form_name}\n"
        f"👤 Автор: {message.author or 'Не указано'}\n"
        f"📞 Контакт: {message.phone_number or 'Не указано'}\n"
        f"➡️ Как связаться: {message.connection_type or 'Не указано'}\n"
        f"🌐 Страница: {message.url or 'Не указано'}\n"
        f"💬 Сообщение:\n{message.text}"
    )