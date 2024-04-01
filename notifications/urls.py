"""Defines the urls to be used by the notifications."""

from django.urls import path
from .views import NotificationsAPI

urlpatterns = [
    path("", NotificationsAPI.as_view(), name="notifications"),
]
