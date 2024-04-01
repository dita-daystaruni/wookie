"""Definition to the timetable serializer."""

from .models import CoursesExamInfo
from rest_framework import serializers


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
