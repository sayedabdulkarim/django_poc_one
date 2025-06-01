Arey bhai, seedha seedha bata deta hoon step by step, tension nahi lene ka!
Django backend, frontend HTML/CSS/JS — full basic TODO app banaenge.

---

## **Step 1: Project setup — Virtual Environment**

```bash
# 1. Make project folder and cd into it
mkdir todo-django-app
cd todo-django-app

# 2. Create virtual environment (use any name, e.g., venv)
python3 -m venv venv

# 3. Activate virtual env
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate

# 4. Install Django
pip install django
```

---

## **Step 2: Django Project and App Banana**

```bash
# 5. Start Django project
django-admin startproject backend .

# 6. Start TODO app inside project
python manage.py startapp todo
```

---

## **Step 3: Add App in settings**

- Open `backend/settings.py`
- Add `'todo',` in `INSTALLED_APPS` list.

---

## **Step 4: Model Banana (TODO model)**

In `todo/models.py`:

```python
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

---

## **Step 5: Migrate kar, admin banana**

```bash
python manage.py makemigrations (models ke changes ko migration files me convert karta hai)
python manage.py migrate (migration files ko apply karke database ko update karta hai)
python manage.py createsuperuser
# Follow prompts, set username/password
```

---

## **Step 6: Admin Panel Setup**

In `todo/admin.py`:

```python
from .models import Todo
from django.contrib import admin

admin.site.register(Todo)
```

---

## **Step 7: Backend Views aur URLs (basic CRUD)**

In `todo/views.py`:

```python
from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
        return redirect('/')
    return render(request, 'todo/index.html', {'todos': todos})

def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('/')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')
```

---

## **Step 8: URLs bana**

In `todo/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:todo_id>/', views.complete, name='complete'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
```

In `backend/urls.py`, edit:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),   # Add this line
]
```

---

## **Step 9: Frontend — HTML/CSS/JS**

- Make a folder: `todo/templates/todo/`
- Create `index.html` inside it.

Example: `todo/templates/todo/index.html`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>TODO App</title>
    <style>
      /* Your CSS here, e.g., */
      body {
        font-family: Arial;
        background: #111;
        color: #eee;
      }
      .todo {
        margin: 10px 0;
      }
      .completed {
        text-decoration: line-through;
        color: #888;
      }
    </style>
  </head>
  <body>
    <h1>TODO List</h1>
    <form method="POST">
      {% csrf_token %}
      <input type="text" name="title" placeholder="Add new todo" required />
      <button type="submit">Add</button>
    </form>
    <ul>
      {% for todo in todos %}
      <li class="todo {% if todo.completed %}completed{% endif %}">
        {{ todo.title }} {% if not todo.completed %}
        <a href="{% url 'complete' todo.id %}">[Complete]</a>
        {% endif %}
        <a href="{% url 'delete' todo.id %}">[Delete]</a>
      </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

---

## **Step 10: Run the server**

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) — bhai, aapka TODO app ready hai!

---
