from rest_framework import serializers
from apps.tasks.models import Task
from apps.users.models import User


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","is_superuser","first_name", "last_name", "is_staff","is_active","username","email")
            