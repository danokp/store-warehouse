from rest_framework import serializers

from .models import StoreOrder
from store_warehouse.orders.serializers import SwapIDOrderSerializer


class StoreOrderSerializer(serializers.ModelSerializer):
    '''Serializer used for StoreOrder CRUD depicting'''

    class Meta:
        model = StoreOrder
        fields = ('id', 'order_number', 'status', 'prev_status')


class SwapIDStoreOrderSerializer(SwapIDOrderSerializer):
    '''Serialized used for synchronization with Warehouse. It swaps id and
    id_in_connected_db in order to get write request.'''

    class Meta:
        model = StoreOrder
        fields = ('order_number', 'status', 'id_in_connected_db', 'prev_status')
