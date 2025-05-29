import uuid
from django.db import models
from django.utils import timezone


class Message(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=200, default="", blank=True)
    form_name = models.CharField(max_length=200, default="", blank=True)
    phone_number = models.CharField(max_length=200, default="", blank=True)
    connection_type = models.CharField(max_length=50, default="", blank=True)
    url = models.CharField(max_length=500, default="", blank=True)
    text = models.TextField(default="", blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    date_of_sending_to_admin = models.DateTimeField(blank=True, null=True)
    result_of_sending_to_admin = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = "Запрос с сайта"
        verbose_name_plural = "Запросы с сайта"

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

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __save__(self):
        
        if "google" in self.url:
            self.type = "google"
        elif "clickclick" in self.url:
            self.type = "clickclick"
        else:
            self.type = ""
    


class TelegramSubscriber(models.Model):

    chat_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    is_valid = models.BooleanField(default=False)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Учетная запись Telegram"
        verbose_name_plural = "Учетные записи Telegram"

    def __str__(self):
        return f"{self.username or self.chat_id}"


class OrderItemType(models.Model):

    title = models.CharField(max_length=255, default="", verbose_name="Тип товара")

    class Meta:
        verbose_name = "Тип товара"
        verbose_name_plural = "Типы товаров"
        
    def __str__(self):
        return f"{self.title}"
    

class OrderItem(models.Model):

    title = models.CharField(max_length=255, default="", verbose_name="Название товара")
    type = models.ForeignKey(OrderItemType, on_delete=models.CASCADE, verbose_name="Тип товара")
    image = models.FileField(upload_to="order_files/", blank=True, verbose_name="Изображение")
    article_number = models.CharField(max_length=50, default="", verbose_name="Артикул")
    description = models.TextField(max_length=100, default="", blank=True, verbose_name="Короткое описание для карточки товара")
    full_description = models.TextField(default="", blank=True, verbose_name="Подробное описание")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        
    def __str__(self):
        return f"{self.title} ({self.article_number})"