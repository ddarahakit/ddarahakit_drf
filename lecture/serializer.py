from rest_framework import serializers
from rest_framework import serializers
from course.models import Course, CourseIcon
from lecture.models import School,Course, CourseIcon


class SchoolSerializer(serializers.ModelSerializer):
    course_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    course_count = serializers.IntegerField(source='course_set.count')

    class Meta:
        model = School
        fields = '__all__'



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
