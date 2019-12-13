from rest_framework import serializers

from meals.models import SpecificMeal, Meal
from meals.serializers import SmSerializer
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


class OrderSerializer(serializers.ModelSerializer):
    """
    Class for serializing Order objects
    """
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all()
    )
    # table_name = serializers.SerializerMethodField("get_table_name")
    meals_id = SmSerializer(
        many=True
    )

    class Meta:
        model = Order
        fields = (
            "id",
            "waiter_id",
            "table_id",
            "is_open",
            "date",
            "meals_id",
        )
        read_only_fields = ("id", "is_open")

    # def get_table_name(self, obj):
    #     """
    #     Getting table name from related Table model
    #     """
    #     # table = Table.objects.get(pk=obj["table_id"])
    #     print(obj)
    #     return "table.name"

    def create(self, validated_data):
        """
        Custom create method for Order serializer
        """
        meals_id = validated_data.pop("meals_id")
        order = Order.objects.create(**validated_data)

        for specific_meal in meals_id:
            meal = Meal.objects.get(pk=specific_meal["meal_id"])
            amount = specific_meal["amount"]
            SpecificMeal.objects.create(order_id=order, amount=amount, meal_id=meal)

        return order
