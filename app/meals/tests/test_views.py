from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from meals.models import Department, MealCategory, Meal
from meals import serializers
from .utils import DepartmentFactory, MealCategoryFactory, MealFactory

DEPARTMENT_URL = reverse("departments")
MEAL_CATEGORY_URL = reverse("meal-categories")


class TestDepartmentView(TestCase):
    """
        Testing endpoints for Departments model
    """

    def setUp(self) -> None:
        self.client = APIClient()

    def test_list_departments(self):
        """
        Testing GET method for department model, expecting list of departments
        """
        DepartmentFactory()
        DepartmentFactory()

        response = self.client.get(DEPARTMENT_URL)

        departments = Department.objects.all()
        serializer = serializers.DepartmentSerializer(departments, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)

    def test_create_department(self):
        """
        Testing POST method on departments/ endpoint with some data
        """
        payload = {
            "name": "Keke"
        }

        response = self.client.post(DEPARTMENT_URL, payload, format="json")
        exists = Department.objects.filter(name=payload["name"]).exists()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_custom_delete(self):
        """
        Testing custom handling of DELETE method on departments/  endpoint
        """
        department = DepartmentFactory()
        payload = {
            "id": department.id
        }

        response = self.client.delete(DEPARTMENT_URL, payload, format="json")
        exists = Department.objects.filter(id=payload["id"]).exists()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(exists)


class TestMealCategoryView(TestCase):
    """
    Class for testing endpoints of MealCategory model
    """

    def setUp(self) -> None:
        self.department = DepartmentFactory()
        self.client = APIClient()

    def test_list_categories(self):
        """
        Testing GET method for MealCategory model, expecting list of categories
        """
        MealCategoryFactory()
        MealCategoryFactory()

        response = self.client.get(MEAL_CATEGORY_URL)

        categories = MealCategory.objects.all()
        serializer = serializers.MealCategorySerializer(categories, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(categories, [])
        self.assertEqual(serializer.data, response.data)

    def test_create_category(self):
        """
        Testing creation of MealCategory object through API
        :return:
        """
        payload = {
            "name": "Kitchen",
            "department_id": self.department.id,
        }

        response = self.client.post(MEAL_CATEGORY_URL, payload, format="json")
        exists = MealCategory.objects.filter(name=payload["name"]).exists()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_custom_delete_method(self):
        """
        Testing custom handling of DELETE method on departments/  endpoint
        :return:
        """
        category = MealCategoryFactory()
        payload = {
            "id": category.id
        }

        response = self.client.delete(MEAL_CATEGORY_URL, payload, format="json")
        exists = MealCategory.objects.filter(id=payload["id"]).exists()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(exists)


class TestMealsViews(TestCase):
    """
    Class for testing endpoints of Meal model
    """
