# Django TODO App

## Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Django

```bash
pip install django
```

### 3. Verify Django Installation

```bash
python -m django --version
```

Agar version number aa jaye, toh Django install hai.

---

## Project Structure

```
todo-django-app/           # (root folder, naam kuch bhi ho sakta)
│
├── venv/                  # Virtual environment folder (auto)
│
├── backend/               # Django project folder (auto)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── todo/                  # TODO app
│   ├── migrations/        # Migration files (auto)
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   ├── urls.py            # Khud banana hai, by default nahi aata
│   └── templates/
│       └── todo/
│           └── index.html # HTML frontend
│
├── db.sqlite3             # Default DB file (auto banega)
├── manage.py              # Django ka main command file
└── requirements.txt       # (optional) Packages ka list
```

---

## Django Architecture (MVC vs MTV)

### 1. Model (M)

**File:** `todo/models.py`  
**Explanation:**  
Yahan par data structure define hota hai (jaise `Todo` class).  
Database se interact karta hai (save/fetch/update).

### 2. View (V)

**File:** `todo/views.py`  
**Explanation:**  
Yahan functions/classes likhte ho jo request lete hain,  
database se data nikalte hain (Model use karte hain),  
aur Template ko data dete hain.

### 3. Template (T)

**File:** `todo/templates/todo/index.html`  
**Explanation:**  
Yahan HTML/CSS hota hai, jo user ko dikhaya jata hai.

---

### Django MTV vs Traditional MVC

- **Model:** Data structure (same in both)
- **Template:** User interface (MVC ka "View")
- **View:** Logic handler (MVC ka "Controller")

Django me "View" = MVC ka "Controller"  
Django me "Template" = MVC ka "View"

---

## Common Commands

- **Make Migrations:**
  ```bash
  python manage.py makemigrations
  ```
- **Apply Migrations:**
  ```bash
  python manage.py migrate
  ```
- **Run Server:**
  ```bash
  python manage.py runserver
  ```

---

## Notes

- `complete` aur `delete` actions ke baad page reload hota hai kyunki view me `redirect('/')` use hota hai.
- `.gitignore` file zaroor add karein taaki unnecessary files git me na jayein.
