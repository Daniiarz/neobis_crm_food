from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from meals.tests.utils import MealFactory
from orders import models, serializers
from .utils import TableFactory, OrderFactory, create_user_model

TABLES_URL = reverse("tables")
ORDERS_URL = reverse("orders")


class TestTableViews(TestCase):
    """
    Testing table views
    """

    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_tables(self):
        """
        Testing GET method for table view
        """

        table1 = TableFactory()
        table2 = TableFactory()
        tables = models.Table.objects.all()

        response = self.client.get(TABLES_URL)
        serializer = serializers.TableSerializer(tables, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_table(self):
        """
        Testing POST method for table view
        """
        payload = {
            "name": "Table#1"
        }

        response = self.client.post(TABLES_URL, data=payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_table(self):
        """
        Testing DELETE method for table view
        """
        table = TableFactory()

        payload = {
            "id": table.id
        }

        response = self.client.delete(TABLES_URL, data=payload)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestOrderViews(TestCase):
    """
    Testing order views
    """

    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_orders(self):
        """
        Testing GET method of order view
        """
        user = create_user_model()

        order1 = OrderFactory(waiter_id=user)
        order2 = OrderFactory(waiter_id=user)

        orders = models.Order.objects.all()
        serializer = serializers.OrderSerializer(orders, many=True)

        response = self.client.get(ORDERS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_post_order(self):
        """
        Testing POST method of order view
        """
        user = create_user_model()
        table = TableFactory()
        meal = MealFactory()
        meal2 = MealFactory()

        self.client.force_authenticate(user)

        payload = {
            "table_id": table.id,

            "meals_id": [
                {
                    "meal_id": meal.id,
                    "amount": 4
                },
                {
                    "meal_id": meal2.id,
                    "amount": 6
                }
            ]
        }

        response = self.client.post(ORDERS_URL, data=payload)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
