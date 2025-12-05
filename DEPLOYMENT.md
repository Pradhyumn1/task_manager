# Deployment and GitHub Hosting Guide

This guide will help you deploy your To-Do List API and host it on GitHub.

## 📦 Hosting on GitHub

### 1. Initialize Git Repository

```bash
git init
```

### 2. Add All Files

```bash
git add .
```

### 3. Create Initial Commit

```bash
git commit -m "Initial commit: To-Do List API with Django REST Framework"
```

### 4. Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it `todo-list-api` or similar
3. **Don't** initialize with README (we already have one)
4. Copy the repository URL

### 5. Link Local Repository to GitHub

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/todo-list-api.git
git push -u origin main
```

## 🚀 Deployment Options

### Option 1: Railway.app (Recommended for Beginners)

Railway is free and easy to use for Django projects.

#### Steps:

1. **Create `railway.json`** (already included in project):
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && gunicorn todo_project.wsgi:application",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

2. **Update `requirements.txt`** to include production dependencies:
```
Django>=4.2.0,<5.0
djangorestframework>=3.14.0
django-filter>=23.0
django-cors-headers>=4.0
python-decouple>=3.8
gunicorn>=21.2.0
psycopg2-binary>=2.9.9
whitenoise>=6.6.0
```

3. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up/Login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your `todo-list-api` repository
   - Add environment variables:
     - `SECRET_KEY`: Generate a new secret key
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: Your Railway domain
   - Railway will automatically deploy!

### Option 2: Heroku

1. **Install Heroku CLI**:
```bash
brew tap heroku/brew && brew install heroku  # macOS
```

2. **Create `Procfile`**:
```
web: gunicorn todo_project.wsgi:application --log-file -
release: python manage.py migrate
```

3. **Deploy**:
```bash
heroku login
heroku create your-todo-api
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
git push heroku main
```

### Option 3: Render

1. Go to [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn todo_project.wsgi:application`
5. Add environment variables in Render dashboard
6. Deploy!

## 🔧 Production Configuration

### Update `settings.py` for Production

Add this to the end of `settings.py`:

```python
import os

# Production settings
if not DEBUG:
    # Security settings
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    
    # Static files
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    # Database (PostgreSQL)
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(
            default=config('DATABASE_URL', default='sqlite:///db.sqlite3')
        )
    }
```

### Update Middleware for WhiteNoise

In `settings.py`, add WhiteNoise middleware:

```python
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Add this
    "corsheaders.middleware.CorsMiddleware",
    # ... rest of middleware
]
```

## 📊 Database Migration

When deploying, ensure migrations run automatically:

```bash
python manage.py migrate
```

Most platforms run this automatically or can be configured to do so.

## 🔐 Environment Variables

**Never commit your `.env` file to GitHub!**

Essential environment variables for production:

- `SECRET_KEY`: Generate a strong, random secret key
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Your domain name(s)
- `DATABASE_URL`: Your database connection string (if using PostgreSQL)

### Generate a Strong Secret Key

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 📝 Post-Deployment Checklist

- [ ] All tests passing (`python manage.py test`)
- [ ] Migrations applied
- [ ] Static files collected
- [ ] Environment variables configured
- [ ] `DEBUG=False` in production
- [ ] Database backed up regularly
- [ ] HTTPS enabled
- [ ] Domain configured (optional)
- [ ] API documentation accessible

## 🔍 Testing Your Deployment

After deployment, test all endpoints:

```bash
# Replace YOUR_DOMAIN with your actual domain
curl https://YOUR_DOMAIN/api/auth/register/ -X POST \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@example.com","password":"testpass123","password2":"testpass123"}'
```

## 📚 Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [Railway Documentation](https://docs.railway.app/)
- [Heroku Django Guide](https://devcenter.heroku.com/articles/django-app-configuration)
- [DRF Production Guide](https://www.django-rest-framework.org/topics/deployment/)

## 🆘 Troubleshooting

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic` and ensure WhiteNoise is configured

### Issue: Database errors on deployment
**Solution**: Check that migrations ran successfully and DATABASE_URL is set correctly

### Issue: 500 Internal Server Error
**Solution**: Check logs, ensure DEBUG=False, and verify all environment variables are set

## 📧 Support

If you encounter issues, check the logs on your hosting platform or refer to their documentation.

---

**Good luck with your deployment! 🚀**
