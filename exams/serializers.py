"""Contains the serializer definition for exams."""

from rest_framework import serializers
from .models import Exam


class ExamSerializer(serializers.ModelSerializer):
    """The Exam Serializer."""

    class Meta:
        """Define the fields to be serialized to and fro json."""

        model = Exam
        fields = [
            "id",
            "semester",
            "exam_sheet",
            "date_submitted",
            "start_date",
            "end_date",
        ]
