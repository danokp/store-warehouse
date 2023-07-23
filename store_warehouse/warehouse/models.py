from django.db import models

from store_warehouse.orders.models import Order


class WarehouseOrder(Order):

    id_in_connected_db = models.IntegerField(
        null=True,
        default=None,
    )
