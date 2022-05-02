from django.db import models

from chapter.models import Chapter

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)


    def __str__(self) : return self.name
