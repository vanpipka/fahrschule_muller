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


class Anmeldung(models.Model):

    form_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Имя формы'
    )
    url = models.URLField(
        max_length=500,
        blank=True,
        verbose_name='Источник URL'
    )
    anrede = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Обращение (Herr/Frau)'
    )
    vorname = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Имя'
    )
    nachname = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Фамилия'
    )
    anschrift = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Адрес'
    )
    fuhrerschein = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Категория водительских прав'
    )
    course = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Курс'
    )
    anschrift = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Адрес'
    )
    plz = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Почтовый индекс'
    )
    email = models.EmailField(
        max_length=254,
        blank=True,
        verbose_name='Email'
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Телефон'
    )
    geburtsort = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Место рождения'
    )
    geburtsdatum = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    fristablauf = models.DateField(
        null=True,
        blank=True,
        verbose_name='Срок окончания'
    )
    form_message = models.TextField(
        blank=True,
        verbose_name='Сообщение'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    created_date = models.DateTimeField(default=timezone.now)
    date_of_sending_to_admin = models.DateTimeField(blank=True, null=True)
    result_of_sending_to_admin = models.TextField(blank=True, default="")

    def __str__(self):
        
        return f"{self.vorname} {self.nachname} — {self.form_name or 'Форма'}"
    
    class Meta:
        verbose_name = "ASF заявка"
        verbose_name_plural = "ASF заявки"
    
    def set_date_of_sending_to_admin(self, result_of_sending_to_admin: bool, message: str = ""):
        
        self.date_of_sending_to_admin = timezone.now()
        self.result_of_sending_to_admin = message
        self.save(update_fields=['date_of_sending_to_admin', 'result_of_sending_to_admin'])


class AsfCourse(models.Model):

    title = models.CharField(max_length=255, verbose_name="Название курса")
    lessons_duration = models.IntegerField(verbose_name="Длительность одного занятия в минутах", default=135)
    lesson_1_date = models.DateTimeField(verbose_name="Дата/время первого занятия")
    lesson_2_date = models.DateTimeField(verbose_name="Дата/время второго занятия")  
    lesson_3_date = models.DateTimeField(verbose_name="Дата/время третьего занятия") 
    lesson_4_date = models.DateTimeField(verbose_name="Дата/время четвертого занятия")  
    fahrproben = models.TextField(max_length=100, default="", blank=True, verbose_name="Fahrproben")   
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ASF Курс"
        verbose_name_plural = "ASF Курсы"

    def __str__(self):
        return self.title
