from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, models

from meals import models as md


class Table(models.Model):
    """
    Model for holding table objects
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Model for Order objects
    """

    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="orders")
    waiter_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    date = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f"Order #{self.pk}, {self.date}"

    def add_meals(self, request):
        """
        Adding meals to order
        """

        specific_meals = self.meals_id

        data = request.data
        meals = data.pop("meals_id")

        for meal in meals:
            amount = meal["amount"]
            meal_id = meal["meal_id"]
            try:
                s_meal = specific_meals.get(meal_id=meal_id)
                s_meal.amount += amount
                s_meal.save()
            except ObjectDoesNotExist:
                md.SpecificMeal.objects.create(order_id=self, amount=amount, meal_id=meal_id)

        return self

    def remove_meal(self, request):
        """
        Removing some meals
        """
        data = request.data

        specific_meal = self.meals_id.get(meal_id=data["meal_id"])
        specific_meal.amount -= data["amount"]

        if specific_meal.amount <= 0:
            specific_meal.delete()
        else:
            specific_meal.save()

        return self


class CheckManager(models.Manager):
    """
    Class for managing check instances
    """

    def create_check(self, order_id):
        if not order_id:
            raise IntegrityError("Order is required!")

        order_id.is_open = False

        prices = [specific_meal.get_total_price() for specific_meal in order_id.meals_id.all()]
        total_sum = sum(prices)

        service_fee = total_sum / 4
        check = self.model(
            order_id=order_id,
            service_fee=service_fee,
            total_sum=total_sum
        )
        check.save(using=self._db)

        return check


class Check(models.Model):
    """
    Model for Check objects
    """

    order_id = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="order_check")
    date = models.DateTimeField(auto_now_add=True)
    service_fee = models.IntegerField()
    total_sum = models.IntegerField()

    objects = CheckManager()

    def __str__(self):
        return f"Order ID-{self.order_id.pk}, Date-{self.date}, Total sum-{self.total_sum}"
