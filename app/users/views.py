from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_auth.registration.views import RegisterView as RView, sensitive_post_parameters_m
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.mixins import CustomDeleteMixin, CustomUpdateMixin
from . import serializers
from .models import Role, User


class RoleViews(ListCreateAPIView, CustomDeleteMixin):
    """
    Class for creating, listing and deleting course models
    """
    model = Role
    queryset = Role.objects.all()
    serializer_class = serializers.RoleSerializer

    def delete(self, request, *args, **kwargs):
        """
        function responsible for DELETE method defined in CustomDeleteMixin
        """
        return self.destroy(request, *args, **kwargs)


class UserViews(ListCreateAPIView, CustomDeleteMixin, CustomUpdateMixin):
    """
    Class for user endpoints
    """
    model = User
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.custom_get_object()

    def get_serializer_class(self):
        """
        Method for getting serializer depending on request method
        """
        method = self.request.method

        if method == "POST":
            return serializers.UserCreateSerializer

        if method == "PUT" or method == "PATCH":
            return serializers.UserUpdateSerializer

        return serializers.UserDetailSerializer

    def delete(self, request, *args, **kwargs):
        """
        function responsible for DELETE method defined in CustomDeleteMixin
        """
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        function responsible for PUT method defined in CustomUpdateMixin
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        function responsible for PATCH method defined in CustomUpdateMixin
        """
        return self.partial_update(request, *args, **kwargs)


class RegisterView(RView):
    """
    Register view
    """
    serializer_class = serializers.SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            {
                'login': user.login,
                'password': user.phone,
                'token': self.get_response_data(user)["key"]
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
