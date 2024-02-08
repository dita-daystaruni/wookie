from .models import Notifications
from rest_framework import serializers

class NotificationsSrializers(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['date_subitted', 'contents', 'upload', 'validity', 'notification_link']
