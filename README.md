# 📝 TaskFlow - To-Do List Application

A beautiful, modern full-stack To-Do application with Django REST Framework backend and stunning glassmorphism frontend. Features complete authentication, CRUD operations, real-time search, filtering, and comprehensive testing.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14+-red.svg)
![Tests](https://img.shields.io/badge/tests-25%20passed-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- ✅ **Full CRUD Operations** - Create, Read, Update, Delete tasks
- 🎨 **Beautiful Glassmorphism UI** - Modern frosted glass design with smooth animations
- 🔐 **User Authentication** - Secure token-based authentication
- 🔒 **User-Specific Tasks** - Complete data isolation between users
- 🔍 **Advanced Filtering** - Filter by completion status (All/Active/Completed)
- 🔎 **Real-time Search** - Instant search across task titles and descriptions
- 📊 **Live Statistics** - Dashboard showing total, active, and completed tasks
- 📱 **Fully Responsive** - Beautiful on desktop, tablet, and mobile
- 🧪 **Comprehensive Testing** - 25 unit tests with 100% pass rate
- 📖 **Browsable API** - Django REST Framework's interactive API explorer

## 🛠️ Tech Stack

**Backend:**
- Django 4.2+ - Python web framework
- Django REST Framework 3.14+ - RESTful API toolkit
- SQLite (development) / PostgreSQL (production)
- Token-based authentication

**Frontend:**
- HTML5 - Semantic structure
- CSS3 - Modern styling with glassmorphism effects
- Vanilla JavaScript - No frameworks, pure JS
- Google Fonts (Inter) - Clean typography

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Pradhyumn1/task_manager.git
cd task_manager
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and update SECRET_KEY if needed
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Access the application**
- **Frontend UI:** http://127.0.0.1:8000
- **API Root:** http://127.0.0.1:8000/api/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## 🎨 Using the Frontend

### Beautiful Web Interface

Visit **http://127.0.0.1:8000** to access the stunning glassmorphism UI.

**Features:**
- 🎨 Modern dark theme with gradient backgrounds
- ✨ Smooth animations and micro-interactions
- 📊 Real-time statistics dashboard
- 🔍 Instant search functionality
- 🎯 Smart task filtering

**Getting Started:**
1. **Register** a new account or **Login**
2. View your personalized **dashboard** with stats
3. **Add tasks** using the form on the left
4. **Manage tasks**: mark complete, search, filter, delete
5. **Logout** when done

See [FRONTEND.md](FRONTEND.md) for detailed frontend documentation.

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/auth/register/` | Register new user | No |
| POST | `/api/auth/login/` | Login and get token | No |
| POST | `/api/auth/logout/` | Logout user | Yes |
| GET | `/api/auth/profile/` | Get user profile | Yes |

### Task Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/tasks/` | List all user's tasks | Yes |
| POST | `/api/tasks/` | Create new task | Yes |
| GET | `/api/tasks/{id}/` | Get specific task | Yes |
| PUT | `/api/tasks/{id}/` | Update task (full) | Yes |
| PATCH | `/api/tasks/{id}/` | Update task (partial) | Yes |
| DELETE | `/api/tasks/{id}/` | Delete task | Yes |

### Filtering & Search

```bash
# Filter by completion status
GET /api/tasks/?completed=true
GET /api/tasks/?completed=false

# Search tasks
GET /api/tasks/?search=keyword

# Order tasks
GET /api/tasks/?ordering=-created_at
```

## 🧪 API Usage Examples

### 1. Register a User
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepass123",
    "password2": "securepass123"
  }'
```

### 2. Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepass123"
  }'
```

**Response:**
```json
{
  "token": "a1b2c3d4...",
  "user_id": 1,
  "username": "johndoe",
  "email": "john@example.com"
}
```

### 3. Create a Task
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{
    "title": "Complete Django Tutorial",
    "description": "Build a To-Do API",
    "completed": false
  }'
```

### 4. List All Tasks
```bash
curl -X GET http://127.0.0.1:8000/api/tasks/ \
  -H "Authorization: Token YOUR_TOKEN"
```

### 5. Update a Task
```bash
curl -X PATCH http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN" \
  -d '{"completed": true}'
```

### 6. Delete a Task
```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/ \
  -H "Authorization: Token YOUR_TOKEN"
```

## 🧪 Running Tests

Run the comprehensive test suite:

```bash
# Run all tests
python manage.py test

# Run with verbosity
python manage.py test -v 2

# Run specific app tests
python manage.py test tasks
python manage.py test authentication
```

**Test Coverage:** 25 tests covering:
- Task CRUD operations
- User authentication flow
- Permission enforcement
- Input validation
- Filtering and search
- User data isolation

## 📁 Project Structure

```
task_manager/
├── todo_project/           # Django project settings
│   ├── settings.py        # Configuration
│   ├── urls.py            # URL routing
│   └── views.py           # Frontend view
├── tasks/                  # Tasks app
│   ├── models.py          # Task model
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py            # Task URLs
│   ├── admin.py           # Admin config
│   └── tests.py           # Task tests
├── authentication/         # Authentication app
│   ├── serializers.py     # Auth serializers
│   ├── views.py           # Auth views
│   ├── urls.py            # Auth URLs
│   └── tests.py           # Auth tests
├── templates/             # HTML templates
│   └── index.html         # Main frontend
├── static/                # Static files
│   ├── css/
│   │   └── styles.css     # Glassmorphism styles
│   └── js/
│       └── app.js         # Frontend logic
├── manage.py              # Django CLI
├── requirements.txt       # Dependencies
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
└── README.md             # This file
```

## 🚀 Deployment

### Deploy to Railway (Free & Easy)

1. **Create Railway Account**
   - Visit https://railway.app
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose "task_manager"

3. **Add Environment Variables**
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-railway-domain.railway.app
   ```

4. **Deploy!**
   - Railway automatically detects Django and deploys

### Deploy to Heroku

1. **Install Heroku CLI**
```bash
brew tap heroku/brew && brew install heroku  # macOS
```

2. **Create Procfile**
```
web: gunicorn todo_project.wsgi:application --log-file -
```

3. **Add to requirements.txt**
```
gunicorn>=21.2.0
```

4. **Deploy**
```bash
heroku login
heroku create your-app-name
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
git push heroku main
```

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Generate strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use PostgreSQL database
- [ ] Set up static files with WhiteNoise
- [ ] Enable HTTPS
- [ ] Regular backups

## 🎨 Customization

### Change UI Colors

Edit `static/css/styles.css`:

```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --dark-bg: #0f0f1e;
    /* Customize other colors */
}
```

### Modify API Behavior

Edit settings in `todo_project/settings.py`:

```python
REST_FRAMEWORK = {
    'PAGE_SIZE': 20,  # Change pagination
    # Other settings...
}
```

## 🛠️ Development Tools

### Useful Commands

See [COMMANDS.md](COMMANDS.md) for a complete reference.

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic
```

### API Testing

**Using Postman:**
1. Import `postman_collection.json`
2. Set `baseUrl` to `http://127.0.0.1:8000`
3. Test all endpoints

**Using Demo Script:**
```bash
python api_demo.py
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [RESTful API Design](https://restfulapi.net/)

## 📊 Project Statistics

- **Total Files:** 45
- **Backend (Python):** ~2,000 lines
- **Frontend (HTML/CSS/JS):** ~1,200 lines
- **Tests:** 25 (100% passing)
- **API Endpoints:** 10
- **Documentation:** Comprehensive

## 🌟 Features Showcase

### Backend API
- ✅ RESTful design principles
- ✅ Token authentication
- ✅ User data isolation
- ✅ Input validation
- ✅ Error handling
- ✅ Pagination
- ✅ Filtering & search

### Frontend UI
- ✅ Glassmorphism design
- ✅ Responsive layout
- ✅ Smooth animations
- ✅ Real-time updates
- ✅ Clean UX
- ✅ Cross-browser compatible

## 👨‍💻 Author

**Pradhyumn Yadav**
- GitHub: [@Pradhyumn1](https://github.com/Pradhyumn1)
- Repository: [task_manager](https://github.com/Pradhyumn1/task_manager)

## 🙏 Acknowledgments

- Django & DRF communities
- Modern web design inspiration
- Open source contributors

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/Pradhyumn1/task_manager/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Pradhyumn1/task_manager/discussions)

---

## 🎉 Get Started Now!

```bash
git clone https://github.com/Pradhyumn1/task_manager.git
cd task_manager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Then visit:** http://127.0.0.1:8000

---

**Built with ❤️ using Django, DRF, and modern web technologies**

**⭐ Star this repo if you found it helpful!**
