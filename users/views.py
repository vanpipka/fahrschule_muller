from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms.registration_form import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('')  # Замените на вашу главную страницу
    else:
        form = RegisterForm()
    return render(request, './template/users/register.html', {'form': form})
