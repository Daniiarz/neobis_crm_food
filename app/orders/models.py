from django.db import models

class Table(models.Model):
  """
    Model for holding table objects
  """

  name = models.CharField(max_lenght=50)

  def __str__(self):
    return self.name