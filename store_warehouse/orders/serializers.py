from rest_framework import serializers


class SwapIDOrderSerializer(serializers.ModelSerializer):
    id_in_connected_db = serializers.IntegerField(source='id')

    class Meta:
        fields = (
            'order_number',
            'status',
            'id_in_connected_db',
            'prev_status',
        )
