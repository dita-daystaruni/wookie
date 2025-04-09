"""Definition to the timetable serializer."""

from .models import CoursesExamInfo
from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    """The message serializer."""

    message = serializers.CharField(max_length=100)

class CourseExamInfoSerializer(serializers.ModelSerializer):
    """The Timetable Serializer Class."""

    class Meta:
        """Defines the timetable serializer."""

        model = CoursesExamInfo
        fields = [
            "course_code",
            "day",
            "time",
            "venue",
            "campus",
            "coordinator",
            "hrs",
            "invigilator",
        ]
