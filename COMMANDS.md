# 📚 Command Reference Sheet

Quick reference for common operations with your TaskFlow To-Do application.

## 🚀 Development Server

### Start the Server
```bash
python manage.py runserver
```

### Start on Different Port
```bash
python manage.py runserver 8001
```

### Access Points
- **Frontend:** http://127.0.0.1:8000
- **API:** http://127.0.0.1:8000/api/
- **Admin:** http://127.0.0.1:8000/admin/

### Stop the Server
Press `CTRL + C`

## 🗄️ Database Operations

### Create Migrations
```bash
python manage.py makemigrations
```

### Apply Migrations
```bash
python manage.py migrate
```

### Show Migration Status
```bash
python manage.py showmigrations
```

### View SQL for Migration
```bash
python manage.py sqlmigrate tasks 0001
```

### Reset Database (Development Only)
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Access Database Shell
```bash
python manage.py dbshell
```

## 🧪 Testing

### Run All Tests
```bash
python manage.py test
```

### Run with Verbosity
```bash
python manage.py test -v 2
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

### Run Specific Test Method
```bash
python manage.py test tasks.tests.TaskAPITest.test_create_task
```

### Run Tests with Coverage (if installed)
```bash
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

## 📦 Package Management

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Update Requirements File
```bash
pip freeze > requirements.txt
```

### Install New Package
```bash
pip install package-name
pip freeze > requirements.txt
```

### Upgrade Package
```bash
pip install --upgrade package-name
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

### Deactivate Virtual Environment
```bash
deactivate
```

### Verify Virtual Environment
```bash
which python  # Should show path in venv
pip list      # Show installed packages
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
git add *.py                 # Add all Python files
```

### Commit Changes
```bash
git commit -m "Your descriptive message"
```

### View Commit History
```bash
git log                      # Full log
git log --oneline            # Compact view
git log --oneline -n 5       # Last 5 commits
git log --graph              # Visual graph
```

### Push to GitHub
```bash
git push                     # Push current branch
git push origin main         # Push to main branch
```

### Pull from GitHub
```bash
git pull                     # Pull current branch
git pull origin main         # Pull main branch
```

### Branch Operations
```bash
git branch                   # List branches
git branch feature-name      # Create branch
git checkout feature-name    # Switch branch
git checkout -b feature-name # Create and switch
git branch -d feature-name   # Delete branch
```

### View Remote
```bash
git remote -v
```

### Undo Changes
```bash
git checkout -- filename.py  # Discard changes in file
git reset HEAD filename.py   # Unstage file
git reset --hard HEAD        # Reset to last commit (CAREFUL!)
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

### Create Task
```bash
# Replace YOUR_TOKEN with actual token from login
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

### Get Specific Task
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/1/ \
  -H "Authorization: Token YOUR_TOKEN"
```

### Update Task (PATCH)
```bash
curl -X PATCH http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{"completed": true}'
```

### Update Task (PUT)
```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{
    "title": "Updated Task",
    "description": "Updated description",
    "completed": true
  }'
```

### Delete Task
```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/ \
  -H "Authorization: Token YOUR_TOKEN"
```

### Filter Tasks
```bash
# Completed tasks
curl -X GET "http://127.0.0.1:8000/api/tasks/?completed=true" \
  -H "Authorization: Token YOUR_TOKEN"

# Active tasks
curl -X GET "http://127.0.0.1:8000/api/tasks/?completed=false" \
  -H "Authorization: Token YOUR_TOKEN"

# Search tasks
curl -X GET "http://127.0.0.1:8000/api/tasks/?search=django" \
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

### Change User Password
```bash
python manage.py changepassword username
```

## 🔍 Django Shell

### Open Django Shell
```bash
python manage.py shell
```

### Common Shell Operations
```python
# Import models
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

# Update task
task.completed = True
task.save()

# Delete task
task.delete()

# Count tasks
Task.objects.count()
Task.objects.filter(completed=True).count()

# Exit shell
exit()
```

## 📝 Useful Django Commands

### Check for Issues
```bash
python manage.py check
```

### Check Deployment Readiness
```bash
python manage.py check --deploy
```

### Collect Static Files
```bash
python manage.py collectstatic
```

### Create New App
```bash
python manage.py startapp appname
```

### Clear Sessions
```bash
python manage.py clearsessions
```

### Show URLs
```bash
python manage.py show_urls  # Requires django-extensions
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

### Clean Git Repository
```bash
git clean -fd  # Remove untracked files
```

## 🐛 Debugging

### Run Server with Debug Output
```bash
python manage.py runserver --verbosity 2
```

### Enable Django Debug Toolbar (if installed)
```python
# Add to INSTALLED_APPS in settings.py
'debug_toolbar',
```

### Print SQL Queries (in shell)
```python
from django.db import connection
print(connection.queries)
```

## 📦 Demo Script

### Run API Demo
```bash
python api_demo.py
```

### Install Requests (if needed)
```bash
pip install requests
```

## 🚀 Deployment Commands

### Generate Secret Key
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Collect Static Files for Production
```bash
python manage.py collectstatic --noinput
```

### Run Production Server (with Gunicorn)
```bash
gunicorn todo_project.wsgi:application --bind 0.0.0.0:8000
```

## 📊 Project Statistics

### Count Lines of Code
```bash
find . -name "*.py" -not -path "./venv/*" | xargs wc -l
```

### List All Python Files
```bash
find . -name "*.py" -not -path "./venv/*" -not -path "./.git/*"
```

### Count Files
```bash
find . -type f | wc -l
```

## 🔄 Common Workflows

### Starting Fresh Development Session
```bash
source venv/bin/activate
python manage.py runserver
```

### Making Model Changes
```bash
# 1. Edit models.py
# 2. Create migrations
python manage.py makemigrations
# 3. Review migration file
# 4. Apply migrations
python manage.py migrate
# 5. Test changes
python manage.py test
```

### Adding New Feature
```bash
# 1. Create feature branch
git checkout -b feature/new-feature

# 2. Make changes
# Edit files...

# 3. Test
python manage.py test

# 4. Commit
git add .
git commit -m "Add new feature"

# 5. Push
git push origin feature/new-feature

# 6. Create pull request on GitHub
```

### Updating from GitHub
```bash
git pull origin main
pip install -r requirements.txt  # If dependencies changed
python manage.py migrate          # If models changed
```

## 🆘 Emergency Commands

### Kill Process on Port 8000
```bash
# macOS/Linux
lsof -ti:8000 | xargs kill -9

# Find process
lsof -i :8000
```

### Reset Everything (Development Only)
```bash
# WARNING: This deletes all data!
deactivate
rm -rf venv/
rm db.sqlite3
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Fix Migration Issues
```bash
# Delete all migrations except __init__.py
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Recreate migrations
python manage.py makemigrations
python manage.py migrate
```

## 📚 Help Commands

### Django Help
```bash
python manage.py help
python manage.py help migrate
python manage.py help test
```

### Git Help
```bash
git help
git help commit
git help push
```

### Python Help
```bash
python --version
pip --version
pip list
```

## 💡 Bash Aliases (Optional)

Add to your `.bashrc` or `.zshrc`:

```bash
# Django shortcuts
alias dj='python manage.py'
alias djrun='python manage.py runserver'
alias djtest='python manage.py test'
alias djmig='python manage.py migrate'
alias djmake='python manage.py makemigrations'
alias djshell='python manage.py shell'
alias djsuper='python manage.py createsuperuser'

# Virtual environment
alias vact='source venv/bin/activate'
alias vdeact='deactivate'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gl='git log --oneline'
```

Then use:
```bash
djrun    # Instead of python manage.py runserver
djtest   # Instead of python manage.py test
vact     # Instead of source venv/bin/activate
```

---

## 📖 Quick Reference Card

| Task | Command |
|------|---------|
| Start server | `python manage.py runserver` |
| Run tests | `python manage.py test` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Create superuser | `python manage.py createsuperuser` |
| Django shell | `python manage.py shell` |
| Git status | `git status` |
| Git commit | `git commit -m "message"` |
| Git push | `git push` |

---

**💡 Tip:** Bookmark this file for quick command reference while developing!

**🔗 Repository:** https://github.com/Pradhyumn1/task_manager
