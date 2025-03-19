from fahrschule_muller import models as app_models
from exam import models as exam_models


def check_and_save_message(message_data):

    message = app_models.Message()
    message.text = message_data.get('phone', '')
    message.author = message_data.get('name', '')
    message.form_name = message_data.get('form_name', '')
    message.save()
    
    
def get_questions(type_id = ""):

    query_set = exam_models.Question.objects
                 
    if type_id:
        query_set = query_set.select_related("type").filter(type_id=type_id) 
        
    return list(query_set)