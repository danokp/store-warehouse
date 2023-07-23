from rest_framework import serializers

from .models import WarehouseOrder
from store_warehouse.orders.serializers import SwapIDOrderSerializer


class WarehouseOrderSerializer(serializers.ModelSerializer):
    '''Serializer used for WarehouseOrder CRUD depicting'''

    class Meta:
        model = WarehouseOrder
        fields = (
            'id',
            'order_number',
            'status',
            'id_in_connected_db',
            'prev_status',
        )


class SwapIDWarehouseOrderSerializer(SwapIDOrderSerializer):
    '''Serialized used for synchronization with Store. It swaps id and
    id_in_connected_db in order to get write request.'''

    class Meta:
        model = WarehouseOrder
        fields = (
            'order_number',
            'status',
            'id_in_connected_db',
            'prev_status',
        )
