from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Task


class TaskModelTest(TestCase):
    """Test Task model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_create_task(self):
        """Test creating a task"""
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            user=self.user
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test Description')
        self.assertFalse(task.completed)
        self.assertEqual(task.user, self.user)

    def test_task_str_representation(self):
        """Test task string representation"""
        task = Task.objects.create(
            title='Test Task',
            user=self.user,
            completed=False
        )
        self.assertIn('Test Task', str(task))
        self.assertIn('✗', str(task))


class TaskAPITest(APITestCase):
    """Test Task API endpoints"""

    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='pass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='pass123'
        )
        
        # Create tokens
        self.token1 = Token.objects.create(user=self.user1)
        self.token2 = Token.objects.create(user=self.user2)
        
        # Create API client
        self.client = APIClient()
        
        # Create some tasks for user1
        self.task1 = Task.objects.create(
            title='Task 1',
            description='Description 1',
            user=self.user1,
            completed=False
        )
        self.task2 = Task.objects.create(
            title='Task 2',
            description='Description 2',
            user=self.user1,
            completed=True
        )
        
        # Create a task for user2
        self.task3 = Task.objects.create(
            title='Task 3',
            description='Description 3',
            user=self.user2,
            completed=False
        )

    def test_list_tasks_authenticated(self):
        """Test listing tasks for authenticated user"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        response = self.client.get('/api/tasks/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # User1 should see only their 2 tasks, not user2's task
        self.assertEqual(len(response.data['results']), 2)

    def test_list_tasks_unauthenticated(self):
        """Test that unauthenticated users cannot list tasks"""
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task(self):
        """Test creating a new task"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'completed': False
        }
        response = self.client.post('/api/tasks/', data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Task')
        self.assertEqual(Task.objects.filter(user=self.user1).count(), 3)

    def test_create_task_without_title(self):
        """Test that creating task without title fails"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        data = {
            'description': 'Description without title',
            'completed': False
        }
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_task(self):
        """Test retrieving a specific task"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        response = self.client.get(f'/api/tasks/{self.task1.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_retrieve_other_user_task(self):
        """Test that users cannot retrieve other users' tasks"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        response = self.client.get(f'/api/tasks/{self.task3.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_task(self):
        """Test updating a task"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        data = {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'completed': True
        }
        response = self.client.put(f'/api/tasks/{self.task1.id}/', data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')
        self.assertTrue(response.data['completed'])

    def test_partial_update_task(self):
        """Test partially updating a task (PATCH)"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        data = {'completed': True}
        response = self.client.patch(f'/api/tasks/{self.task1.id}/', data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['completed'])
        self.assertEqual(response.data['title'], 'Task 1')  # Title unchanged

    def test_delete_task(self):
        """Test deleting a task"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        response = self.client.delete(f'/api/tasks/{self.task1.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.filter(user=self.user1).count(), 1)

    def test_filter_completed_tasks(self):
        """Test filtering tasks by completion status"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        
        # Filter for completed tasks
        response = self.client.get('/api/tasks/?completed=true')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertTrue(response.data['results'][0]['completed'])
        
        # Filter for incomplete tasks
        response = self.client.get('/api/tasks/?completed=false')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertFalse(response.data['results'][0]['completed'])

    def test_search_tasks(self):
        """Test searching tasks"""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)
        response = self.client.get('/api/tasks/?search=Task 1')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Task 1')
