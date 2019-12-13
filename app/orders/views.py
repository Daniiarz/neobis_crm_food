from rest_framework.generics import ListAPIView, ListCreateAPIView

from core.mixins import CustomDeleteMixin
from . import serializers
from .models import Order, Table, Check


class TableView(ListCreateAPIView, CustomDeleteMixin):
    """
    Class responsible for endpoints of Table model
    """

    queryset = Table.objects.all()
    model = Table
    serializer_class = serializers.TableSerializer

    def delete(self, request, *args, **kwargs):
        """
        Custom DELETE method, which accepts an id from request and delete corresponding model
        """
        return self.destroy(request, *args, **kwargs)


class OrderView(ListCreateAPIView, CustomDeleteMixin):
    """
    Class responsible for endpoints of Order model
    """

    queryset = Order.objects.all()
    model = Order
    serializer_class = serializers.OrderSerializer

    def delete(self, request, *args, **kwargs):
        """
        Custom DELETE method, which accepts an id from request and delete corresponding model
        """
        return self.destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        """Create a new order"""
        serializer.save(waiter_id=self.request.user)


class GetAllActiveOrders(ListAPIView):
    """
    Class for listing orders that are active
    """
    queryset = Order.objects.filter(is_open=True)
    model = Order
    serializer_class = serializers.OrderSerializer


class CheckView(ListCreateAPIView, CustomDeleteMixin):
    """
    Class responsible for endpoints of departments model
    """

    queryset = Check.objects.all()
    model = Check
    serializer_class = serializers.CheckSerializer

    def delete(self, request, *args, **kwargs):
        """
        Custom DELETE method, which accepts an id from request and delete corresponding model
        """
        return self.destroy(request, *args, **kwargs)
