from django.shortcuts import render, redirect
from services import db_manager

def home(request):
    return render(request, 'app/pages/index.html')


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


def anfrage(request):
    if request.method == "POST":
               
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        form_name = request.POST.get("form_name")
        
        db_manager.check_and_save_message({'name': name, 'phone': phone, 'form_name': form_name})

        return redirect("success_page")

    return redirect("home")