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
