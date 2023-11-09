from rest_framework import viewsets
from .models import TaskList, Task
from .serializers import TaskListSerializer, TaskSerializer

class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer