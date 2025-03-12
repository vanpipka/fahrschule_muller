"""
URL configuration for fahrschule_muller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, team, motorrad, motorrad_details, lkw, lkw_details, datenschutz, pkw, pkw_details, b_17, aufbauseminare

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/', team, name='team'),
    path('b_17/', b_17, name='b_17'),
    path('aufbauseminare/', aufbauseminare, name='aufbauseminare'),
    path('motorrad/details', motorrad_details, name='motorrad_details'),
    path('motorrad/', motorrad, name='motorrad'),
    path('lkw/details', lkw_details, name='lkw_details'),
    path('lkw/', lkw, name='lkw'),
    path('pkw/', pkw, name='pkw'),
    path('pkw/details', pkw_details, name='pkw_details'),
    path('datenschutz/', datenschutz, name='datenschutz'),
    path('users/', include('users.urls')),
    path('', home, name='home'),
]
