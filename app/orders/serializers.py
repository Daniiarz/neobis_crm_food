from rest_framework import serializers
from .models import Table, Order


class TableSerializer(serializers.ModelSerializer):
    """
    Class for serializing Table objects
    """

    class Meta:
        model = Table
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class OrderSerializer(serializers.ModelSerializer):
    """
    Class for serializing Order objects
    """
    table_name = serializers.SerializerMethodField()
    meals_id = serializers.

    class Meta:
        model = Order
        fields = (
            "id",
            "waiter_id",
            "table_id",
            "table_name",
            "is_open",
            "date",

        )