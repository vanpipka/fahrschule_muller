from django.contrib import admin
from .models import Category, Question, Thema, Type


@admin.register(Category)  # Декоратор для регистрации модели
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Поля, которые будут показаны в списке
    search_fields = ("name",)  # Поля, по которым можно искать
    readonly_fields = ("id",)  # Поля, которые нельзя редактировать


@admin.register(Thema)  # Декоратор для регистрации модели
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Поля, которые будут показаны в списке
    search_fields = ("name",)  # Поля, по которым можно искать
    readonly_fields = ("id",)  # Поля, которые нельзя редактировать


@admin.register(Type)  # Декоратор для регистрации модели
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)  # Поля, которые будут показаны в списке
    search_fields = ("name",)  # Поля, по которым можно искать
    readonly_fields = ("id",)  # Поля, которые нельзя редактировать
    

@admin.register(Question)  # Декоратор для регистрации модели
class ProductAdmin(admin.ModelAdmin):
    list_display = ("category", "description")  # Поля, которые будут показаны в списке
    search_fields = ("description",)  # Поля, по которым можно искать
    readonly_fields = ("id",)  # Поля, которые нельзя редактировать
    list_filter = ("category",)  # Фильтры справа