from django.shortcuts import render
from .models import Notifications
from .serializers import NotificationsSerializer, MessageSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date


# Create your views here.
class NotificationsAPI(APIView):
    """
    Used to handle notifications services
    """
    def get(self, request, *arg, **kwargs):
        """
        Will return valid notifications for posting
        """
        valid_notifications = Notifications.get_valid_notifcations()
        return Response(data=valid_notifications, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Will receive Notifications and store them in server
        """
        contents = request.data.get("contents")
        upload = request.data.get("file")
        if not contents or not upload:
            data = {"message": "Missing Post Content or Post Uploads"}
            serializer = MessageSerializer(data)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        # receiving request data
        data = {
            "content": contents,
            "upload": upload,
            "validity": request.data.get("validity"),
            "notification_link": request.data.get("notification_link")
        }

        serializer = NotificationsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)