# Contributing to TaskFlow

Thank you for considering contributing to TaskFlow! 🎉

This document provides guidelines for contributing to this To-Do List application.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)

## 🤝 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all. Please be respectful and constructive in all interactions.

### Our Standards

**Positive Behavior:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable Behavior:**
- Harassment or discriminatory language
- Trolling or insulting comments
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

## 🚀 How Can I Contribute?

### Reporting Bugs

**Before submitting a bug report:**
1. Check the [Issues](https://github.com/Pradhyumn1/task_manager/issues) page
2. Search for existing similar issues
3. Try the latest version from `main` branch

**Creating a Bug Report:**

Include these details:
- **Clear title** - Describe the issue concisely
- **Steps to reproduce** - Detailed steps to reproduce the behavior
- **Expected behavior** - What you expected to happen
- **Actual behavior** - What actually happened
- **Screenshots** - If applicable
- **Environment details**:
  - OS: [e.g., macOS 13.0, Windows 10, Ubuntu 22.04]
  - Python version: [e.g., 3.11.0]
  - Django version: [e.g., 4.2.27]
  - Browser (if frontend issue): [e.g., Chrome 120, Safari 17]

**Example:**
```markdown
## Bug: Tasks not filtering correctly

**Steps to reproduce:**
1. Login to the application
2. Create 3 tasks (2 completed, 1 active)
3. Click "Completed" filter
4. Observe results

**Expected:** Should show 2 completed tasks
**Actual:** Shows all 3 tasks

**Environment:**
- OS: macOS 13.0
- Python: 3.11.0
- Browser: Chrome 120
```

### Suggesting Features

**Before submitting a feature request:**
1. Check if the feature already exists
2. Search existing feature requests
3. Consider if it fits the project scope

**Creating a Feature Request:**

Include:
- **Clear title** - Concise feature description
- **Use case** - Why is this feature useful?
- **Proposed solution** - How should it work?
- **Alternatives** - Other approaches you've considered
- **Additional context** - Mockups, examples, references

**Example:**
```markdown
## Feature: Task Categories/Tags

**Use Case:**
Users want to organize tasks by categories (Work, Personal, Shopping, etc.)

**Proposed Solution:**
- Add `category` field to Task model
- Add category dropdown in frontend
- Allow filtering by category
- Display category badge on tasks

**Benefits:**
- Better task organization
- Easier to find related tasks
- More professional functionality
```

### Improving Documentation

Documentation improvements are always welcome:
- Fix typos or unclear explanations
- Add missing information
- Improve code examples
- Add diagrams or screenshots
- Translate documentation

## 💻 Development Setup

### 1. Fork the Repository

Click the "Fork" button on GitHub to create your copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/task_manager.git
cd task_manager
```

### 3. Add Upstream Remote

```bash
git remote add upstream https://github.com/Pradhyumn1/task_manager.git
git remote -v  # Verify remotes
```

### 4. Set Up Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env if needed

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run tests to verify setup
python manage.py test
```

### 5. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

**Branch naming conventions:**
- `feature/` - New features (e.g., `feature/task-categories`)
- `fix/` - Bug fixes (e.g., `fix/filter-bug`)
- `docs/` - Documentation (e.g., `docs/improve-readme`)
- `refactor/` - Code refactoring (e.g., `refactor/serializers`)
- `test/` - Adding tests (e.g., `test/task-api`)

## 📝 Coding Standards

### Python Code Style

Follow [PEP 8](https://pep8.org/) style guide:

```python
# Good
def create_task(title, description, user):
    """Create a new task for the given user."""
    return Task.objects.create(
        title=title,
        description=description,
        user=user,
        completed=False
    )

# Bad
def CreateTask(Title,Description,User):
    return Task.objects.create(title=Title,description=Description,user=User,completed=False)
```

**Key Points:**
- Use 4 spaces for indentation (not tabs)
- Maximum line length: 79 characters for code, 72 for docstrings
- Use meaningful variable names
- Add docstrings to functions and classes
- Add type hints where beneficial

### Django Best Practices

```python
# Good - Use get_object_or_404
from django.shortcuts import get_object_or_404
task = get_object_or_404(Task, pk=task_id, user=request.user)

# Good - Use F expressions for updates
from django.db.models import F
Task.objects.filter(user=request.user).update(views=F('views') + 1)

# Good - Use select_related for foreign keys
tasks = Task.objects.select_related('user').all()
```

### Frontend Code Style

**HTML:**
```html
<!-- Good - Semantic and accessible -->
<button type="submit" class="btn btn-primary" aria-label="Add task">
    Add Task
</button>

<!-- Bad - Non-semantic and inaccessible -->
<div onclick="addTask()">Add Task</div>
```

**CSS:**
```css
/* Good - Organized and commented */
.task-card {
    /* Layout */
    display: flex;
    padding: 20px;
    
    /* Visual */
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    
    /* Animation */
    transition: all 0.3s ease;
}

/* Bad - Disorganized */
.task-card{background:rgba(255,255,255,0.1);padding:20px;display:flex;border-radius:12px;transition:all 0.3s ease;}
```

**JavaScript:**
```javascript
// Good - Clear and modern
async function loadTasks() {
    try {
        const response = await fetch(`${API_BASE_URL}/tasks/`, {
            headers: { 'Authorization': `Token ${authToken}` }
        });
        
        if (response.ok) {
            const data = await response.json();
            renderTasks(data.results);
        }
    } catch (error) {
        showAlert('Error loading tasks', 'error');
    }
}

// Bad - Unclear and outdated
function loadTasks(){fetch(API_BASE_URL+'/tasks/',{headers:{'Authorization':'Token '+authToken}}).then(function(r){return r.json()}).then(function(d){renderTasks(d.results)})}
```

### Writing Tests

**Always write tests for:**
- New features
- Bug fixes
- API endpoints
- Model methods

```python
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class TaskAPITest(TestCase):
    """Test Task API endpoints."""
    
    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
    
    def test_create_task(self):
        """Test creating a new task."""
        data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'completed': False
        }
        response = self.client.post('/api/tasks/', data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Task')
    
    def tearDown(self):
        """Clean up after tests."""
        pass
```

## 📌 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Code style changes (formatting, no logic change)
- `refactor` - Code refactoring
- `test` - Adding or updating tests
- `chore` - Maintenance tasks

**Examples:**

```bash
# Good commits
git commit -m "feat(tasks): add category field to Task model"
git commit -m "fix(auth): fix token validation bug"
git commit -m "docs(readme): update installation instructions"
git commit -m "test(tasks): add tests for task filtering"

# Bad commits
git commit -m "fixed stuff"
git commit -m "update"
git commit -m "changes"
```

**Detailed commit example:**
```
feat(tasks): add task priority levels

Add high, medium, and low priority options for tasks.
Users can now set priority when creating/updating tasks.
Frontend displays priority badge with appropriate colors.

Closes #42
```

## 🔄 Pull Request Process

### Before Submitting

1. **Update from upstream:**
```bash
git fetch upstream
git rebase upstream/main
```

2. **Run tests:**
```bash
python manage.py test
```

3. **Check code style:**
```bash
# If using flake8
flake8 .
```

4. **Update documentation** if needed

### Creating Pull Request

1. **Push your branch:**
```bash
git push origin feature/your-feature-name
```

2. **Create PR on GitHub:**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Fill in the PR template

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] All tests pass
- [ ] Added new tests
- [ ] Tested manually

## Screenshots (if applicable)
Add screenshots for UI changes

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Tests added/updated
```

### After Submitting

- Respond to review comments promptly
- Make requested changes
- Keep PR up to date with main branch
- Be patient and respectful

## 🔍 Code Review Process

### For Reviewers

**What to check:**
- Code quality and style
- Test coverage
- Documentation updates
- Security implications
- Performance impact

**How to review:**
- Be constructive and kind
- Explain reasoning
- Suggest improvements
- Approve when ready

### For Contributors

**Responding to reviews:**
- Thank reviewers
- Address all comments
- Ask for clarification if needed
- Update PR as requested

## 🎯 Areas for Contribution

### Easy (Good First Issues)
- Fix typos in documentation
- Add code comments
- Improve error messages
- Add unit tests
- Update dependencies

### Medium
- Add filtering options
- Improve UI/UX
- Add validation
- Optimize queries
- Add API documentation

### Advanced
- Add task categories
- Implement due dates
- Add file attachments
- Implement notifications
- Add task sharing

## 📚 Resources

**Django:**
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Best Practices](https://django-best-practices.readthedocs.io/)

**Python:**
- [PEP 8 Style Guide](https://pep8.org/)
- [Python Documentation](https://docs.python.org/)

**Git:**
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)

**Testing:**
- [Django Testing](https://docs.djangoproject.com/en/stable/topics/testing/)
- [pytest-django](https://pytest-django.readthedocs.io/)

## ❓ Questions?

- **General questions:** Open a [Discussion](https://github.com/Pradhyumn1/task_manager/discussions)
- **Bug reports:** Create an [Issue](https://github.com/Pradhyumn1/task_manager/issues)
- **Feature requests:** Create an [Issue](https://github.com/Pradhyumn1/task_manager/issues)

## 🙏 Thank You!

Your contributions help make TaskFlow better for everyone. Whether it's:
- Reporting a bug
- Suggesting a feature
- Improving documentation
- Submitting code

**Every contribution is valued and appreciated!** 🌟

---

**Happy Contributing! 🚀**

*For more information, see:*
- [README.md](README.md) - Project overview
- [COMMANDS.md](COMMANDS.md) - Command reference
- [FRONTEND.md](FRONTEND.md) - Frontend documentation
