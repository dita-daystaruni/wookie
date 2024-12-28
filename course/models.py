import uuid
from django.db import models


class Course(models.Model):
    """
    Course.
    The course model represents a class's course in the real world
    """

    unit = models.CharField(
        primary_key=True,
        max_length=200,
        null=False,
        blank=False,
        unique=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    semester = models.UUIDField(
        null=False,
        blank=False,
    )
    section = models.CharField(
        max_length=20,
    )
    campus = models.CharField(
        max_length=30,
    )
    weekday = models.CharField(
        max_length=15,
    )

    room = models.CharField(
        max_length=15,
    )
    period = models.CharField(
        max_length=60,
    )

    lecturer = models.CharField(
        max_length=60,
    )
    course = models.ForeignKey(
        Course,
        related_name="lessons_courses",
        on_delete=models.DO_NOTHING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
