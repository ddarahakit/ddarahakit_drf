from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .serializer import TopicSerializer
from .models import Topic


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [AllowAny]

