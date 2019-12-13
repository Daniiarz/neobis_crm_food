from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from . import serializers
from .models import Table, Order
from core.mixins import CustomUpdateMixin, CustomDeleteMixin


class TableView(ListCreateAPIView, CustomDeleteMixin):
    """
    Class responsible for endpoints of departments model
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
    Class responsible for endpoints of departments model
    """

    queryset = Order.objects.all()
    model = Order
    serializer_class = serializers.OrderSerializer

    def delete(self, request, *args, **kwargs):
        """
        Custom DELETE method, which accepts an id from request and delete corresponding model
        """
        return self.destroy(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     """Create a new order"""
    #     serializer.save(waiter_id=self.request.user)
