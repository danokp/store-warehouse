from .models import StoreOrder
from .serializers import StoreOrderSerializer
from store_warehouse.orders.views import OrderAPIViewSet


class StoreOrderAPIViewSet(OrderAPIViewSet):
    basename = 'storeorder'
    queryset = StoreOrder.objects.all()
    serializer_class = StoreOrderSerializer



# class StoreOrderAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = StoreOrder.objects.all()
#     serializer_class = StoreOrderSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)