from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
)

from course.models import Course
from course.serializers import CourseSerializer
from wookie.pagination_result_sets import ResultsSetPagination


class CoursesListView(ListAPIView):
    """
    Lists all courses in a paginated format as per the ResultsSetPagination
    """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = ResultsSetPagination


class CoursesCreateView(CreateAPIView):
    """
    A view to create a course
    """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDeleteView(DestroyAPIView):
    """
    Deletes a course from DB
    """

    def delete(self, request, *args, **kwargs):
        """
        Specify to the user they are not authorized to perform this action.
        Only the admin interface can delete a course once written.
        """
        return Response(
            {
                "error": "Strong with the force you are not, more training you need",
                "details": "You lack the necessarry permissions to delete this artifact",
            },
            status=HTTP_401_UNAUTHORIZED,
        )
