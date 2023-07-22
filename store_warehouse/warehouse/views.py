from .models import WarehouseOrder
from store_warehouse.warehouse.serializers import WarehouseOrderSerializer
from store_warehouse.orders.views import OrderAPIViewSet



class WarehouseOrderAPIViewSet(OrderAPIViewSet):
    basename = 'warehouseorder'
    queryset = WarehouseOrder.objects.all()
    serializer_class = WarehouseOrderSerializer


# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import WarehouseOrder
# from .serializers import WarehouseOrderSerializer
#
# class WarehouseOrderCreate(APIView):
#     def post(self, request):
#         serializer = WarehouseOrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework import generics, mixins
#
# from .models import WarehouseOrder
# from store_warehouse.warehouse.serializers import WarehouseOrderSerializer
#
#
# class WarehouseOrderAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = WarehouseOrder.objects.all()
#     serializer_class = WarehouseOrderSerializer
#
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)