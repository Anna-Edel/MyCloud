from django.apps import AppConfig # type: ignore

class CloudConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cloud'