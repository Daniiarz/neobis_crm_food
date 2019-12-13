from django.urls import path
from . import views


urlpatterns = [
    path('tables/', views.TableView.as_view(), name="tables"),
    path('orders/', views.OrderView.as_view(), name="orders")
]
