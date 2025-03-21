from services import db_manager
import services.const as const

def exam_items(request):
    
    items = [x for x in db_manager.get_themes() if str(x.id) != const.GRUND_STOFF_ID]
    return {'exam_items': items}