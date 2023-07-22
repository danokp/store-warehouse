import requests

from store_warehouse.orders.models import Order
from store_warehouse.config import STORE_WAREHOUSE_SYNC_URL


class StoreOrder(Order):

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from .serializers import StoreOrderSerializer

        # if self.objects.filter(order_number=self.order_number):
        #     requests.post(
        #         f'{STORE_WAREHOUSE_SYNC_URL}create/',
        #         data=StoreOrderSerializer(self).data,
        #     )
        # else:
        requests.post(
            f'{STORE_WAREHOUSE_SYNC_URL}/warehouse/warehouseorder/create/',
            data=StoreOrderSerializer(self).data,
        )
