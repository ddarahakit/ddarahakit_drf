from django.contrib import admin

from .models import Course, CourseIcon, CourseBackground

admin.site.register(Course)
admin.site.register(CourseIcon)
admin.site.register(CourseBackground)