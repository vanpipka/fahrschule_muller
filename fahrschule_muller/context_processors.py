from services import utils
import services.const as const

def exam_items(request):
    
    items = [x for x in utils.get_exam_themes() if str(x.id) != const.GRUND_STOFF_ID]
    return {'exam_items': items}


def company_contacts(request):

    settings = utils.get_site_settings()
    return {
        'company_phone': settings.phone if settings else '',
        'company_email': settings.email if settings else '',
        'company_address': settings.address if settings else '',
        'company_mobile_phone': settings.mobile_phone if settings else '',
    }