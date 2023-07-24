import requests

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import StoreOrder
from .serializers import SwapIDStoreOrderSerializer
from store_warehouse.config import CLIENT_URL
from store_warehouse.client.requests import synchronize_databases


@receiver(post_save, sender=StoreOrder)
def add_new_order(sender, instance, **kwargs):
    '''Add new order in Warehouse if it has been created in Store'''

    if instance.prev_status is None:
        connected_store = sender.objects.get(id=instance.id).connection
        token = connected_store.token
        url = f'{connected_store.url}/warehouse/warehouseorder/'

        instance.prev_status = instance.status
        data = SwapIDStoreOrderSerializer(instance).data
        data['connection'] = CLIENT_URL

        synchronize_databases('post', url, token, data)
