// create virtial environent
python3 -m venv venv
source venv/bin/activate

pip install django

TODO: how to test django is installed or not ?

## ASCII

todo-django-app/ # (root folder, naam kuch bhi ho sakta)
│
├── venv/ # Virtual environment folder (auto)
│
├── backend/ # Django project folder (auto)
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── todo/ # Ye hai tu ka TODO app
│ ├── migrations/ # Migration files (auto)
│ │ └── **init**.py
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── tests.py
│ ├── urls.py # Khud banana hai, by default nahi aata
│ └── templates/
│ └── todo/
│ └── index.html # Tera HTML frontend yahan
│
├── db.sqlite3 # Default DB file (auto banega)
├── manage.py # Django ka main command file
└── requirements.txt # (optional) Tere packages ka list

## MVC

---

1. Model (M):
   Code: todo/models.py

Explanation:
Yahan par sab data structure defined hota hai — jaise Todo class.
Database se interact karta hai, save/fetch/update ka kaam.

2. View (V):
   Django style: Ye confusing hai, kyunki Django ka "View" = Controller (logic handler)

Code: todo/views.py

Explanation:
Yahan functions/classes likhte ho jo request lete hain,
database se data nikalte hain (Model use karte hain),
aur Template ko data dete hain.

3. Controller (C):
   Django style: Yeh actually views.py hi controller hai

MVC vs MTV:

Django me "View" = MVC ka "Controller"

Django me "Template" = MVC ka "View"
