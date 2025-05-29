from fahrschule_muller import models as app_models
from exam import models as exam_models


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
    
    if ids is None: ids = []
        
    query_set = exam_models.Question.objects.filter(id__in=ids)
    return list(query_set)


def get_reviews(count: int = 20) -> list[app_models.Review]:

    query_set = app_models.Review.objects.all()[:count]
    return list(query_set)


def get_themes(count: int = 10) -> list[exam_models.Thema]:

    query_set = exam_models.Thema.objects.all()[:count]
    return list(query_set)


def get_products(count: int = 10) -> list[app_models.OrderItem]:

    query_set = app_models.OrderItem.objects.all()[:count]
    return list(query_set)


def get_valid_subscribers() -> list[app_models.TelegramSubscriber]:
    
    return list(app_models.TelegramSubscriber.objects.filter(is_valid=True).all())