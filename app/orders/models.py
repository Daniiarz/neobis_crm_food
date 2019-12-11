from django.db import models
from django.conf import settings


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
    date = models.DateField(auto_now_add=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f"Order #{self.pk}, {self.date}"
