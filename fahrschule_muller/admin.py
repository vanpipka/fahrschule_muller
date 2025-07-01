from django.contrib import admin
from .models import Message, Review, TelegramSubscriber, OrderItem, OrderItemType, Anmeldung, AsfCourse, SiteSettings, SiteTexts


@admin.register(SiteSettings)  # Декоратор для регистрации модели
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("phone", "mobile_phone", "email", "address")  # Поля, которые будут показаны в списке


@admin.register(SiteTexts)  # Декоратор для регистрации модели
class SiteTextsAdmin(admin.ModelAdmin):
    list_display = ("key", "text")  # Поля, которые будут показаны в списке


@admin.register(Message)  # Декоратор для регистрации модели
class MessageAdmin(admin.ModelAdmin):
    list_display = ("author", "phone_number", "created_date", "date_of_sending_to_admin", "result_of_sending_to_admin")  # Поля, которые будут показаны в списке
    search_fields = ("author",)  # Поля, по которым можно искать
    list_filter = ("created_date",)  # Фильтры справа
    ordering = ("-created_date",)  # Сортировка по дате создания (новые сверху)
    readonly_fields = ("created_date",)  # Поля, которые нельзя редактировать


@admin.register(Anmeldung)  # Декоратор для регистрации модели
class Anmeldung(admin.ModelAdmin):
    list_display = ("vorname", "anschrift", "email", "phone", "geburtsdatum", "course", "created_date")  # Поля, которые будут показаны в списке
    # list_filter = ("form_name",)  # Фильтры справа
    ordering = ("-created_date",)  # Сортировка по дате создания (новые сверху)
    readonly_fields = ("created_date",)  # Поля, которые нельзя редактировать


@admin.register(Review)  # Декоратор для регистрации модели
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "created_date")  # Поля, которые будут показаны в списке
    search_fields = ("author",)  # Поля, по которым можно искать
    ordering = ("-created_date",)  # Сортировка по дате создания (новые сверху)
    readonly_fields = ("created_date",)  # Поля, которые нельзя редактировать


@admin.register(TelegramSubscriber)  # Декоратор для регистрации модели
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("chat_id", "username", "subscribed_at", "is_valid")  # Поля, которые будут показаны в списке
    ordering = ("-subscribed_at",)  # Сортировка по дате создания (новые сверху)


@admin.register(OrderItemType)  # Декоратор для регистрации модели
class OrderItemTypeAdmin(admin.ModelAdmin):
    list_display = ("title",)  # Поля, которые будут показаны в списке


@admin.register(OrderItem)  # Декоратор для регистрации модели
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("title", "article_number")  # Поля, которые будут показаны в списке


@admin.register(AsfCourse)  # Декоратор для регистрации модели
class AsfCourseAdmin(admin.ModelAdmin):
    list_display = ("title", "lesson_1_date", "lesson_2_date", "lesson_3_date", "lesson_4_date", "fahrproben")  # Поля, которые будут показаны в списке
    ordering = ("-lesson_1_date",)  # Сортировка по дате создания (новые сверху)