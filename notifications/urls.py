from django.urls import path
from .views import NotificationsAPI

urlpatterns = [
    path("notifications/", NotificationsAPI.as_view(), name="notifications"),
]