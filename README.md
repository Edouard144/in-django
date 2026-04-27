# 📝 In-Django Blog Application

A modern **Django-based blog platform** featuring authentication, post management, and RESTful API support. Built for scalability, clean architecture, and developer-friendly debugging.

---

## 🚀 Features

* 🔐 User Registration & Authentication
* ✍️ Create, Edit, and Delete Blog Posts
* 📢 Publish / Unpublish Posts
* 🌐 REST API for Blog Content
* 🛠️ Debug Toolbar for Development
* 📱 Responsive UI Templates

---

## 🛠️ Tech Stack

* **Django 6.0.4**
* **Django REST Framework**
* **SQLite** (default database)
* **HTML / CSS Templates**

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/in-django.git
cd in-django
```

### 2. Install Dependencies

```bash
pip install django djangorestframework django-debug-toolbar
```

### 3. Apply Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

---

## 🌍 Usage

### Web Interface

* Home: http://127.0.0.1:8000/

### Admin Panel

* http://127.0.0.1:8000/admin/

### API Endpoints

| Method | Endpoint           | Description                             |
| ------ | ------------------ | --------------------------------------- |
| GET    | `/api/posts/`      | List all published posts                |
| POST   | `/api/posts/`      | Create a post (requires authentication) |
| GET    | `/api/posts/{id}/` | Retrieve a specific post                |

---

## 🧪 Development

* Debug mode enabled
* Logs stored in `debug.log`
* Django Debug Toolbar active for internal IPs

---

## 📂 Project Structure (Simplified)

```
in-django/
│── blog/
│── users/
│── templates/
│── static/
│── manage.py
```

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.


## 👨‍💻 Author

**Edouard Tuyubahe**
🔗 GitHub: https://github.com/Edouard144
