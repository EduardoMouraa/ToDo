from rest_framework import serializers
from apps.tasks.models import Task


class TasksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'