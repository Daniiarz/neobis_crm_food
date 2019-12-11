from django.test import TestCase
from django.db.utils import IntegrityError
from rest_framework.test import APIClient

from orders import models
from .utils import TableFactory, create_user_model, OrderFactory
from meals.tests.utils import SMFactory


class TestModels(TestCase):
	"""
	Class for testing meals and related models
	"""

	def setUp(self) -> None:
		self.client = APIClient()

	def test_tables(self):
		"""
		Testing creation of Table model
		"""
		name = "Any Table"
		table = TableFactory(name=name)

		self.assertEqual(str(table), name)

	def test_orders(self):
		"""
		Testing creation of Order model
		"""

		table = TableFactory()
		user = create_user_model()

		order = models.Order.objects.create(waiter_id=user, table_id=table)

		self.assertEqual(str(order), f"Order #{order.id}, {order.date}")

	def test_orders_with_specific_meals(self):
		"""
		Testing creation of order model with specific meals
		"""

		user = create_user_model()
		order = OrderFactory(waiter_id=user)

		special_meal1 = SMFactory(order_id=order)
		special_meal2 = SMFactory(order_id=order)

		related_meals = order.specific_meals.all()
		self.assertIn(special_meal1, related_meals)
		self.assertIn(special_meal2, related_meals)

	def test_order_without_user(self):
		"""
		Testing creation of order without User model
		"""
		user = None
		with self.assertRaises(IntegrityError):
			OrderFactory(waiter_id=user)

	def test_order_without_table(self):
		"""
		Testing creation of order without Table model
		"""

		table = None
		with self.assertRaises(IntegrityError):
			OrderFactory(table_id=table)
