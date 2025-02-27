from django.shortcuts import render

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


def datenschutz(request):
    return render(request, 'app/pages/datenschutz.html')
