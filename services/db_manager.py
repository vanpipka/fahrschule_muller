from fahrschule_muller import models as app_models
from exam import models as exam_models


def check_and_save_message(message_data):

    message = app_models.Message()
    message.text = message_data.get('phone', '')
    message.author = message_data.get('name', '')
    message.form_name = message_data.get('form_name', '')
    message.save()
    
    
def get_questions_by_theme(theme_id = "", count = 20):

    query_set = exam_models.Question.objects
                 
    if theme_id:
        query_set = query_set.select_related("thema").filter(thema_id=theme_id)

    query_set = query_set.all()[:count]
        
    return list(query_set)


def get_reviews(count = 20):

    query_set = app_models.Review.objects.all()[:count]
    return list(query_set)


def get_themes(count = 10):

    query_set = exam_models.Thema.objects.all()[:count]
    return list(query_set)