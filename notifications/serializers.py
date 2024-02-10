from .models import Notifications
from rest_framework import serializers

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['contents', 'upload', 'validity', 'notification_link', 'style', 'sender', 'file_type']

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=100)