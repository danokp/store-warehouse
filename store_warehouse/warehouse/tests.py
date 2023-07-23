from django.test import TestCase

from .models import WarehouseOrder
from .serializers import (
    WarehouseOrderSerializer,
    SwapIDWarehouseOrderSerializer,
)


class WarehouseOrderSerializerTestCase(TestCase):
    def setUp(self):
        '''Create a WarehouseOrder instance for testing'''

        self.warehouse_order = WarehouseOrder.objects.create(
            order_number='ORDER1',
            status='new',
            id_in_connected_db=1,
            prev_status='stored',
        )

    def test_warehouse_order_serializer(self):

        serializer = WarehouseOrderSerializer(instance=self.warehouse_order)
        expected_data = {
            'order_number': 'ORDER1',
            'status': 'new',
            'id_in_connected_db': self.warehouse_order.id,
            'prev_status': 'stored',
        }
        self.assertEqual(serializer.data, expected_data)

    def test_swap_id_warehouse_order_serializer(self):

        serializer = SwapIDWarehouseOrderSerializer(
            instance=self.warehouse_order,
        )
        expected_data = {
            'order_number': 'ORDER1',
            'status': 'new',
            'id_in_connected_db': self.warehouse_order.id,
            'prev_status': 'stored',
        }
        self.assertEqual(serializer.data, expected_data)
