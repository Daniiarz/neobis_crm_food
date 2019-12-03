from django.urls import path, include
from . import views

urlpatterns = [
    path("roles/", views.RoleViews.as_view(), name="roles")
]
