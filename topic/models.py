from django.db import models
from course.models import Course

class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    detail = models.TextField()
    difficulty = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    course = models.ManyToManyField(Course, blank=True)
    theme = models.CharField(max_length=20)

    def __str__(self) : return '%s' % (self.name)


