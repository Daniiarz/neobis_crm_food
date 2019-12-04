from django.test import TestCase
# from django.db.utils import IntegrityError

from .utils import TableFactory


class TestModels(TestCase):
	"""
	Class for testing meals and related models
	"""

	def test_tables(self):
		"""
		Testing creation of Table model
		"""
		name = "Any Table"
		table = TableFactory(name=name)

		self.assertEqual(str(table), name)
