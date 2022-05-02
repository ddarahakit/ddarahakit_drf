from django.db import models

from lecture.models import School


class Course(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    detail = models.TextField()
    difficulty = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    school = models.ManyToManyField(School, blank=True)
    theme = models.CharField(max_length=20)

    def __str__(self) : return "{}".format(self.name)

class CourseIcon(models.Model):
    image = models.FileField(upload_to='static/images/course/icon/', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

class CourseBackground(models.Model):
    image = models.ImageField(upload_to='static/images/course/background/', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
