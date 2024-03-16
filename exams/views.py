"""Exam Module Views.

Author: Erick Muuo
Copyright (C) Academia 2024 All Rights Reserved
"""

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView
from .serializers import ExamSerializer
from .models import Exam


# Create your views here.
class ExamsApiView(APIView):
    """ExamsApiView.

    Return the most recent exam name.
    """

    def get(self, request, *arg, **kwargs):
        """Return the most recent exam info."""
        return Response({"exams": True}, status=HTTP_200_OK)

    def post(self, request, *arg, **kwargs):
        """Register an exam."""
        serializer = ExamSerializer(data=request.data)

        if serializer.is_valid():
            # Save to the db and return 200
            serializer.save()
            return Response({"message": "success"}, status=HTTP_200_OK)
        else:
            return Response(
                {
                    "error": "There was an error saving exam",
                    "details": serializer.errors,
                },
                status=HTTP_406_NOT_ACCEPTABLE,
            )
        return Response(
            {"error": "The sun is shining its the end of the world"},
            status=HTTP_500_INTERNAL_SERVER_ERROR,
        )

    def put(self, request, *arg, **kwargs):
        """Find an exam."""
        recent = Exam.objects.all().last()
        print(recent.exam_sheet)

        # try openning the excel file
        return Response({"message": "Feature coming soon"}, status=HTTP_200_OK)


class ExamListView(ListAPIView):
    """Return a list of all exams registered."""

    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
