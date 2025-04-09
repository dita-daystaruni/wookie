"""Definition to the timetable serializer."""

from .models import CoursesExamInfo
from datetime import datetime
from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    """The message serializer."""

    message = serializers.CharField(max_length=100)

class CourseExamInfoSerializer(serializers.ModelSerializer):
    """The Timetable Serializer Class."""

    datetime_str = serializers.SerializerMethodField()

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
            "datetime_str",
        ]
    def get_datetime_str(self, instance):
        """
        returns Iso format
        """
        time = instance.day.split(' ')[1]
        time += " " + instance.time.split("-")[0]
        # '%m/%d/%Y %I:%M %p'
        time = datetime.strptime(time, "%d/%m/%y %H:%M%p")
        return time.isoformat()