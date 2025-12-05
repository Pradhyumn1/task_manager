from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """
    Task model representing a to-do item.
    
    Fields:
        title: Short description of the task
        description: Detailed description (optional)
        completed: Boolean indicating completion status
        user: Foreign key to the User who owns this task
        created_at: Timestamp when task was created
        updated_at: Timestamp when task was last updated
    """
    title = models.CharField(max_length=200, help_text="Short description of the task")
    description = models.TextField(blank=True, help_text="Detailed description of the task")
    completed = models.BooleanField(default=False, help_text="Task completion status")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        help_text="User who owns this task"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Most recent tasks first
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"{self.title} - {'✓' if self.completed else '✗'}"
