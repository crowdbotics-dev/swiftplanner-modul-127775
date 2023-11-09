from rest_framework import serializers
from .models import TaskList, Task

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ('id', 'name')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'due_date', 'completed', 'task_list')