import factory
from faker import Faker

from meals import models

fake = Faker()


class DepartmentFactory(factory.django.DjangoModelFactory):
    """
        Class for creating fake department models
    """

    class Meta:
        model = models.Department

    name = fake.job()


class MealCategoryFactory(factory.django.DjangoModelFactory):
    """
    Class for creating fake meal category models
    """

    class Meta:
        model = models.MealCategory

    name = fake.job()
    department_id = factory.SubFactory(DepartmentFactory)


class MealFactory(factory.django.DjangoModelFactory):
    """
        Class for creating fake meal models
    """

    class Meta:
        model = models.Meal

    name = fake.pystr(min_chars=10, max_chars=20)
    category_id = factory.SubFactory(MealCategoryFactory)
    price = fake.pyint(min_value=100, max_value=9999, step=1)
    description = fake.paragraph(nb_sentences=3)
