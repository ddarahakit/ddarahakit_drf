from rest_framework import serializers

from chapter.serializer import ChapterSerializer
from topic.models import Topic



class TopicSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField(many=True)
    chapter_set = ChapterSerializer(many=True)
    class Meta:
        model = Topic
        fields = '__all__'






