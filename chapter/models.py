from django.db import models

from topic.models import Topic


class Chapter(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    def __str__(self) : return self.name

