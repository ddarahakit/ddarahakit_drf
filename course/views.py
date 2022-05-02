from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import CourseSerializer
from .models import Course


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]