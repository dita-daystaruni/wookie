"""Definition to the notification serializer."""

from .models import Notifications
from rest_framework import serializers


class NotificationsSerializer(serializers.ModelSerializer):
    """The Notification Serializer Class."""

    class Meta:
        """Defines the notification serializer."""

        model = Notifications
        fields = [
            "contents",
            "upload",
            "validity",
            "notification_link",
            "style",
            "sender",
            "file_type",
        ]


class MessageSerializer(serializers.Serializer):
    """The message serializer."""

    message = serializers.CharField(max_length=100)
