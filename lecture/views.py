from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from .serializer import SchoolSerializer
from .models import School

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [AllowAny]
