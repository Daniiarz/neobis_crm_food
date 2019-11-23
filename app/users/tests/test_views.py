from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .utils import RoleFactory
from users.models import Role, User
from users import serializers

ROLES_URL = reverse("roles")


class TestRoleView(TestCase):
    """
        Testing Role model endpoints
    """

    def setUp(self) -> None:
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
