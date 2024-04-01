"""Definition to the notification serializer."""

from .models import CoursesExamInfo
from rest_framework import serializers


class CourseExamInfoSerializer(serializers.ModelSerializer):
    """The Notification Serializer Class."""

    class Meta:
        """Defines the notification serializer."""

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
