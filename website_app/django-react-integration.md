# 🔗 Integrating React with Django — Complete Guide

> A step-by-step guide to building a full-stack application using **Django** (backend REST API) and **React** (frontend SPA).

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Architecture](#project-architecture)
3. [Step 1 — Django Backend Setup](#step-1--django-backend-setup)
4. [Step 2 — Create Django App & Model](#step-2--create-django-app--model)
5. [Step 3 — Install Django REST Framework & CORS](#step-3--install-django-rest-framework--cors)
6. [Step 4 — Configure Settings](#step-4--configure-settings)
7. [Step 5 — Create Serializers](#step-5--create-serializers)
8. [Step 6 — Create API Views](#step-6--create-api-views)
9. [Step 7 — Configure URLs](#step-7--configure-urls)
10. [Step 8 — React Frontend Setup](#step-8--react-frontend-setup)
11. [Step 9 — Connect React to Django API](#step-9--connect-react-to-django-api)
12. [Step 10 — Run Both Servers](#step-10--run-both-servers)
13. [Project Structure](#project-structure)
14. [Tips & Best Practices](#tips--best-practices)

---

## ✅ Prerequisites

Make sure the following are installed on your machine:

| Tool | Version |
|------|---------|
| Python | 3.8+ |
| pip / pipenv | Latest |
| Node.js | 14+ |
| npm | 6+ |

---

## 🏗 Project Architecture

```
django-react-app/
├── backend/               ← Django project (REST API)
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── todo/              ← Django app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   └── manage.py
└── frontend/              ← React app (SPA)
    ├── src/
    │   ├── App.js
    │   └── components/
    └── package.json
```

**How it works:**
```
React (Port 3000)  ←──HTTP/Axios──→  Django REST API (Port 8000)
                                            ↓
                                       Database (SQLite/PostgreSQL)
```

---

## Step 1 — Django Backend Setup

### 1.1 Create Project Directory & Virtual Environment

```bash
# Create and navigate to project directory
mkdir django-react-app
cd django-react-app

# Install pipenv and create virtual environment
pip install pipenv
pipenv shell

# Install Django
pipenv install django
```

### 1.2 Create Django Project

```bash
# Create Django project named "backend"
django-admin startproject backend

# Navigate into the project
cd backend

# Run initial migrations
python manage.py migrate

# Verify the setup
python manage.py runserver
```

> 🟢 Visit `http://localhost:8000` — you should see the Django welcome page.

---

## Step 2 — Create Django App & Model

### 2.1 Create the App

```bash
python manage.py startapp todo
```

### 2.2 Register the App in `settings.py`

```python
# backend/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',   # ← Add your app here
]
```

### 2.3 Define the Model

```python
# todo/models.py
from django.db import models

class Todo(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    completed   = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

### 2.4 Run Migrations

```bash
python manage.py makemigrations todo
python manage.py migrate
```

---

## Step 3 — Install Django REST Framework & CORS

```bash
# Install Django REST Framework and CORS headers
pipenv install djangorestframework django-cors-headers

# Or using pip
pip install djangorestframework django-cors-headers
```

---

## Step 4 — Configure Settings

Open `backend/settings.py` and update the following:

```python
# backend/settings.py

INSTALLED_APPS = [
    # ... default apps ...
    'todo',
    'rest_framework',     # ← Django REST Framework
    'corsheaders',        # ← CORS Headers
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',    # ← Must be at the TOP
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ... rest of middleware ...
]

# Allow React's dev server to communicate with Django
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',   # ← React development server
]
```

---

## Step 5 — Create Serializers

Create a new file `todo/serializers.py`:

```python
# todo/serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Todo
        fields = ('id', 'title', 'description', 'completed')
```

> 📌 Serializers convert Django model instances into JSON format that React can consume.

---

## Step 6 — Create API Views

```python
# todo/views.py
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset         = Todo.objects.all()
```

> 🔥 `ModelViewSet` automatically provides `list`, `create`, `retrieve`, `update`, and `destroy` actions — full CRUD with just a few lines!

---

## Step 7 — Configure URLs

### 7.1 App-level URLs (`todo/urls.py`)

Create `todo/urls.py`:

```python
# todo/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TodoView, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
```

### 7.2 Project-level URLs (`backend/urls.py`)

```python
# backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),   # ← Mount API at /api/
]
```

### 7.3 Available API Endpoints

| Method | Endpoint | Action |
|--------|----------|--------|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/:id/` | Get a specific task |
| PUT | `/api/tasks/:id/` | Update a task |
| DELETE | `/api/tasks/:id/` | Delete a task |

---

## Step 8 — React Frontend Setup

### 8.1 Create React App (in a new terminal)

```bash
# From the root of your project (not inside /backend)
cd ..   # Go back to django-react-app/

# Create React app
npx create-vite@latest frontend

# Navigate into frontend
cd frontend
```

### 8.2 Install Dependencies

```bash
# Install Axios for HTTP requests
npm install axios

# Optional: Install Bootstrap for UI styling
npm install tailwindcss @tailwindcss/vite
```
---
```javascript
Open the vite.config.js (or vite.config.ts) file in your project's root directory. Import the tailwindcss plugin and add it to the plugins array.
javascript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite'; // Import the plugin

// https://vitejs.dev
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(), // Add the plugin here
  ],
});



```



### 8.3 Add Proxy to `package.json`

Open `frontend/package.json` and add the `proxy` field:

```json
{
  "name": "frontend",
  "version": "0.1.0",
  "proxy": "http://localhost:8000",
  ...
}
```

> ✅ This proxy tunnels all API requests from React (`localhost:3000`) to Django (`localhost:8000`), avoiding CORS issues in development.

---

## Step 9 — Connect React to Django API

### 9.1 Create a Component to Fetch Data

```jsx
// frontend/src/components/TodoList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TodoList() {
  const [tasks, setTasks]   = useState([]);
  const [title, setTitle]   = useState('');
  const [loading, setLoading] = useState(true);

  // ─── Fetch all tasks on mount ─────────────────────────────
  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const res = await axios.get('/api/tasks/');
      setTasks(res.data);
    } catch (err) {
      console.error('Error fetching tasks:', err);
    } finally {
      setLoading(false);
    }
  };

  // ─── Create a new task ────────────────────────────────────
  const createTask = async (e) => {
    e.preventDefault();
    if (!title.trim()) return;
    try {
      await axios.post('/api/tasks/', { title, completed: false });
      setTitle('');
      fetchTasks();   // Refresh the list
    } catch (err) {
      console.error('Error creating task:', err);
    }
  };

  // ─── Toggle task completion ───────────────────────────────
  const toggleTask = async (task) => {
    try {
      await axios.put(`/api/tasks/${task.id}/`, {
        ...task,
        completed: !task.completed,
      });
      fetchTasks();
    } catch (err) {
      console.error('Error updating task:', err);
    }
  };

  // ─── Delete a task ────────────────────────────────────────
  const deleteTask = async (id) => {
    try {
      await axios.delete(`/api/tasks/${id}/`);
      fetchTasks();
    } catch (err) {
      console.error('Error deleting task:', err);
    }
  };

  // ─── Render ───────────────────────────────────────────────
  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', fontFamily: 'Arial' }}>
      <h2>📝 Todo List</h2>

      {/* Create Task Form */}
      <form onSubmit={createTask} style={{ display: 'flex', gap: '8px', marginBottom: '20px' }}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Add a new task..."
          style={{ flex: 1, padding: '8px', fontSize: '16px' }}
        />
        <button type="submit" style={{ padding: '8px 16px' }}>Add</button>
      </form>

      {/* Task List */}
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {tasks.map((task) => (
          <li key={task.id} style={{
            display: 'flex', justifyContent: 'space-between',
            alignItems: 'center', padding: '10px',
            borderBottom: '1px solid #eee'
          }}>
            <span
              onClick={() => toggleTask(task)}
              style={{
                cursor: 'pointer',
                textDecoration: task.completed ? 'line-through' : 'none',
                color: task.completed ? '#aaa' : '#333',
              }}
            >
              {task.completed ? '✅' : '⬜'} {task.title}
            </span>
            <button
              onClick={() => deleteTask(task.id)}
              style={{ color: 'red', border: 'none', background: 'none', cursor: 'pointer' }}
            >
              🗑 Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
```

### 9.2 Update `App.js`

```jsx
// frontend/src/App.js
import React from 'react';
import TodoList from './components/TodoList';
import 'bootstrap/dist/css/bootstrap.min.css'; // Optional

function App() {
  return (
    <div className="App">
      <TodoList />
    </div>
  );
}

export default App;
```

---

## Step 10 — Run Both Servers

Open **two terminal windows**:

### Terminal 1 — Django Backend
```bash
cd django-react-app/backend
pipenv shell
python manage.py runserver
# ✅ Running at http://localhost:8000
```

### Terminal 2 — React Frontend
```bash
cd django-react-app/frontend
npm start
# ✅ Running at http://localhost:3000
```

> 🎉 Visit `http://localhost:3000` to see your full-stack Django + React application!

---

## 📁 Project Structure

```
django-react-app/
├── backend/
│   ├── backend/
│   │   ├── __init__.py
│   │   ├── settings.py       ← CORS + INSTALLED_APPS config
│   │   ├── urls.py           ← API routes
│   │   └── wsgi.py
│   ├── todo/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py         ← Database models
│   │   ├── serializers.py    ← JSON serializers
│   │   ├── views.py          ← API ViewSets
│   │   └── urls.py           ← App-level routes
│   ├── db.sqlite3
│   └── manage.py
└── frontend/
    ├── public/
    ├── src/
    │   ├── App.js            ← Root component
    │   └── components/
    │       └── TodoList.js   ← Main component
    ├── package.json          ← Proxy config
    └── node_modules/
```

---

## 💡 Tips & Best Practices

### 🔐 Authentication (JWT)
For production apps, add JWT authentication:
```bash
pip install djangorestframework-simplejwt
```
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

### 🌐 Environment Variables
Never hardcode URLs. Use environment variables:
```bash
# frontend/.env
REACT_APP_API_URL=http://localhost:8000/api
```
```jsx
// In React component
const res = await axios.get(`${process.env.REACT_APP_API_URL}/tasks/`);
```

### 🚀 Production Build
For deployment, build the React app and serve it via Django:
```bash
# Build React
cd frontend && npm run build

# Collect static files in Django
python manage.py collectstatic
```
```python
# backend/settings.py (production)
CORS_ORIGIN_WHITELIST = [
    'https://yourdomain.com',
]
```

### 📦 Package Manager Alternative
You can also use **Vite** instead of Create React App for a faster build:
```bash
npm create vite@latest frontend -- --template react
cd frontend && npm install
```

---

## 🔗 Resources

- [Django REST Framework Docs](https://www.django-rest-framework.org/)
- [React Official Docs](https://react.dev/)
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- [Axios HTTP Client](https://axios-http.com/)
- [GeeksForGeeks — Django + React](https://www.geeksforgeeks.org/reactjs/integrating-django-with-reactjs-using-django-rest-framework/)
- [DigitalOcean Tutorial](https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react)

---

> 📝 **Summary:** Django handles your data models, database, and REST API endpoints. React consumes those APIs to build a dynamic, interactive frontend. The two are connected via `django-cors-headers` on the backend and `axios` + a proxy configuration on the frontend.
