from rest_framework import serializers
from .models import MealCategory, Meal, Department


class DepartmentSerializer(serializers.ModelSerializer):
    """
        Class for serializing Department models
    """

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class DepartmentDeleteSerializer(serializers.ModelSerializer):
    """
        Class for serializing Department models on DELETE method
    """

    class Meta:
        model = Department
        fields = {
            "id"
        }


class MealCategorySerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )

    class Meta:
        model = MealCategory
        fields = (
            "id",
            "name",
            "department_id",
        )
        read_only_fields = ("id",)


class MealCategoryDeleteSerializer(serializers.ModelSerializer):
    """
    Class for serializing MealCategory models on DELETE method
    """
    class Meta:
        model = MealCategory
        fields = (
            "id"
        )


class MealSerializer(serializers.ModelSerializer):
    """
    Class for serializing Meal models
    """
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=MealCategory.objects.all()
    )

    class Meta:
        model = Meal
        fields = (
            "id",
            "category_id",
            "name",
            "price",
            "description"
        )
        read_only_fields = ("id",)


class MealDeleteSerializer(object):
    """
    Class for serializing Meal models on DELETE method
    """
    class Meta:
        model = Meal
        fields = (
            "id",
        )
