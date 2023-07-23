from django.apps import AppConfig


class WarehouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_warehouse.warehouse'

    def ready(self):
        from . import signals
