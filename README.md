in-django
A Django-based blog application featuring user authentication, post management, and REST API endpoints.

Features
User registration and authentication
Create, edit, and delete blog posts
Publish/unpublish posts
REST API for posts
Debug toolbar for development
Responsive templates
Setup
Install dependencies:
pip install django djangorestframework django-debug-toolbar
Run migrations:
python manage.py migrate
Create superuser:
python manage.py createsuperuser
Start server:
python manage.py runserver
Usage
Web interface: Access at http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/
API endpoints:
GET /api/posts/ - List published posts
POST /api/posts/ - Create post (authenticated)
GET /api/posts/{id}/ - Get specific post
Tech Stack
Django 6.0.4
Django REST Framework
SQLite (default database)
HTML/CSS templates
Development
Debug mode enabled
Logging configured to debug.log
Debug toolbar available for internal IPs
