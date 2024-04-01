from django.shortcuts import render
from .models import Notifications
from .serializers import NotificationsSerializer, MessageSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class NotificationsAPI(APIView):
    """Handles notification services."""

    def get(self, request, *arg, **kwargs):
        """Return notifications that are to be displayed."""
        valid_notifications = Notifications.get_valid_notifcations()
        return Response(data=valid_notifications, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Recieve a notification and stores it."""
        contents = request.data.get("contents")
        upload = request.data.get("file")
        sender = request.data.get("sender")
        file_type = request.data.get("file_type")

        if not contents and not upload:
            data = {"message": "Missing Post Content or Post Uploads"}
            serializer = MessageSerializer(data)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        if not sender or not file_type:
            data = {"message": "Missing File Type or Sender Name"}
            serializer = MessageSerializer(data)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        # receiving request data
        data = {
            "contents": contents,
            "upload": upload,
            "validity": request.data.get("validity"),
            "notification_link": request.data.get("notification_link"),
            "sender": request.data.get("sender"),
            "file_type": request.data.get("file_type"),
        }
        serializer = NotificationsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
