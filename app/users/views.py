from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response

from . import serializers
from .models import Role, User


class RoleViews(ListCreateAPIView, DestroyModelMixin ):
    """
        Class for creating, listing and deleting course models
    """
    model = Role
    queryset = Role.objects.all()

    def get_serializer_class(self):
        """
            Method for getting serializer depending on request method
        """
        if self.request.method == "DELETE":
            return serializers.RoleDeleteSerializer
        return serializers.RoleSerializer

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(self.model, pk=request.data["id"])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class UserViews(ListCreateAPIView, DestroyModelMixin, UpdateModelMixin):
    """
        Class for user endpoints
    """
    model = User
    queryset = User.objects.all()

    def get_serializer_class(self):
        """
            Method for getting serializer depending on request method
        """
        if self.request.method == "DELETE":
            return serializers.UserDeleteSerializer
        if self.request.method == "POST":
            return serializers.UserCreateSerializer
        return serializers.UserDetailSerializer

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(self.model)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


