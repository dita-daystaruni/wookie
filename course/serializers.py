from rest_framework import serializers

from course.models import Course, Lesson


class CourseSerializer(serializers.Serializer):
    """
    The course serializer
    """

    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.Serializer):
    """The lesson serializer"""

    class Meta:
        model = Lesson
        fields = "__all__"
