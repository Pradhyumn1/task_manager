# 📚 Command Reference Sheet

Quick reference for common operations with your To-Do List API.

## 🚀 Development Server

### Start the Server
```bash
python manage.py runserver
```

### Start on Different Port
```bash
python manage.py runserver 8001
```

### Stop the Server
Press `CTRL + C`

## 🗄️ Database Operations

### Make Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Reset Database
```bash
rm db.sqlite3
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

## 🧪 Testing

### Run All Tests
```bash
python manage.py test
```

### Run Specific App Tests
```bash
python manage.py test tasks
python manage.py test authentication
```

### Run Specific Test Class
```bash
python manage.py test tasks.tests.TaskAPITest
```

### Run with Verbosity
```bash
python manage.py test -v 2
```

## 📦 Package Management

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Update Requirements
```bash
pip freeze > requirements.txt
```

### Install New Package
```bash
pip install package-name
pip freeze > requirements.txt
```

## 🔐 Environment Setup

### Create Virtual Environment
```bash
python3 -m venv venv
```

### Activate Virtual Environment
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Deactivate
```bash
deactivate
```

## 🐙 Git Commands

### Check Status
```bash
git status
```

### Add Files
```bash
git add .                    # Add all files
git add filename.py          # Add specific file
```

### Commit Changes
```bash
git commit -m "Your message here"
```

### Push to GitHub
```bash
git push
git push origin main         # Specific branch
```

### Pull from GitHub
```bash
git pull
```

### View Commit History
```bash
git log
git log --oneline           # Compact view
```

### Create Branch
```bash
git checkout -b feature-name
```

### Switch Branch
```bash
git checkout main
git checkout feature-name
```

## 🌐 API Testing with cURL

### Register User
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123",
    "password2": "testpass123"
  }'
```

### Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

### Create Task (Replace YOUR_TOKEN)
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{
    "title": "My Task",
    "description": "Task description",
    "completed": false
  }'
```

### List Tasks
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Token YOUR_TOKEN"
```

### Update Task
```bash
curl -X PATCH http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{"completed": true}'
```

### Delete Task
```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/ \
  -H "Authorization: Token YOUR_TOKEN"
```

## 📊 Django Admin

### Access Admin Panel
```
http://127.0.0.1:8000/admin/
```

### Create Superuser
```bash
python manage.py createsuperuser
```

## 🔍 Database Shell

### Django Shell
```bash
python manage.py shell
```

### Inside Shell
```python
from tasks.models import Task
from django.contrib.auth.models import User

# Get all tasks
tasks = Task.objects.all()

# Get specific user's tasks
user = User.objects.get(username='testuser')
user_tasks = Task.objects.filter(user=user)

# Create a task
task = Task.objects.create(
    title='Test Task',
    description='Created from shell',
    user=user,
    completed=False
)

# Exit shell
exit()
```

## 📝 Useful Django Commands

### Check for Issues
```bash
python manage.py check
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Create App
```bash
python manage.py startapp appname
```

### Show Migrations
```bash
python manage.py showmigrations
```

### SQL for Migration
```bash
python manage.py sqlmigrate tasks 0001
```

## 🧹 Cleanup Commands

### Remove Python Cache
```bash
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

### Remove Database
```bash
rm db.sqlite3
```

## 🐛 Debugging

### Run Server with Debug Output
```bash
python manage.py runserver --verbosity 2
```

### Check Database
```bash
python manage.py dbshell
```

### Show URLs
```bash
python manage.py show_urls  # Requires django-extensions
```

## 📦 Demo Script

### Run API Demo
```bash
python api_demo.py
```

## 🚀 Deployment

### Generate Secret Key
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Check Deployment Readiness
```bash
python manage.py check --deploy
```

## 📊 Statistics

### Count Lines of Code
```bash
find . -name "*.py" -not -path "./venv/*" | xargs wc -l
```

### List All Python Files
```bash
find . -name "*.py" -not -path "./venv/*" -not -path "./.git/*"
```

## 🔄 Update Workflow

```bash
# 1. Make changes to code
# 2. Run tests
python manage.py test

# 3. Add changes to git
git add .

# 4. Commit with message
git commit -m "Add feature X"

# 5. Push to GitHub
git push

# 6. Profit! 🎉
```

## 🆘 Emergency Commands

### Kill Process on Port 8000
```bash
lsof -ti:8000 | xargs kill -9
```

### Reset Everything
```bash
rm -rf venv/
rm db.sqlite3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## 📚 Help Commands

### Django Help
```bash
python manage.py help
python manage.py help migrate
```

### Git Help
```bash
git help
git help commit
```

---

**💡 Tip:** Bookmark this file for quick reference!

**🔖 Pro Tip:** Create aliases for frequently used commands in your `.bashrc` or `.zshrc`:

```bash
alias dj='python manage.py'
alias djrun='python manage.py runserver'
alias djtest='python manage.py test'
alias djmig='python manage.py migrate'
```

Then you can just use:
```bash
djrun    # Instead of python manage.py runserver
djtest   # Instead of python manage.py test
```
