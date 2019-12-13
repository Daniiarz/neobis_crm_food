from django.test import TestCase

from meals.tests.utils import MealFactory, SMFactory
from orders import serializers
from .utils import OrderFactory, TableFactory, create_user_model


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
        serializer.save(waiter_id=user)

        self.assertTrue(valid)

    def test_check_serializer(self):
        """
        Testing Check serializer
        """
        user = create_user_model()
        order = OrderFactory(waiter_id=user)

        SMFactory(order_id=order)
        SMFactory(order_id=order)

        payload = {
            "order_id": order.id
        }

        serializer = serializers.CheckSerializer(data=payload)
        valid = serializer.is_valid()
        serializer.save()

        self.assertTrue(valid)
