from datetime import datetime
from fahrschule_muller import models as app_models
from exam import models as exam_models


def check_and_save_anmeldung(data):

    EMPTY_DATE = '0001-01-01'

    geburtsdatum = data.get('geburtsdatum', EMPTY_DATE)
    fristablauf = data.get('fristablauf', EMPTY_DATE)

    if not geburtsdatum:
        geburtsdatum = EMPTY_DATE

    if not fristablauf:
        fristablauf = EMPTY_DATE

    message = app_models.Anmeldung(
        form_name = data.get('form_name', ''), 
        url = data.get('url', ''), 
        anrede = data.get('anrede', ''), 
        vorname = data.get('vorname', ''), 
        nachname = data.get('nachname', ''), 
        anschrift = data.get('anschrift', ''), 
        plz = data.get('plz', ''), 
        email = data.get('email', ''), 
        phone = data.get('phone', ''), 
        geburtsort = data.get('geburtsort', ''), 
        fuhrerschein = data.get('fuhrerschein', ''), 
        course = data.get('course', ''), 
        geburtsdatum = geburtsdatum, 
        fristablauf = fristablauf, 
        form_message = data.get('form_message', '')
    )

    message.save()


def check_and_save_message(message_data):

    message = app_models.Message(
        text = message_data.get('message', ''),
        author = message_data.get('name', ''),
        form_name = message_data.get('form_name', ''),
        phone_number = message_data.get('phone', ''),
        url = message_data.get('url', ''),
        connection_type = message_data.get('connection_type', ''),
    )

    message.save()

    
def get_random_questions_by_theme(theme_id: str = "", count: int = 20) -> list[exam_models.Question]:

    query_set = exam_models.Question.objects
                 
    if theme_id:
        query_set = query_set.select_related("thema").filter(thema_id=theme_id)

    query_set = query_set.order_by('?')[:count]
        
    return list(query_set)


def get_questions_by_ids(ids: list[str] = None) -> list[exam_models.Question]:

    if not isinstance(ids, list):
        raise ValueError("The 'ids' parameter must be a list of question IDs.")
    
    if ids is None: ids = []
        
    query_set = exam_models.Question.objects.filter(id__in=ids)
    return list(query_set)


def get_reviews(count: int = 20) -> list[app_models.Review]:

    if count <= 0:
        raise ValueError("The 'count' parameter must be a positive integer.")

    query_set = app_models.Review.objects.all()[:count]
    return list(query_set)


def get_themes(count: int = 10) -> list[exam_models.Thema]:

    if count <= 0:
        raise ValueError("The 'count' parameter must be a positive integer.")

    query_set = exam_models.Thema.objects.all()[:count]
    return list(query_set)


def get_products(count: int = 10) -> list[app_models.OrderItem]:

    if count <= 0:
        raise ValueError("The 'count' parameter must be a positive integer.")

    query_set = app_models.OrderItem.objects.all()[:count]
    return list(query_set)


def get_valid_subscribers() -> list[app_models.TelegramSubscriber]:
    
    return list(app_models.TelegramSubscriber.objects.filter(is_valid=True).all())


def get_next_asf_courses(date: datetime, count: int = 3) -> list[app_models.AsfCourse]:
    
    if not isinstance(date, datetime):
        raise ValueError("The 'date' parameter must be a datetime object.")
    if count <= 0:
        raise ValueError("The 'count' parameter must be a positive integer.")

    query_set = app_models.AsfCourse.objects.filter(lesson_1_date__gt=date).order_by('lesson_1_date')[:count]
    return list(query_set)