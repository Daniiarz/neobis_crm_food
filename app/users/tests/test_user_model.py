from django.test import TestCase
from . import utils

from django.db.utils import IntegrityError


class TestUserModel(TestCase):
    """
        Testing publicly available endpoints for user app
    """

    def test_roles_model(self):
        """
            Testing Role model creation
        """

        role_name = "Waiter"
        role = utils.RoleFactory(name=role_name)
        self.assertEqual(str(role), role_name)

    def test_create_user_without_role(self):
        """
            Testing that user can't be created without role model
        """

        role = None

        with self.assertRaises(IntegrityError):
            user = utils.UserFactory(role_id=role)

    def test_create_user_without_first_name(self):
        """
            Testing that user model can't be created without first name
        """

        first_name = ""

        with self.assertRaises(ValueError):
            user = utils.UserFactory(first_name=first_name)

    def test_create_user_without_last_name(self):
        """
            Testing that user model can't be created without last name
        """

        last_name = ""

        with self.assertRaises(ValueError):
            user = utils.UserFactory(last_name=last_name)

    def test_create_user_without_phone_number(self):
        """
            Testing that user model can't be created without phone number
        """

        phone_number = ""

        with self.assertRaises(ValueError):
            user = utils.UserFactory(phone_number=phone_number)

    def test_create_user_without_email(self):

        email = ""

        with self.assertRaises(ValueError):
            user = utils.UserFactory(email=email)

    def test_create_user_model(self):
        """
            Testing creation of user model
        """

        role = utils.RoleFactory()
        user = utils.UserFactory(role_id=role)

        self.assertEqual(role, user.role_id)
        self.assertEqual(user.login, f"{user.name}_{user.last_name}")
        self.assertEqual(str(user), f"{user.name} {user.last_name}, {user.login}")
