"""Defines the urls to be used."""

from django.urls import path
from .views import ExamsApiView, ExamListView

urlpatterns = [
    path("", ExamsApiView.as_view(), name="exams"),
    path("listings", ExamListView.as_view(), name="exams-listings"),
]
