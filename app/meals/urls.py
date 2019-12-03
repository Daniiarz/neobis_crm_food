from django.urls import path, include
from . import views

urlpatterns = [
    path("departments/", views.DepartamentView().as_view(), name="departments"),
    path("meals/", views.MealCategoryView.as_view(), name="meal-categories"),

]
