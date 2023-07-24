from .models import WarehouseOrder
from store_warehouse.warehouse.serializers import WarehouseOrderSerializer
from store_warehouse.orders.views import OrderAPIViewSet

from store_warehouse.orders.models import SynchConnection


class WarehouseOrderAPIViewSet(OrderAPIViewSet):
    basename = 'warehouseorder'
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer

    def perform_create(self, serializer):
        '''With use of received url identify store that created order'''
        serializer.validated_data['connection'] = SynchConnection.objects.get(
            url=serializer.validated_data.get('connection')
        )
        serializer.save()
