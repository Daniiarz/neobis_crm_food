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
    serializer_class = serializers.RoleSerializer
    http_method_names = ["get", "post", "delete", "head"]

    def destroy(self, request, *args, **kwargs):
        # instance = self.model.objects.get(request.POST["id"])
        # self.perform_destroy(instance)
        print(request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
