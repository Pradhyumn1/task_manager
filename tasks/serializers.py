from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    Automatically associates tasks with the requesting user.
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'user', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def validate_title(self, value):
        """Ensure title is not empty or just whitespace"""
        if not value or value.strip() == '':
            raise serializers.ValidationError("Title cannot be empty.")
        return value.strip()


class TaskCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating tasks.
    Doesn't expose user field in input.
    """
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed']
        read_only_fields = ['id']

    def validate_title(self, value):
        """Ensure title is not empty or just whitespace"""
        if not value or value.strip() == '':
            raise serializers.ValidationError("Title cannot be empty.")
        return value.strip()
