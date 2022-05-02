from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Chapter
from .serializer import ChapterSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [AllowAny]
