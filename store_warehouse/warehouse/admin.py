from django.contrib import admin
from .models import WarehouseOrder


@admin.register(WarehouseOrder)
class PersonAdmin(admin.ModelAdmin):
    fields = ('order_number', 'status')
    readonly_fields = ('order_number',)

    def has_add_permission(self, request, obj=None):
        '''Make it impossible to add new Order in Django Admin
        in Warehouse mode.'''
        return False
