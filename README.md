# 📝 To-Do List API

A comprehensive RESTful API for managing tasks, built with Django and Django REST Framework. This project demonstrates essential backend development concepts including CRUD operations, user authentication, filtering, and API best practices.

## 🎯 Features

- ✅ **Full CRUD Operations** - Create, Read, Update, and Delete tasks
- 🔐 **User Authentication** - Token-based authentication with user registration
- 🔒 **User-Specific Tasks** - Users can only manage their own tasks
- 🔍 **Filtering** - Filter tasks by completion status
- 📊 **REST API** - Clean RESTful endpoints with proper HTTP methods
- 📖 **API Documentation** - Browsable API interface powered by DRF
- ✨ **Input Validation** - Comprehensive data validation and error handling

## 🛠️ Tech Stack

- **Backend Framework:** Django 4.2+
- **API Framework:** Django REST Framework 3.14+
- **Database:** SQLite (development) / PostgreSQL (production-ready)
- **Authentication:** Token-based authentication
- **Python:** 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd todo_django
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and update the SECRET_KEY
# You can generate a secret key using:
# python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and get auth token |
| POST | `/api/auth/logout/` | Logout and invalidate token |

### Tasks

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| GET | `/api/tasks/` | List all user's tasks | Required |
| POST | `/api/tasks/` | Create a new task | Required |
| GET | `/api/tasks/{id}/` | Get a specific task | Required |
| PUT | `/api/tasks/{id}/` | Update a task | Required |
| PATCH | `/api/tasks/{id}/` | Partially update a task | Required |
| DELETE | `/api/tasks/{id}/` | Delete a task | Required |

### Filtering

You can filter tasks by completion status:

```
GET /api/tasks/?completed=true   # Get completed tasks
GET /api/tasks/?completed=false  # Get incomplete tasks
```

## 🧪 API Usage Examples

### 1. Register a New User

```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

### 2. Login and Get Token

```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

Response:
```json
{
  "token": "a1b2c3d4e5f6...",
  "user_id": 1,
  "username": "johndoe"
}
```

### 3. Create a Task

```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token a1b2c3d4e5f6..." \
  -d '{
    "title": "Complete Django Tutorial",
    "description": "Finish building the To-Do API",
    "completed": false
  }'
```

### 4. List All Tasks

```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Token a1b2c3d4e5f6..."
```

### 5. Update a Task

```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token a1b2c3d4e5f6..." \
  -d '{
    "title": "Complete Django Tutorial",
    "description": "Finished!",
    "completed": true
  }'
```

### 6. Delete a Task

```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/ \
  -H "Authorization: Token a1b2c3d4e5f6..."
```

## 📂 Project Structure

```
todo_django/
├── todo_project/           # Django project settings
│   ├── settings.py        # Main settings file
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── tasks/                  # Tasks app
│   ├── models.py          # Task model definition
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # App URL routes
│   └── tests.py           # Unit tests
├── authentication/         # Authentication app
│   ├── views.py           # Auth views
│   ├── serializers.py     # Auth serializers
│   └── urls.py            # Auth URL routes
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md             # This file
```

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Run tests with coverage:

```bash
coverage run --source='.' manage.py test
coverage report
```

## 🧰 Using Postman

1. Import the Postman collection (if provided)
2. Set the `baseUrl` variable to `http://127.0.0.1:8000`
3. After login, set the `authToken` variable
4. Test all endpoints using the collection

## 🔧 Development Tips

### Browse the API

Django REST Framework provides a browsable API. Simply visit:
- `http://127.0.0.1:8000/api/` in your browser while the server is running

### Admin Interface

Access the Django admin at:
- `http://127.0.0.1:8000/admin/`
- Login with your superuser credentials

### Database

To reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 🚀 Deployment

### Environment Variables

For production, ensure you set:
- `SECRET_KEY` - A strong, random secret key
- `DEBUG=False`
- `ALLOWED_HOSTS` - Your domain names

### Database

Replace SQLite with PostgreSQL for production:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 📧 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/todo_django](https://github.com/yourusername/todo_django)

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [REST API Best Practices](https://restfulapi.net/)

---

**Happy Coding! 🚀**
