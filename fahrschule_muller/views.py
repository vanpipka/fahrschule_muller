from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json
from services import db_manager


def custom_404(request, exception):
    return render(request, "app/404.html", status=404)


def custom_500(request):
    return render(request, "app/500.html", status=500)


def custom_403(request, exception):
    return render(request, "app/403.html", status=403)


def custom_400(request, exception):
    return render(request, "app/400.html", status=400)


def home(request):    
    reviews = db_manager.get_reviews(20)
    return render(request, 'app/pages/index.html', context={'reviews': reviews})


def team(request):
    return render(request, 'app/pages/team.html')


def motorrad(request):
    return render(request, 'app/pages/motorrad.html')


def motorrad_details(request):
    return render(request, 'app/pages/motorrad_details.html')


def lkw(request):
    return render(request, 'app/pages/lkw.html')


def lkw_details(request):
    return render(request, 'app/pages/lkw_details.html')


def pkw(request):
    return render(request, 'app/pages/pkw.html')


def pkw_details(request):
    return render(request, 'app/pages/pkw_details.html')


def b_17(request):
    return render(request, 'app/pages/b_17.html')


def aufbauseminare(request):
    return render(request, 'app/pages/aufbauseminare.html')


def datenschutz(request):
    return render(request, 'app/pages/datenschutz.html')


def ausbildung(request):
    return render(request, 'app/pages/ausbildung.html')


def stelle(request):
    return render(request, 'app/pages/stelle.html')


def products(request):
    products = db_manager.get_products(20)
    return render(request, 'app/pages/products.html', context={'products': products})


def products_detail(request):
    products = db_manager.get_products(20)
    return render(request, 'app/pages/products.html', context={'products': products})


def anfrage(request):
    if request.method == "POST":

        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        
        print("Received request body:", request_body)
        
        db_manager.check_and_save_message({
            'name': request_body.get("name", ""),
            'phone': request_body.get("phone", ""),
            'url': request_body.get("url", ""), 
            'form_name': request_body.get("form", ""), 
            'message': request_body.get("message", ""), 
            'connection_type': request_body.get("connection_type", ""),     
        })

        return JsonResponse({"redirect_url": "/anfrage/"})

    return render(request, 'app/pages/success.html')