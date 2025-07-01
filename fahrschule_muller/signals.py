from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Anmeldung
from services.models import Notification
from services.db_manager import get_valid_subscribers
from services.telegram.telegram_utils import send_telegram_message

@receiver(post_save, sender=Message)
def send_message_to_telegram(sender, instance: Message, created: bool, **kwargs):

    if created:

        notification = Notification.from_message(instance)
        result = send_telegram_message(notification, get_valid_subscribers())
        instance.set_date_of_sending_to_admin(result[0], message=result[1])

    
@receiver(post_save, sender=Anmeldung)
def send_message_to_telegram(sender, instance: Anmeldung, created: bool, **kwargs):
    
    if created:

        notification = Notification.from_anmeldung(instance)
        result = send_telegram_message(notification, get_valid_subscribers())
        instance.set_date_of_sending_to_admin(result[0], message=result[1])
