# Quick Start Guide

Get your To-Do List API up and running in 5 minutes! ⚡

## Prerequisites

- Python 3.8 or higher
- pip
- Git (for version control)

## Setup Steps

### 1. Clone or Download the Project

```bash
cd /Users/pradhyumnyadav/Desktop/todo_django
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
# A .env file has already been created for you
# For production, update the SECRET_KEY
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000`

### 8. Test the API

#### Option 1: Use the Demo Script
```bash
python api_demo.py
```

#### Option 2: Use the Browsable API
Open your browser and go to:
- `http://127.0.0.1:8000/api/tasks/`
- `http://127.0.0.1:8000/api/auth/register/`

#### Option 3: Use Postman
1. Import `postman_collection.json` into Postman
2. Set the `baseUrl` variable to `http://127.0.0.1:8000`
3. Start testing!

#### Option 4: Use cURL
```bash
# Register a user
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@test.com","password":"test123","password2":"test123"}'

# Login and get token
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"test123"}'

# Create a task (replace YOUR_TOKEN with the token from login)
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{"title":"My First Task","description":"Testing the API","completed":false}'
```

## What's Next?

### Run Tests
```bash
python manage.py test
```

### Access Admin Panel
```bash
# Go to http://127.0.0.1:8000/admin/
# Login with your superuser credentials
```

### Deploy to Production
See `DEPLOYMENT.md` for detailed deployment instructions.

### Push to GitHub
```bash
# Already initialized! Just add your remote:
git remote add origin https://github.com/YOUR_USERNAME/your-repo.git
git push -u origin main
```

## API Endpoints Reference

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register new user | No |
| POST | `/api/auth/login/` | Login user | No |
| POST | `/api/auth/logout/` | Logout user | Yes |
| GET | `/api/auth/profile/` | Get user profile | Yes |
| GET | `/api/tasks/` | List all tasks | Yes |
| POST | `/api/tasks/` | Create a task | Yes |
| GET | `/api/tasks/{id}/` | Get task details | Yes |
| PUT | `/api/tasks/{id}/` | Update task | Yes |
| PATCH | `/api/tasks/{id}/` | Partial update | Yes |
| DELETE | `/api/tasks/{id}/` | Delete task | Yes |

## Common Issues

### Port already in use
```bash
# Kill the process using port 8000
lsof -ti:8000 | xargs kill -9
# Or use a different port
python manage.py runserver 8001
```

### Migration errors
```bash
# Reset database
rm db.sqlite3
python manage.py migrate
```

## Need Help?

- Check the full `README.md` for detailed documentation
- Review `DEPLOYMENT.md` for deployment help
- See `CONTRIBUTING.md` to contribute to the project

---

**Happy coding! 🚀**
