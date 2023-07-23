import requests

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import WarehouseOrder
from .serializers import SwapIDWarehouseOrderSerializer
from store_warehouse.config import STORE_WAREHOUSE_SYNC_URL


@receiver(pre_save, sender=WarehouseOrder)
def update_order_status_in_store(sender, instance, **kwargs):
    '''Synchronize order status in Store and Warehouse'''

    if instance.status != instance.prev_status:
        instance.prev_status = instance.status
        requests.put(
            f'{STORE_WAREHOUSE_SYNC_URL}/store/storeorder/{instance.id_in_connected_db}/',
            data=SwapIDWarehouseOrderSerializer(instance).data,
        )
