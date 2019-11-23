import factory
from faker import Faker

from users import models
from users.utils import login_creator

fake = Faker()


class RoleFactory(factory.django.DjangoModelFactory):
    """
        Class for creating random role models
    """

    class Meta:
        model = models.Role

    name = fake.job()


class UserFactory(factory.django.DjangoModelFactory):
    """
        Class for creating random role models
    """

    class Meta:
        model = models.User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    role_id = factory.SubFactory(RoleFactory)
    phone = fake.phone_number()
