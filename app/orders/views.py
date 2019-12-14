from rest_framework.generics import ListAPIView, ListCreateAPIView, get_object_or_404
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from core.mixins import CustomDeleteMixin
from . import serializers
from .models import Check, Order, Table


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


class AddMealToOrder(ListCreateAPIView, UpdateModelMixin, RetrieveModelMixin):
    """
    Class for listing meals of an order and adding additional meals to order
    """

    model = Order
    queryset = Order.objects.all()
    serializer_class = serializers.MealToOrderSerializer

    def delete(self, request, *args, **kwargs):
        """
        Custom DELETE method, which accepts an order_id, meal_id, amount
        """
        instance = self.get_object()
        instance.remove_meal(request)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Custom POST method that accepts order_id and meals and updates them
        """
        instance = self.get_object()
        instance.add_meals(request)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        """
        Custom GET method that accepts order_id and return all related meals
        """
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        """
        Returns the object the view is displaying.
        Gets object by an id from request
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Getting object by an id of object
        obj = get_object_or_404(queryset, pk=self.request.data["order_id"])

        # May raise permission denied
        self.check_object_permissions(self.request, obj)

        return obj


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
