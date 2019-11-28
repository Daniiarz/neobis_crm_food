from django.db import models


class Department(models.Model):
    """
		Class for holding Department objects
	"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MealCategory(models.Model):
    """
		Class for holding Meal Category objects
	"""

    name = models.CharField(max_length=50)
    departmnet_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name


class Meal(models.Model):
    """
		Class for holding Meal objects
	"""

    name = models.CharField(max_length=50)
    category_id = models.ForeignKey(
        MealCategory, on_delete=models.CASCADE, related_nam="meals")
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.price} - {self.description}"
