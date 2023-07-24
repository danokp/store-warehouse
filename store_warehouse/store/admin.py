from django.contrib import admin
from .models import StoreOrder


@admin.register(StoreOrder)
class StoreAdmin(admin.ModelAdmin):
    fields = ('order_number', 'status', 'connection')
    readonly_fields = ('order_number', 'status', 'connection')

    def get_readonly_fields(self, request, obj=None):
        # For new objects (during creation), allow all fields to be editable
        if not obj:
            return ()

        # For existing objects (during editing),
        # return the read-only fields list
        return self.readonly_fields
