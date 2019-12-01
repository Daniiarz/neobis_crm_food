from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r"roles", views.RoleViewSet)

urlpatterns = [
    path("roles/", views.RoleViews.as_view(), name="roles")
]
