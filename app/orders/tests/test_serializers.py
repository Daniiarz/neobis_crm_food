from django.test import TestCase
from orders import serializers
from orders.models import Order

from .utils import create_user_model, TableFactory
from meals.tests.utils import MealFactory


class TestSerializers(TestCase):
    """
    Testing serializers for Order model and Related models
    """

    def test_table_serializer(self):
        """
        Testing table serializer
        """

        payload = {
            "name": "Table #1"
        }

        serializer = serializers.TableSerializer(data=payload)
        valid = serializer.is_valid()
        self.assertTrue(valid)

    def test_order_serializer(self):
        """
        Testing order serializer and custom create
        """
        user = create_user_model()
        table = TableFactory()
        meal = MealFactory()
        meal2 = MealFactory()

        payload = {
            "waiter_id": user.id,
            "table_id": table.id,
            "meals_id": [
                {
                    "meal_id": meal.id,
                    "amount": 3,
                },
                {
                    "meal_id": meal2.id,
                    "amount": 5,
                }
            ]
        }

        serializer = serializers.OrderSerializer(data=payload)
        valid = serializer.is_valid()
        serializer.save()

        exists = Order.objects.all()[0]

        self.assertTrue(valid)
        print(serializer.data)
