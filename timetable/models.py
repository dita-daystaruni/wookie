from django.db import models

# Create your models here.
class CoursesExamInfo(models.Model):
    """
    Will hold info about course exam timetable info
    """
    course_code = models.CharField(max_length=50, default="",blank=False, primary_key=True)
    day = models.CharField(max_length=50, default="",blank=False)
    time = models.CharField(max_length=50, default="",blank=True)
    venue = models.CharField(max_length=50, default="",blank=False)
    campus = models.CharField(max_length=50, default="",blank=False)
    coordinator = models.CharField(max_length=50, null=True,blank=False)
    hrs = models.CharField(max_length=5, default="",blank=False)
    invigilator = models.CharField(max_length=50, null=True, blank=False)