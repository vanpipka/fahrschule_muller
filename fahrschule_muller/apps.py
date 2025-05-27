from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fahrschule_muller'

    def ready(self):
        import fahrschule_muller.signals
        