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
        read_only_Fields = ('id',)


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
        user = User.objects.create_user(**validated_data)
        return {'login': user.login, 'password': user.password}


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
