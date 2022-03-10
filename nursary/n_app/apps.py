from django.apps import AppConfig


class NAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'n_app'


class NAppConfig(AppConfig):
    name = 'n_app'

    def ready(self):
        import n_app.signals
