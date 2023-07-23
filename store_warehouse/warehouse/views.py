from .models import WarehouseOrder
from store_warehouse.warehouse.serializers import WarehouseOrderSerializer
from store_warehouse.orders.views import OrderAPIViewSet


class WarehouseOrderAPIViewSet(OrderAPIViewSet):
    basename = 'warehouseorder'
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer
