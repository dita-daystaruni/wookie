from django.db import IntegrityError
from rest_framework import serializers

from course.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """
    The course serializer
    """

    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        print("Create called")
        try:
            course = Course.objects.create(**validated_data)
        except Exception:
            course = Course.objects.filter(unit=validated_data.unit)

        return course


class LessonSerializer(serializers.ModelSerializer):
    """The lesson serializer"""

    class Meta:
        model = Lesson
        fields = "__all__"
