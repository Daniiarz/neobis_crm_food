from rest_framework import serializers
from .models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    """
    Class for serializing role objects
    """

    class Meta:
        model = Role
        fields = (
            "id",
            "name"
        )
        read_only_fields = ('id',)


class RoleDeleteSerializer(serializers.ModelSerializer):
    """
    Class for deleting role instances
    """
    class Meta:
        model = Role
        fields = (
            "id",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Class for serializing user objects on create
    """
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "role_id",
            "phone"
        )

    def create(self, validated_data):
        User.objects.create_user(**validated_data)
        return validated_data


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Class for Serializing detailed information about User
    """

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "login",
            "password",
            "email",
            "role_id",
            "date_of_add",
            "phone",
        )
        read_only_fields = ("id", "password")


class UserDeleteSerializer(serializers.ModelSerializer):
    """
    Class for serializing User objects when deleting
    """

    class Meta:
        model = User
        fields = (
            "id"
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Class for Serializing detailed information about User
    """

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "password",
            "email",
            "role_id",
            "phone",
        )
        read_only_fields = ("id",)
