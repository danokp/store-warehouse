from django.contrib import admin
from .models import StoreOrder


@admin.register(StoreOrder)
class PersonAdmin(admin.ModelAdmin):
    fields = ('order_number', 'status')
    readonly_fields = ('order_number', 'status')

    def get_readonly_fields(self, request, obj=None):
        # For new objects (during creation), allow all fields to be editable
        if not obj:
            return ()

        # For existing objects (during editing),
        # return the read-only fields list
        return self.readonly_fields
