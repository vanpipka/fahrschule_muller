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
    return render(
        request, 
        'app/pages/index.html', 
        context={
            'reviews': db_manager.get_reviews(20),
            'title': 'Fahrschule S.V.S. Müller – Führerschein für PKW, LKW und Motorrad in Deutschland',
            'description': 'Fahrschule S.V.S. Müller – professionelle Ausbildung für PKW, LKW, Motorrad und Führerschein mit 17. Jetzt informieren und anmelden!',
            'keywords': 'Herford, Fahrschule, Führerschein, PKW, LKW, Motorrad, Fahrschule Müller, Aufbauseminare, Führerschein mit 17, Deutschland',
            }  
        )


def team(request):
    return render(
        request, 
        'app/pages/team.html', 
        context={
            'title': 'Unser Team – Fahrschule S.V.S. Müller in Herford',
            'description': 'Lernen Sie das erfahrene Team der Fahrschule S.V.S. Müller in Herford kennen. Persönliche Betreuung und individuelle Ausbildung für Ihren Führerschein.',
            'keywords': 'Herford, Fahrschule Herford, Fahrlehrer, Führerscheinausbildung, Team, S.V.S. Müller, PKW, LKW, Motorrad',
            }     
        )


def motorrad(request):
    return render(
        request, 
        'app/pages/motorrad.html',
        context={
            'title': 'Führerschein Klasse A – Motorrad-Ausbildung bei Fahrschule S.V.S. Müller in Herford',
            'description': 'Erleben Sie Freiheit auf zwei Rädern mit unserer professionellen Motorrad-Ausbildung für die Klassen A, A1, A2 und AM in Herford.',
            'keywords': 'Motorradführerschein Herford, Klasse A, A1, A2, AM, Fahrschule S.V.S. Müller, Motorrad-Ausbildung',
            }   
    )


def motorrad_details(request):
    return render(
        request, 
        'app/pages/motorrad_details.html',
        context={
            'title': 'Führerschein Klasse A – Motorrad-Ausbildung bei Fahrschule S.V.S. Müller in Herford',
            'description': 'Erleben Sie Freiheit auf zwei Rädern mit unserer professionellen Motorrad-Ausbildung für die Klassen A, A1, A2 und AM in Herford.',
            'keywords': 'Motorradführerschein Herford, Klasse A, A1, A2, AM, Fahrschule S.V.S. Müller, Motorrad-Ausbildung',
            }     
    )


def lkw(request):
    return render(
        request, 
        'app/pages/lkw.html',
        context={
            'title': 'LKW-Führerschein – Berufskraftfahrer-Ausbildung bei S.V.S. Müller in Herford',
            'description': 'Werden Sie Profi im Güterverkehr mit unserer umfassenden LKW-Ausbildung für die Klassen C1, C1E, C und CE in Herford.',
            'keywords': 'LKW-Führerschein Herford, Klasse C, C1, CE, Berufskraftfahrer, Fahrschule S.V.S. Müller',
            }   
    )


def lkw_details(request):
    return render(
        request, 
        'app/pages/lkw_details.html',
        context={
            'title': 'LKW-Führerschein – Berufskraftfahrer-Ausbildung bei S.V.S. Müller in Herford',
            'description': 'Werden Sie Profi im Güterverkehr mit unserer umfassenden LKW-Ausbildung für die Klassen C1, C1E, C und CE in Herford.',
            'keywords': 'LKW-Führerschein Herford, Klasse C, C1, CE, Berufskraftfahrer, Fahrschule S.V.S. Müller',
            }    
    )


def pkw(request):
    return render(
        request, 
        'app/pages/pkw.html',
        context={
            'title': 'PKW-Führerschein Klasse B – Ihre Fahrschule S.V.S. Müller in Herford',
            'description': 'Starten Sie Ihre Mobilität mit unserem PKW-Führerschein der Klasse B. Individuelle Betreuung und moderne Ausbildungsmethoden erwarten Sie.',
            'keywords': 'PKW-Führerschein Herford, Klasse B, Fahrschule S.V.S. Müller, Autoführerschein, Fahrunterricht',
            }   
    )


def pkw_details(request):
    return render(
        request, 
        'app/pages/pkw_details.html',
        context={
            'title': 'PKW-Führerschein Klasse B – Ihre Fahrschule S.V.S. Müller in Herford',
            'description': 'Starten Sie Ihre Mobilität mit unserem PKW-Führerschein der Klasse B. Individuelle Betreuung und moderne Ausbildungsmethoden erwarten Sie.',
            'keywords': 'PKW-Führerschein Herford, Klasse B, Fahrschule S.V.S. Müller, Autoführerschein, Fahrunterricht',
            }   
    )


def b_17(request):
    return render(
        request, 
        'app/pages/b_17.html',
        context={
            'title': 'Begleitetes Fahren ab 17 – Führerschein B17 bei S.V.S. Müller in Herford',
            'description': 'Starten Sie frühzeitig mit dem Führerschein B17 und sammeln Sie sichere Fahrerfahrung unter Begleitung. Jetzt bei uns anmelden!',
            'keywords': 'Führerschein mit 17, B17 Herford, begleitetes Fahren, Fahrschule S.V.S. Müller, Klasse B',
            }   
    )


def aufbauseminare(request):
    return render(
        request, 
        'app/pages/aufbauseminare.html',
        context={
            'title': 'Aufbauseminare für Fahranfänger und Punkteauffällige – S.V.S. Müller Herford',
            'description': 'Unsere Aufbauseminare (ASF & FES) helfen Ihnen, Fahrverhalten zu verbessern und Punkte abzubauen. Professionelle Nachschulungen in Herford.',
            'keywords': 'Aufbauseminar Herford, ASF, FES, Punkteabbau, Fahrschule S.V.S. Müller, Nachschulung',
            }   
    )


def aufbauseminare_anmeldung(request):
    return render(
        request, 
        'app/pages/asf.html',
        context={
            'title': 'Aufbauseminare für Fahranfänger und Punkteauffällige – S.V.S. Müller Herford',
            'description': 'Unsere Aufbauseminare (ASF & FES) helfen Ihnen, Fahrverhalten zu verbessern und Punkte abzubauen. Professionelle Nachschulungen in Herford.',
            'keywords': 'Aufbauseminar Herford, ASF, FES, Punkteabbau, Fahrschule S.V.S. Müller, Nachschulung',
            }   
    )


def aufbauseminare_anmeldung_asf(request):

    if request.method == "POST":
        
        try:
            request_body = request.POST.dict()
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        
        db_manager.check_and_save_anmeldung(request_body)

        return render(request, 'app/pages/success.html')

    return HttpResponse(status=404)


def datenschutz(request):
    return render(
        request, 
        'app/pages/datenschutz.html',
        context={
            'title': 'Datenschutzerklärung – Fahrschule S.V.S. Müller Herford',
            'description': 'Erfahren Sie, wie wir Ihre personenbezogenen Daten schützen und verarbeiten. Unsere Datenschutzerklärung gibt Ihnen einen Überblick über Ihre Rechte und unsere Datenschutzmaßnahmen.',
            'keywords': 'Datenschutz, Datenschutzerklärung, Fahrschule Herford, S.V.S. Müller, personenbezogene Daten, DSGVO',
            }   
    )


def ausbildung(request):
    return render(
        request, 
        'app/pages/ausbildung.html',
        context={
            'title': 'Fahrlehrerausbildung bei S.V.S. Müller – Ihre Karriere in Herford starten',
            'description': 'Beginnen Sie Ihre Karriere als Fahrlehrer mit unserer umfassenden Ausbildung in Herford. Werden Sie Teil unseres professionellen Teams und gestalten Sie die Mobilität von morgen mit.',
            'keywords': 'Fahrlehrerausbildung Herford, Karriere Fahrschule, S.V.S. Müller, Fahrlehrer werden, Ausbildung Fahrlehrer',
            }   
    )


def stelle(request):
    return render(
        request, 
        'app/pages/stelle.html',
        context={
            'title': 'Stellenangebote für Fahrlehrer – Arbeiten bei S.V.S. Müller in Herford',
            'description': 'Suchen Sie eine neue Herausforderung als Fahrlehrer? Bei S.V.S. Müller in Herford erwartet Sie ein motiviertes Team, flexible Arbeitszeiten und attraktive Entwicklungsmöglichkeiten.',
            'keywords': 'Fahrlehrer Stellenangebote Herford, Jobs Fahrschule, S.V.S. Müller, Fahrlehrer gesucht, Karriere Fahrschule',
            }   
    )


def products(request):
    return render(
        request, 
        'app/pages/products.html', 
        context={
            'products': db_manager.get_products(50),
            'title': 'Lehrmaterialien für Ihre Fahrausbildung – S.V.S. Müller Herford',
            'description': 'Entdecken Sie unsere hochwertigen Lehrmittel für Theorie und Praxis. Optimal vorbereitet mit Materialien der Fahrschule S.V.S. Müller.',
            'keywords': 'Fahrschule Lehrmittel, Theorieunterricht, Praxisvorbereitung, Fahrschule S.V.S. Müller, Lernmaterialien'
            }
    )


def products_detail(request):
    return render(
        request, 
        'app/pages/products.html', 
        context={
            'products': db_manager.get_products(50),
            'title': 'Lehrmaterialien für Ihre Fahrausbildung – S.V.S. Müller Herford',
            'description': 'Entdecken Sie unsere hochwertigen Lehrmittel für Theorie und Praxis. Optimal vorbereitet mit Materialien der Fahrschule S.V.S. Müller.',
            'keywords': 'Fahrschule Lehrmittel, Theorieunterricht, Praxisvorbereitung, Fahrschule S.V.S. Müller, Lernmaterialien'
            }
    )


def anfrage(request):
    if request.method == "POST":
        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        
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