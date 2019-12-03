from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response

from . import serializers
from .models import Role, User


class RoleViews(GenericAPIView, CreateModelMixin, DestroyModelMixin, ListModelMixin):
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

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # In my opinion used to check whether error is in creation of model or in post method
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
        print(request.data)
        instance = get_object_or_404(self.model)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


