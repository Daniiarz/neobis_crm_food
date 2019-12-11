import factory
from faker import Faker

from orders import models
from users.models import User
from users.tests.utils import RoleFactory

fake = Faker()


def create_user_model():
    """
    Creating User model
    :return: User
    """
    role = RoleFactory()
    user_data = {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone": fake.phone_number(),
        "role_id": role,
    }

    return User.objects.create_user(**user_data)


class TableFactory(factory.django.DjangoModelFactory):
    """
    Class for creating fake Department models
    """

    class Meta:
        model = models.Table

    name = fake.job()


class OrderFactory(factory.django.DjangoModelFactory):
    """
    Class for creating fake Order models
    """

    class Meta:
        model = models.Order

    table_id = factory.SubFactory(TableFactory)
    waiter_id = create_user_model()
