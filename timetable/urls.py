"""Defines the urls to be used by the timetable app."""

from django.urls import path
from .views import ParseTimeTablesAPI, ExamsCourseInfoAPI
from .views import ExamInfoTruncateAPI

urlpatterns = [
    path("parse/", ParseTimeTablesAPI.as_view(), name="parser"),
    path("exams/", ExamsCourseInfoAPI.as_view(), name="exams"),
    path("truncate/", ExamInfoTruncateAPI.as_view(), name="truncate"),
]
