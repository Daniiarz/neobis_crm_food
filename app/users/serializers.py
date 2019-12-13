from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, serializers

from .models import Role, User

UserModel = get_user_model()


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


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = None

        # Authenticate user
        user = self._validate_username(username, password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs
