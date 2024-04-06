"""Defines the urls to be used by the timetable app."""

from django.urls import path
from .views import ParseTimeTablesAPI, ExamsCourseInfoAPI

urlpatterns = [
    path("parse/", ParseTimeTablesAPI.as_view(), name="parser"),
    path("exams/", ExamsCourseInfoAPI.as_view(), name="exams"),
]
