"""
Sample script demonstrating how to interact with the To-Do List API.
This script shows how to register, login, create tasks, and perform other operations.

Requirements:
    pip install requests

Usage:
    python api_demo.py
"""

import requests
import json

# Configuration
BASE_URL = "http://127.0.0.1:8000"
API_URL = f"{BASE_URL}/api"


def print_response(title, response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")
    print(f"{'='*60}\n")


def main():
    """Main demonstration function"""
    
    # Step 1: Register a new user
    print("\n🚀 STEP 1: Registering a new user...")
    register_data = {
        "username": "demouser",
        "email": "demo@example.com",
        "password": "demopass123",
        "password2": "demopass123",
        "first_name": "Demo",
        "last_name": "User"
    }
    
    response = requests.post(f"{API_URL}/auth/register/", json=register_data)
    print_response("Registration", response)
    
    if response.status_code == 201:
        token = response.json()['token']
        print(f"✅ Registration successful! Token: {token}")
    else:
        # If user already exists, try to login
        print("⚠️  User might already exist. Trying to login...")
        login_data = {
            "username": "demouser",
            "password": "demopass123"
        }
        response = requests.post(f"{API_URL}/auth/login/", json=login_data)
        print_response("Login", response)
        
        if response.status_code == 200:
            token = response.json()['token']
            print(f"✅ Login successful! Token: {token}")
        else:
            print("❌ Failed to login. Exiting...")
            return
    
    # Set up headers with authentication token
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }
    
    # Step 2: Create some tasks
    print("\n\n🚀 STEP 2: Creating tasks...")
    
    tasks_to_create = [
        {
            "title": "Learn Django",
            "description": "Complete Django tutorial and build a REST API",
            "completed": False
        },
        {
            "title": "Learn DRF",
            "description": "Master Django REST Framework",
            "completed": True
        },
        {
            "title": "Build Portfolio Project",
            "description": "Create a To-Do List API for portfolio",
            "completed": False
        }
    ]
    
    created_task_ids = []
    
    for task_data in tasks_to_create:
        response = requests.post(f"{API_URL}/tasks/", json=task_data, headers=headers)
        print_response(f"Creating Task: {task_data['title']}", response)
        
        if response.status_code == 201:
            created_task_ids.append(response.json()['id'])
            print(f"✅ Task created successfully!")
        else:
            print(f"❌ Failed to create task")
    
    # Step 3: List all tasks
    print("\n\n🚀 STEP 3: Listing all tasks...")
    response = requests.get(f"{API_URL}/tasks/", headers=headers)
    print_response("All Tasks", response)
    
    # Step 4: Filter completed tasks
    print("\n\n🚀 STEP 4: Filtering completed tasks...")
    response = requests.get(f"{API_URL}/tasks/?completed=true", headers=headers)
    print_response("Completed Tasks", response)
    
    # Step 5: Filter incomplete tasks
    print("\n\n🚀 STEP 5: Filtering incomplete tasks...")
    response = requests.get(f"{API_URL}/tasks/?completed=false", headers=headers)
    print_response("Incomplete Tasks", response)
    
    # Step 6: Search tasks
    print("\n\n🚀 STEP 6: Searching for 'Django' tasks...")
    response = requests.get(f"{API_URL}/tasks/?search=Django", headers=headers)
    print_response("Search Results", response)
    
    # Step 7: Update a task
    if created_task_ids:
        task_id = created_task_ids[0]
        print(f"\n\n🚀 STEP 7: Updating task {task_id}...")
        
        update_data = {
            "completed": True
        }
        
        response = requests.patch(
            f"{API_URL}/tasks/{task_id}/",
            json=update_data,
            headers=headers
        )
        print_response(f"Update Task {task_id}", response)
        
        if response.status_code == 200:
            print(f"✅ Task updated successfully!")
    
    # Step 8: Get user profile
    print("\n\n🚀 STEP 8: Getting user profile...")
    response = requests.get(f"{API_URL}/auth/profile/", headers=headers)
    print_response("User Profile", response)
    
    # Step 9: Delete a task
    if len(created_task_ids) > 1:
        task_id = created_task_ids[-1]
        print(f"\n\n🚀 STEP 9: Deleting task {task_id}...")
        
        response = requests.delete(
            f"{API_URL}/tasks/{task_id}/",
            headers=headers
        )
        print_response(f"Delete Task {task_id}", response)
        
        if response.status_code == 200:
            print(f"✅ Task deleted successfully!")
    
    # Step 10: Logout
    print("\n\n🚀 STEP 10: Logging out...")
    response = requests.post(f"{API_URL}/auth/logout/", headers=headers)
    print_response("Logout", response)
    
    if response.status_code == 200:
        print(f"✅ Logged out successfully!")
    
    print("\n\n" + "="*60)
    print("🎉 Demo completed successfully!")
    print("="*60)


if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the server.")
        print("Make sure the Django development server is running:")
        print("    python manage.py runserver")
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
