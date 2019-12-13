from django.conf import settings
from django.db import IntegrityError, models


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


class CheckManager(models.Manager):
    """
    Class for managing check instances
    """

    def create_check(self, order_id):
        if not order_id:
            raise IntegrityError("Order is required!")

        order_id.is_open = False
        total_sum = 0
        for specific_meal in order_id.meals_id.all():
            total_sum += specific_meal.get_total_price()

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
