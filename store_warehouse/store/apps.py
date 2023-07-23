from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_warehouse.store'

    def ready(self):
        from . import signals  # noqa:F401
