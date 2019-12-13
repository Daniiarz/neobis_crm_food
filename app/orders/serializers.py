from rest_framework import serializers

from meals.models import SpecificMeal
from meals.serializers import SmSerializer
from .models import Check, Order, Table


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


class OrderSerializer(serializers.ModelSerializer):
    """
    Class for serializing Order objects
    """
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all()
    )
    table_name = serializers.SerializerMethodField("get_table_name")
    is_open = serializers.SerializerMethodField("get_is_open")
    meals_id = SmSerializer(
        many=True
    )

    class Meta:
        model = Order
        fields = (
            "id",
            "waiter_id",
            "table_id",
            "table_name",
            "is_open",
            "date",
            "meals_id",
        )
        read_only_fields = ("id", "is_open", "waiter_id")

    def get_is_open(self, obj):
        is_open = obj

        if is_open:
            return 1
        else:
            return 0

    def get_table_name(self, obj):
        table = obj.table_id

        return str(table)

    def create(self, validated_data):
        """
        Custom create method for Order serializer
        """
        meals_id = validated_data.pop("meals_id")
        order = Order.objects.create(**validated_data)

        for specific_meal in meals_id:
            SpecificMeal.objects.create(order_id=order, **specific_meal)

        return order


class CheckSerializer(serializers.ModelSerializer):
    """
    Class for serializing check objects
    """
    meals = SmSerializer(
        many=True,
        source="order_id.meals_id.all",
        read_only=True
    )
    order_id = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all()
    )

    class Meta:
        model = Check
        fields = (
            "id",
            "order_id",
            "date",
            "service_fee",
            "total_sum",
            "meals"
        )
        read_only_fields = ("id", "date", "service_fee", "total_sum")

    def create(self, validated_data):
        check = Check.objects.create_check(**validated_data)

        return check
