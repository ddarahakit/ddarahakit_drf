from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from lesson.models import Lesson
from lesson.serializer import LessonSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [AllowAny]
