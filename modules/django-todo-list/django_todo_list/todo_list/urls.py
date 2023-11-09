from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TaskListViewSet, TaskViewSet

router = DefaultRouter()
router.register(r"task-lists", TaskListViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    # Your other URL patterns
    path("", include(router.urls)),
]
