
# 1. Student Management API using Django REST Framework

## 2. Project Overview

This project provides a RESTful API to manage student data with the following fields:

- ID
- Full Name
- Address
- Course
- Email ID
- Contact Number
- Parent Name
- Parent Contact Number

The API supports these operations:
- Add a new student (POST)
- List all students (GET)
- Update a student (PUT)
- Delete a student (DELETE)
- Soft delete a student (PUT)

---

## 3. Table of Contents

- [4. Prerequisites](#4-prerequisites)  
- [5. Setup & Installation](#5-setup--installation)  
- [6. Creating the APIs](#6-creating-the-apis)  
- [7. Running the Project](#7-running-the-project)  
- [8. Testing APIs Using Postman](#8-testing-apis-using-postman)  
- [9. Project Structure](#9-project-structure)  
- [10. Additional Notes](#10-additional-notes)  

---

## 4. Prerequisites

- Python 3.8+ installed (download: https://www.python.org/downloads/)  
- Git installed and configured (https://git-scm.com/downloads)  
- Basic command-line knowledge  
- Optional: Postman app for API testing (https://www.postman.com/downloads/)  

---

## 5. Setup & Installation

### 5.1 Clone your repository (or create a new project folder)

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
````

If starting fresh, create a folder and navigate into it:

```bash
mkdir Student_API
cd Student_API
```

---

### 5.2 Create and activate a Python virtual environment

```bash
python -m venv venv
```

* On Windows:

```bash
venv\Scripts\activate
```

* On macOS/Linux:

```bash
source venv/bin/activate
```

---

### 5.3 Install Django and Django REST Framework

```bash
pip install django djangorestframework
```

---

### 5.4 Start a new Django project and app

```bash
django-admin startproject student_project .
python manage.py startapp student_api
```

---

## 6. Creating the APIs

### 6.1 Define the Student model

In `student_api/models.py`, add:

```python
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    course = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    parent_name = models.CharField(max_length=100)
    parent_contact_number = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
```

---

### 6.2 Create serializers

Create `student_api/serializers.py`:

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

---

### 6.3 Create views with Django REST Framework viewsets

In `student_api/views.py`:

```python
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.filter(is_deleted=False)
    serializer_class = StudentSerializer

    def destroy(self, request, *args, **kwargs):
        # Override delete to perform soft delete
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

---

### 6.4 Configure URLs

In `student_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from student_api.views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
```

---

### 6.5 Update `settings.py`

Add `'rest_framework'` and `'student_api'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'student_api',
]
```

---

### 6.6 Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Your API will be accessible at `http://127.0.0.1:8000/api/students/`

---

## 8. Testing APIs Using Postman

You can use Postman to test the APIs. You have a Postman collection (import it by):

* Open Postman.
* Click **Import**.
* Select your provided Postman collection JSON file.
* Use the collection to test all CRUD operations:

| API Operation   | HTTP Method | URL                                                                                  |
| --------------- | ----------- | ------------------------------------------------------------------------------------ |
| Add new student | POST        | [http://127.0.0.1:8000/api/students/](http://127.0.0.1:8000/api/students/)           |
| List students   | GET         | [http://127.0.0.1:8000/api/students/](http://127.0.0.1:8000/api/students/)           |
| Update student  | PUT         | [http://127.0.0.1:8000/api/students/{id}/](http://127.0.0.1:8000/api/students/{id}/) |
| Delete student  | DELETE      | [http://127.0.0.1:8000/api/students/{id}/](http://127.0.0.1:8000/api/students/{id}/) |
| Soft delete     | DELETE      | (Implemented as DELETE in this project; alternatively handled in `destroy` method)   |

---

## 9. Project Structure

```
Student_API/
├── student_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── student_api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── requirements.txt (optional)
└── README.md
```

---

## 10. Additional Notes

* **Soft delete** is implemented by marking `is_deleted=True` and filtering out such students from the API response.
* You can extend authentication and permissions as needed.
* Consider adding pagination for large datasets.
* Keep your Personal Access Token (PAT) secure when pushing to GitHub.
* Always pull remote changes before pushing to avoid merge conflicts.

---

## Contact / Support

If you face any issues setting up or running the project, feel free to reach out.

---


