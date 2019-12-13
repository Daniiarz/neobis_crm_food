from django.db import models

from orders.models import Order


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
    department_id = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="categories"
    )

    def __str__(self):
        return self.name


class Meal(models.Model):
    """
    Class for holding Meal objects
    """

    name = models.CharField(max_length=50)
    category_id = models.ForeignKey(
        MealCategory, on_delete=models.CASCADE, related_name="meals"
    )
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.price} - {self.description}"


class SpecificMeal(models.Model):
    """
    Class for holding multiple Meal models adding amount field
    """
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="specific_meals")
    amount = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="meals_id")

    def get_total_price(self):
        """
        Getting amount * meal_price
        """
        total = self.meal_id.price * self.amount

        return total
