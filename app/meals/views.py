from rest_framework import status
from rest_framework.generics import ListCreateAPIView, get_object_or_404, UpdateAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
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
        Custom DELETE method, which accepts an id from request and delete corresponding model
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
        Custom DELETE method, which accepts an id from request and delete corresponding model
        :param request:
        :return: Response()
        """
        instance = get_object_or_404(self.model, pk=request.data["id"])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class MealView(ListCreateAPIView, DestroyModelMixin, UpdateModelMixin):
    """
    Class responsible for endpoints of Meals model
    """
    model = Meal
    queryset = Meal.objects.all()

    def get_serializer_class(self):
        """
        Method for getting serializer depending on request method
        """
        if self.request.method == "DELETE":
            return serializers.MealDeleteSerializer
        return serializers.MealSerializer

    def delete(self, request):
        """
        Custom DELETE method, which accepts an id from request and delete corresponding model
        :param request:
        :return: Response()
        """
        instance = get_object_or_404(self.model, pk=request.data["id"])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = get_object_or_404(self.model, id=request.data["id"])
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
