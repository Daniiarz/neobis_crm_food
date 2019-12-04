import factory
from faker import Faker

from users import models

fake = Faker()


class RoleFactory(factory.django.DjangoModelFactory):
    """
        Class for creating random role models
    """

    class Meta:
        model = models.Role

    name = fake.job()
