from django.db import models
from django.db.models import F
from django.utils import timezone
from datetime import date

# Create your models here.
class Notifications(models.Model):
    """
    Will hold information about notifictions
    """
    date_submitted = models.DateField(default=timezone.now)
    contents = models.CharField(max_length = 1000, blank=True, null=True)
    upload = models.FileField(null=True, blank=True)
    validity = models.IntegerField(default=0)
    notification_link = models.CharField(max_length=150, blank=True, null=True)
    style = models.CharField(max_length=100, blank=True, null=True)
    sender = models.CharField(max_length=100, blank=False, null=False, default='')
    file_type = models.CharField(max_length=10, blank=False, null=False, default='')

    @staticmethod
    def get_valid_notifcations():
        """
        returns valid notifications
        """
        data = [] # holds data to be returned
        today = date.today()
        valid_notifications = Notifications.objects.filter(validity__gte=(today - F('date_submitted')))
        if valid_notifications:
            for valid_notification in valid_notifications:
                notification = {}
                notification['contents'] = valid_notification.contents
                notification['upload_url'] = 'http://127.0.0.1:8000' + valid_notification.upload.url
                notification['notification_link'] = valid_notification.notification_link
                notification['style'] = valid_notification.style
                notification['file_type'] = valid_notification.file_type
                data.append(notification)
        return data
