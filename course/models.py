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
    name = models.CharField(
        max_length=256,
        blank=False,
        null=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        String representation for the model
        """
        return f"{self.unit}"

    def save(self, *args, **kwargs):
        """
        Neatly set the case of the data
        """
        self.unit = str(self.unit).upper()
        if self.name == "" or self.name is None:
            self.name = str(self.unit).title()

        super().save()
