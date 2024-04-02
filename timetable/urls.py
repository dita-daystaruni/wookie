"""Defines the urls to be used by the timetable app."""

from django.urls import path
from .views import ParseTimeTablesAPI

urlpatterns = [
    path("parse/", ParseTimeTablesAPI.as_view(), name="parser"),
]
