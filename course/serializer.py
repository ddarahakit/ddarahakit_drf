from rest_framework import serializers
from course.models import Course, CourseIcon
from lecture.serializer import SchoolSerializer


class CourseIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseIcon
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    courseicon_set = CourseIconSerializer(many=True)
    school = SchoolSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
