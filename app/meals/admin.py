from django.contrib import admin
from .models import Meal, MealCategory, Department

# Register your models here.
admin.site.register(Meal)
admin.site.register(MealCategory)
admin.site.register(Department)
