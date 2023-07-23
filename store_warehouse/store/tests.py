from django.test import TestCase

from .models import StoreOrder
from .serializers import StoreOrderSerializer, SwapIDStoreOrderSerializer


class TestStoreOrderSerializers(TestCase):

    def setUp(self):
        '''Create a StoreOrder instance for testing'''

        self.store_order = StoreOrder.objects.create(
            order_number='ORDER1',
            status='new',
            prev_status='stored',
        )

    def test_store_order_serializer(self):
        serializer = StoreOrderSerializer(instance=self.store_order)
        expected_data = {
            'id': self.store_order.id,
            'order_number': 'ORDER1',
            'status': 'new',
            'prev_status': 'stored',
        }
        self.assertEqual(serializer.data, expected_data)

    def test_swap_id_store_order_serializer(self):
        serializer = SwapIDStoreOrderSerializer(instance=self.store_order)
        expected_data = {
            'order_number': 'ORDER1',
            'status': 'new',
            'id_in_connected_db': self.store_order.id,
            'prev_status': 'stored',
        }
        self.assertEqual(serializer.data, expected_data)

    def test_store_order_deserialization(self):
        data = {
            'order_number': 'ORDER2',
            'status': 'in progress',
            'id_in_connected_db': 1001,
            'prev_status': 'new',
        }
        serializer = SwapIDStoreOrderSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertEqual(instance.order_number, 'ORDER2')
        self.assertEqual(instance.status, 'in progress')
        self.assertEqual(instance.prev_status, 'new')


class StoreOrderModelTestCase(TestCase):
    def setUp(self):
        '''Create a StoreOrder instance for testing'''
        self.store_order = StoreOrder.objects.create(
            order_number='ORDER1',
            status='new',
            prev_status='stored',
        )

    def test_store_order_str_representation(self):
        '''Test the __str__ method of the StoreOrder model'''

        self.assertEqual(str(self.store_order), 'order: ORDER1-new')

    def test_store_order_status_choices(self):
        '''Test that the status field only accepts valid choices'''
        valid_choices = ['new', 'in progress', 'stored', 'send']
        invalid_choice = 'invalid_status'

        self.assertTrue(all(choice[0] in valid_choices for choice in
                            StoreOrder.STATUS_CHOICES))
        self.assertFalse(invalid_choice in valid_choices)

    def test_store_order_unique_order_number(self):
        '''Test that the order_number field is unique
        Try to create a StoreOrder with an existing order number'''
        with self.assertRaises(Exception):
            StoreOrder.objects.create(
                order_number='ORDER1',
                status='new',
                prev_status='stored',
            )
