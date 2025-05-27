from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, TelegramSubscriber
from services.telegram.telegram_utils import send_telegram_message

@receiver(post_save, sender=Message)
def send_message_to_telegram(sender, instance: Message, created: bool, **kwargs):
    if created:
        result = send_telegram_message(instance, TelegramSubscriber.get_valid_subscribers())
        instance.set_date_of_sending_to_admin(result[0], message=result[1])
