"""Defines the exam model to be used."""

from django.db import models

# from django.utils.timezone import timezone
from datetime import datetime, timedelta


# Create your models here.
class Exam(models.Model):
    """The exams model.

    This model represents the exam entity on the database
    """

    exam_sheet = models.FileField(
        upload_to="exam_sheets/",
        null=False,
        blank=False,
    )
    semester = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )
    date_submitted = models.DateField(auto_now_add=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(
        default=datetime.now() + timedelta(weeks=4),
    )
