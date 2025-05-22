# Project Configurations (Initial Pahse):

## ✅ 1. **Django Project Setup**

### a. **Create Virtual Environment**

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

### b. **Install Django**

```bash
pip install django
```

### c. **Start Project and App**

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

### d. **Register App**

Add your app to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```



## ✅ 2. **Media Configuration in `settings.py`**

Media files are user-uploaded files (e.g., profile pictures, documents).

### a. Add the following lines to `settings.py`:

```python
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### b. Update `urls.py` (only in `project/urls.py`) to serve media files in development:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## ✅ 3. **Static Files Configuration**

Static files include CSS, JavaScript, and images used in the frontend.

### a. Add to `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # used for collectstatic

# OR:

# Setup Static Configuration: for css, js
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### b. In `project/urls.py`, during development:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

> Note: `STATICFILES_DIRS` is used to tell Django where to look for static files in development, and `STATIC_ROOT` is where all static files are collected for production using `python manage.py collectstatic`.


## ✅ 4. **Adding Templates**

### a. Create a `templates` directory in your project root:

```
/myproject/
    templates/
        home.html
```

### b. Configure `TEMPLATES` in `settings.py`:

```python
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

### c. Example usage in a view (`myapp/views.py`):

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```


## 🧪 Example Directory Structure:

```
myproject/
├── myapp/
├── media/
├── static/
│   └── css/
│   └── js/
├── templates/
│   └── home.html
├── myproject/
│   └── settings.py
│   └── urls.py
```


## ✅ Summary

| Configuration | File                        | Purpose                                                                    |
| ------------- | --------------------------- | -------------------------------------------------------------------------- |
| Media         | `settings.py`, `urls.py`    | Handle file uploads (like images, docs) via `MEDIA_URL` and `MEDIA_ROOT`   |
| Static        | `settings.py`, `urls.py`    | Handle frontend assets like CSS, JS using `STATIC_URL`, `STATICFILES_DIRS` |
| Templates     | `settings.py`, `templates/` | Render HTML views with Django template engine                              |


