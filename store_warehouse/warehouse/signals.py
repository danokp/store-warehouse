import requests

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import WarehouseOrder
from .serializers import SwapIDWarehouseOrderSerializer
from store_warehouse.config import STORE_WAREHOUSE_SYNC_URL
from store_warehouse.client.requests import synchronize_databases


@receiver(pre_save, sender=WarehouseOrder)
def update_order_status_in_store(sender, instance, **kwargs):
    '''Synchronize order status in Store and Warehouse'''

    if instance.status != instance.prev_status:
        connected_store = sender.objects.get(id=instance.id).connection
        token = connected_store.token
        url = f'{connected_store.url}/store/storeorder/{instance.id_in_connected_db}/'  # noqa: E501

        instance.prev_status = instance.status
        data = SwapIDWarehouseOrderSerializer(instance).data

        synchronize_databases('put', url, token, data)
        # requests.put(
        #     f'{STORE_WAREHOUSE_SYNC_URL}/store/storeorder/{instance.id_in_connected_db}/',  # noqa: E501
        #     data=SwapIDWarehouseOrderSerializer(instance).data,
        # )
