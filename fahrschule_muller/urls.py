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
from fahrschule_muller import views
from django.conf import settings
from django.conf.urls.static import static

handler404 = views.custom_404
handler500 = views.custom_500
handler403 = views.custom_403
handler400 = views.custom_400

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/', views.team, name='team'),
    path('b_17/', views.b_17, name='b_17'),
    path('aufbauseminare/', views.aufbauseminare, name='aufbauseminare'),
    path('motorrad/details', views.motorrad_details, name='motorrad_details'),
    path('motorrad/', views.motorrad, name='motorrad'),
    path('lkw/details', views.lkw_details, name='lkw_details'),
    path('lkw/', views.lkw, name='lkw'),
    path('products/', views.products, name='products'),
    path('products/detail', views.products_detail, name='products_detail'),
    path('pkw/', views.pkw, name='pkw'),
    path('pkw/details', views.pkw_details, name='pkw_details'),
    path('karriere/ausbildung/', views.ausbildung, name='ausbildung'),
    path('karriere/stelle/', views.stelle, name='stelle'),
    path('datenschutz/', views.datenschutz, name='datenschutz'),
    path('users/', include('users.urls')),
    path('exam/', include('exam.urls')),
    path('anfrage/', views.anfrage, name='anfrage'),
    path('', views.home, name='home'),
]

# Подключаем медиа-файлы в режиме отладки (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)