from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from django.shortcuts import render

from apps.tasks.models import Task
from .serializers import TasksSerializers


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TasksSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        task = Task.objects.get(id=pk)
        serializer = TasksSerializers(task)
        return Response(serializer.data)
