from .models import StoreOrder
from .serializers import StoreOrderSerializer
from store_warehouse.orders.views import OrderAPIViewSet


class StoreOrderAPIViewSet(OrderAPIViewSet):
    basename = 'storeorder'
    queryset = StoreOrder.objects.all()
    serializer_class = StoreOrderSerializer
