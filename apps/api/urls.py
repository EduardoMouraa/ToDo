from django.contrib import admin
from django.urls import path, include
from apps.api.views import TaskViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls), name='api'),
    path('login/', obtain_auth_token),
]