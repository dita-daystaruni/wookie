from django.shortcuts import render
from .models import Notifications
from .serializers import NotificationsSrializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date


# Create your views here.
class NotificationsAPI(APIView):
    """
    Used to handle notifications services
    """
    def post(self, request, *args, **kwargs):
        """
        Will receive Notifications and store them in server
        """
        content = request.data.get("content")
        files = request.data.get("file")
        if not content or not files:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if 
        new_notification = Notifications()

    def get(self, request, *arg, **kwargs):
        """
        Will return valid notifications for posting
        """
        pass