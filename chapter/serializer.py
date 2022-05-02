from rest_framework import serializers

from chapter.models import Chapter
from lesson.serializer import LessonSerializer


class ChapterSerializer(serializers.ModelSerializer):
    lesson_set = serializers.StringRelatedField(many=True)
    class Meta:
        model = Chapter
        fields = '__all__'



