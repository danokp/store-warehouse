import requests

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StoreOrder
from .serializers import SwapIDStoreOrderSerializer
from store_warehouse.config import STORE_WAREHOUSE_SYNC_URL


@receiver(post_save, sender=StoreOrder)
def add_new_order(sender, instance, **kwargs):
    '''Add new order in Warehouse if it has been created in Store'''

    if instance.prev_status is None:
        instance.prev_status = instance.status
        requests.post(
            f'{STORE_WAREHOUSE_SYNC_URL}/warehouse/warehouseorder/',
            data=SwapIDStoreOrderSerializer(instance).data,
        )
