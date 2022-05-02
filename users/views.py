from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import User

from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def set_modified(self, request, pk):
        instance = self.get_object()

        qs = super().get_queryset()

        enrollment = self.request.query_params.get('enrollment', '')
        if enrollment:
            instance.enrollment.add(enrollment)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

