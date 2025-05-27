from django.contrib import admin
from .models import Message, Review, TelegramSubscriber

@admin.register(Message)  # Декоратор для регистрации модели
class MessageAdmin(admin.ModelAdmin):
    list_display = ("author", "phone_number", "created_date", "date_of_sending_to_admin", "result_of_sending_to_admin")  # Поля, которые будут показаны в списке
    search_fields = ("author",)  # Поля, по которым можно искать
    list_filter = ("created_date",)  # Фильтры справа
    ordering = ("-created_date",)  # Сортировка по дате создания (новые сверху)
    readonly_fields = ("created_date",)  # Поля, которые нельзя редактировать


@admin.register(Review)  # Декоратор для регистрации модели
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "created_date")  # Поля, которые будут показаны в списке
    search_fields = ("author",)  # Поля, по которым можно искать
    ordering = ("-created_date",)  # Сортировка по дате создания (новые сверху)


@admin.register(TelegramSubscriber)  # Декоратор для регистрации модели
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "username", "subscribed_at", "is_valid")  # Поля, которые будут показаны в списке
    ordering = ("-subscribed_at",)  # Сортировка по дате создания (новые сверху)