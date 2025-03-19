from django.contrib import admin
from .models import Message, Review

@admin.register(Message)  # Декоратор для регистрации модели
class MessageAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "created_date", "date_of_sending_to_admin")  # Поля, которые будут показаны в списке
    search_fields = ("author",)  # Поля, по которым можно искать
    list_filter = ("created_date",)  # Фильтры справа
    ordering = ("-created_date",)  # Сортировка по дате создания (новые сверху)
    readonly_fields = ("created_date",)  # Поля, которые нельзя редактировать


@admin.register(Review)  # Декоратор для регистрации модели
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "created_date")  # Поля, которые будут показаны в списке
    search_fields = ("author",)  # Поля, по которым можно искать
    ordering = ("-created_date",)  # Сортировка по дате создания (новые сверху)