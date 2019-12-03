from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response

from . import serializers
from .models import Role, User


class RoleViews(ListCreateAPIView, DestroyModelMixin):
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

    def destroy(self, request, *args, **kwargs):
        instance = self.model.objects.get(request.data["id"])
        self.perform_destroy(instance)
        print(request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
