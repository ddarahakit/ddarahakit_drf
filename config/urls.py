from django.contrib import admin
from django.urls import path, include

import lecture.views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj_rest_auth/', include('dj_rest_auth.urls')),
    path('dj_rest_auth/registration/', include('dj_rest_auth.registration.urls')),
    path('allauth/', include('allauth.urls')),
    path('', include('users.urls')),
    path('', include('lecture.urls')),
    path('', include('course.urls')),
    path('', include('topic.urls')),
    path('', include('chapter.urls')),
    path('', include('lesson.urls')),
]
