from rest_framework.generics import ListCreateAPIView

from . import serializers
from .models import Role, User
from core.mixins import CustomUpdateMixin, CustomDeleteMixin


class RoleViews(ListCreateAPIView, CustomDeleteMixin):
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
        """
        Custom DELETE method defined in CustomDeleteMixin
        """
        return self.destroy(request, *args, **kwargs)


class UserViews(ListCreateAPIView, CustomDeleteMixin, CustomUpdateMixin):
    """
    Class for user endpoints
    """
    model = User
    queryset = User.objects.all()

    def get_object(self):
        return self.custom_get_object()

    def get_serializer_class(self):
        """
        Method for getting serializer depending on request method
        """
        method = self.request.method

        if method == "DELETE":
            return serializers.UserDeleteSerializer
        if method == "POST":
            return serializers.UserCreateSerializer
        if method == "PUT" or method == "PATCH":
            return serializers.UserUpdateSerializer
        return serializers.UserDetailSerializer

    def delete(self, request, *args, **kwargs):
        """
        Custom DELETE method defined in CustomDeleteMixin
        """
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Custom PUT method defined in CustomUpdateMixin
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Custom PATCH method defined in CustomUpdateMixin
        """
        return self.partial_update(request, *args, **kwargs)

