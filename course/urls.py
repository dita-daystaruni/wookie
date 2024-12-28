from django.urls import path

from course.views import CourseDeleteView, CoursesCreateView, CoursesListView

urlpatterns = [
    path(
        "all",
        CoursesListView.as_view(),
        name="all-courses",
    ),
    path(
        "create",
        CoursesCreateView.as_view(),
        name="create-courses",
    ),
    path(
        "delete",
        CourseDeleteView.as_view(),
        name="delete-courses",
    ),
]
