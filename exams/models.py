from django.db import models
from django.utils.timezone import timezone


# Create your models here.
class Exam(models.Model):
    """The exams model.

    This model represents the exam entity on the database
    """

    exam_sheet = models.ImageField(
        upload_to="exam_sheets/", null=True, blank=True)
    semester = models.CharField(max_length=20, blank=False, null=False)
    date_submitted = models.DateField(default=timezone.now)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
