from services import db_manager

def exam_items(request):
    return {'exam_items': db_manager.get_exams()}