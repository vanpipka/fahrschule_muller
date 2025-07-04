from django.core.cache import cache
from services import db_manager

def get_site_settings():

    key = 'site_settings_cache'
    settings = cache.get(key)

    if not settings:
        settings = db_manager.get_site_settings()
        if settings:
            # Кэшируем на 24 часа
            cache.set(key, settings, 60 * 60 * 24)

    return settings


def get_site_texts():
    
    key = 'site_texts_cache'
    texts = cache.get(key)

    if not texts:
        texts = db_manager.get_site_texts()
        if texts:
            # Кэшируем на 24 часа
            cache.set(key, texts, 60 * 60 * 24)

    return texts


def get_exam_themes():

    key = 'exams_theme_cache'
    settings = cache.get(key)

    if not settings:
        settings = db_manager.get_themes_for_header() 
        if settings:
            # Кэшируем на 24 часа
            cache.set(key, settings, 60 * 60 * 24)

    return settings