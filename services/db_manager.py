from fahrschule_muller import models as app_models
from exam import models as exam_models


def check_and_save_message(message_data):

    message = app_models.Message(
        text = message_data.get('text', ''),
        author = message_data.get('name', ''),
        form_name = message_data.get('form_name', ''),
        phone_number = message_data.get('phone', ''),
        url = message_data.get('url', '')
    )
    message.save()

    
def get_random_questions_by_theme(theme_id = "", count = 20):

    query_set = exam_models.Question.objects
                 
    if theme_id:
        query_set = query_set.select_related("thema").filter(thema_id=theme_id)

    query_set = query_set.order_by('?')[:count]
        
    return list(query_set)


def get_questions_by_ids(ids = None):
    
    if ids is None: ids = []
        
    query_set = exam_models.Question.objects.filter(id__in=ids)
    return list(query_set)


def get_reviews(count = 20):

    query_set = app_models.Review.objects.all()[:count]
    return list(query_set)


def get_themes(count = 10):

    query_set = exam_models.Thema.objects.all()[:count]
    return list(query_set)