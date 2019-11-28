import factory
from faker import Faker

from meals import models

fake = Faker()


class RoleFactory(factory.django.DjangoModelFactory):
    """
        Class for creating fake department models
    """

    class Meta:
        model = models.Department

    name = fake.job()