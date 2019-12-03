from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .utils import RoleFactory, fake
from users.models import Role, User
from users import serializers

ROLES_URL = reverse("roles")

USERS_URL = reverse("users")


class TestRoleView(TestCase):
    """
    Testing Role model endpoints
    """

    def setUp(self) -> None:
        """
        Initial setUp for all tests
        """
        self.client = APIClient()

    def test_list_view(self):
        """
        Testing listing of role models
        """
        RoleFactory()
        RoleFactory()

        response = self.client.get(ROLES_URL)

        roles = Role.objects.all()
        serializer = serializers.RoleSerializer(roles, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_role(self):
        """
        Testing creation of role model
        """

        payload = {
            "name": "Waiter"
        }

        response = self.client.post(ROLES_URL, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exists = Role.objects.filter(name=response.data["name"]).exists()
        self.assertTrue(exists)

    def test_delete_role(self):
        """
        Testing deletion of role model
        """
        role = RoleFactory(name="Admin")

        payload = {
            'id': role.id
        }

        response = self.client.delete(ROLES_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestUserEndpoints(TestCase):
    """
    Testing user endpoints
    """

    def setUp(self) -> None:
        """
        Initial setUp for all tests
        """
        self.role = RoleFactory()
        self.user_data = {
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone": fake.phone_number(),
            "role_id": self.role,
        }
        self.client = APIClient()

    def test_get_all_users(self):
        """
        Testing on GET method on site/users/ endpoint, should return list of users
        """
        User.objects.create_user(**self.user_data)
        user_data = {
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "phone": fake.phone_number(),
            "role_id": self.role,
        }
        User.objects.create_user(**user_data)

        response = self.client.get(USERS_URL)
        users = User.objects.all()
        serializer = serializers.UserDetailSerializer(users, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_user_endpoint(self):
        """
        Testing user creation on site/users/ endpoint
        """
        self.user_data["role_id"] = self.role.id
        response = self.client.post(USERS_URL, self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exists = User.objects.filter(email=response.data["email"]).exists()
        self.assertTrue(exists)

    def test_user_delete_endpoint(self):
        """
        Testing custom delete method on site/users/ endpoint
        """
        user = User.objects.create_user(**self.user_data)

        payload = {
            'id': user.id
        }

        response = self.client.delete(USERS_URL, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_full_user_update(self):
        """
        Testing custom update method on site/users/ endpoint
        """
        user = User.objects.create_user(**self.user_data)
        payload = {
            "id": user.id,
            "name": "Aika",
            "surname": "Ivanova",
            "password": "Some cool pass",
            "email": "sample@example.com",
            "phone": "0777777777"
        }

        response = self.client.put(USERS_URL, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
