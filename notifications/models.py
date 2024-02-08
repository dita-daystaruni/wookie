from django.db import models

# Create your models here.
class Notifications(models.Model):
    """
    Will hold information about notifictions
    """
    date_submitted = models.DateField()
    contents = models.CharField(max_length = 1000, blank=True, null=True)
    upload = models.FileField(null=True, blank=True)
    validity = models.IntegerField(default=0)
    notification_link = models.CharField(max_length=150, blank=True, null=True)

    def get_valid_notifcations(self):
        """
        returns valid notifications
        """
        pass
