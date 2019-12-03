from rest_framework import status
from rest_framework.generics import ListCreateAPIView, get_object_or_404
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response

from . import serializers
from .models import Department, Meal, MealCategory


class DepartamentView(ListCreateAPIView, DestroyModelMixin):
    """
    Class responsible for endpoints of departments model
    """

    queryset = Department.objects.all()
    model = Department

    def get_serializer_class(self):
        """
        Method for getting serializer depending on request method
        """
        if self.request.method == "DELETE":
            return serializers.DepartmentDeleteSerializer
        return serializers.DepartmentSerializer

    def delete(self, request):
        """
        Custom DELETE method which accepts id from request and delete corresponding model
        :param request:
        :return: Response()
        """
        instance = get_object_or_404(self.model, pk=request.data["id"])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class MealCategoryView(ListCreateAPIView, DestroyModelMixin):
    """
    Class responsible for endpoints of MealCategory model
    """
    model = MealCategory
    queryset = MealCategory.objects.all()

    def get_serializer_class(self):
        """
        Method for getting serializer depending on request method
        """
        if self.request.method == "DELETE":
            return serializers.MealCategoryDeleteSerializer
        return serializers.MealCategorySerializer

    def delete(self, request):
        """
        Custom DELETE method which accepts id from request and delete corresponding model
        :param request:
        :return: Response()
        """
        instance = get_object_or_404(self.model, pk=request.data["id"])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
