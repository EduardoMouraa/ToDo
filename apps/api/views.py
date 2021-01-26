from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import render

from .serializers import TasksSerializers, UserSerializers
from apps.users.models import User
from apps.tasks.models import Task
from apps.tasks.tasks import checkTask

from datetime import datetime, timedelta

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TasksSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        task = Task.objects.get(id=pk)
        serializer = TasksSerializers(task)
        return Response(serializer.data)

    def create(self, request):
        response = {"success": "Tarefa criada com sucesso."}
        serializer = TasksSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            checkTask.apply_async(
                ({'id_task': serializer.data['id']}, ),
                eta=(datetime.strptime(serializer.data['schedule_date'], "%Y-%m-%dT%H:%M:00Z") + timedelta(hours=3))
            )
        else:
            response = {"Failed": "Erro na criação da tarefa."}

        return Response(response)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = User.objects.get(id=pk)
        serializer = UserSerializers(user)
        return Response(serializer.data)