import uuid
from django.db import models
from django.utils import timezone


class Message(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=200, default="")
    form_name = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=200, default="")
    url = models.CharField(max_length=500, default="")
    text = models.TextField(default="")
    created_date = models.DateTimeField(default=timezone.now)
    date_of_sending_to_admin = models.DateTimeField(blank=True, null=True)
    result_of_sending_to_admin = models.TextField(blank=True, default="")

    def set_date_of_sending_to_admin(self, result_of_sending_to_admin: bool, message: str = ""):
        
        self.date_of_sending_to_admin = timezone.now()
        self.result_of_sending_to_admin = message
        self.save(update_fields=['date_of_sending_to_admin', 'result_of_sending_to_admin'])

    def __str__(self):
        return self.form_name
    
    
class Review(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=200)
    type = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=600)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __save__(self):
        
        if "google" in self.url:
            self.type = "google"
        elif "clickclick" in self.url:
            self.type = "clickclick"
        else:
            self.type = ""
    
        print(self.type)


class TelegramSubscriber(models.Model):

    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def get_valid_subscribers():
        return list(TelegramSubscriber.objects.filter(is_valid=True).all())

    def __str__(self):
        return f"{self.username or self.chat_id}"