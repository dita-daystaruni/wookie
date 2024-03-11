"""Exam Module Views.

Author: Erick Muuo
Copyright (C) Academia 2024 All Rights Reserved
"""

from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView, Response


# Create your views here.
class ExamsApiView(APIView):
    """ExamsApiView.

    Return the most recent exam name.
    """

    def get(self, request, *arg, **kwargs):
        """Return the most recent exam info."""
        return Response({"exams": True}, status=HTTP_200_OK)
