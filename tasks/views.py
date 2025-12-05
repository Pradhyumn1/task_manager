from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer, TaskCreateUpdateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task model.
    
    Provides CRUD operations for tasks:
    - list: GET /api/tasks/
    - create: POST /api/tasks/
    - retrieve: GET /api/tasks/{id}/
    - update: PUT /api/tasks/{id}/
    - partial_update: PATCH /api/tasks/{id}/
    - destroy: DELETE /api/tasks/{id}/
    
    Filtering:
    - ?completed=true - Get completed tasks
    - ?completed=false - Get incomplete tasks
    - ?search=keyword - Search in title and description
    
    Ordering:
    - ?ordering=created_at - Order by creation date (oldest first)
    - ?ordering=-created_at - Order by creation date (newest first)
    - ?ordering=title - Order alphabetically by title
    """
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at', 'title', 'completed']
    ordering = ['-created_at']  # Default ordering

    def get_queryset(self):
        """
        Return only tasks belonging to the authenticated user.
        """
        return Task.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        """
        Use different serializers for read and write operations.
        """
        if self.action in ['create', 'update', 'partial_update']:
            return TaskCreateUpdateSerializer
        return TaskSerializer

    def perform_create(self, serializer):
        """
        Automatically set the user to the authenticated user when creating a task.
        """
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
        Update task ensuring user ownership.
        """
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        """
        Delete a task with custom response.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Task deleted successfully"},
            status=status.HTTP_200_OK
        )
