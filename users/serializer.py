from rest_framework import serializers

from topic.models import Topic
from topic.serializer import TopicSerializer
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    enrollment = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Topic.objects.all())

    class Meta:
        model = User
        fields = "__all__"


