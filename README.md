# Django:
**Django** is a high-level, open-source Python web framework that enables rapid development of secure and maintainable websites. It follows the **Model-View-Template (MVT)** architectural pattern. Django includes built-in features like an admin panel, user authentication, URL routing, and ORM for database operations. It promotes **"Don't Repeat Yourself" (DRY)** and **"Convention over Configuration"** principles. Django is ideal for building everything from simple websites to complex web applications quickly and efficiently.



# Django Project File Structure:
* **Build Project:**
    ```cmd
        django-admin startproject myproject
        cd myproject
    ```
    * **You will see something like this:**
        ```txt
            myproject/
                ├── manage.py
                ├── myproject/
                │   ├── __init__.py
                │   ├── asgi.py
                │   ├── settings.py
                │   ├── urls.py
                │   └── wsgi.py
        ```
    Absolutely! Let’s break down the **Django project file structure** with folder/file names and simple explanations. When you create a new Django project using:

### 🔍 Top-Level Overview

#### ✅ `manage.py`

* A command-line utility to interact with your project.
* Use it to run the server, create apps, run migrations, etc.
* Example: `python manage.py runserver`


### 🔍 Inner `myproject/` Directory

This is the actual **project package** (same name as your outer folder).

#### ✅ `__init__.py`

* Makes the directory a Python package.
* Usually empty, but required for Python to recognize it as a module.

#### ✅ `settings.py`

* Core configuration file for your Django project.
* Defines installed apps, middleware, templates, databases, static files, etc.

#### ✅ `urls.py`

* The central URL configuration.
* Routes URLs to views across the project.
* You can include app-specific URLs here too.

#### ✅ `wsgi.py`

* Entry point for WSGI-compatible web servers (like Gunicorn, uWSGI).
* Used for deployment.

#### ✅ `asgi.py`

* Similar to `wsgi.py`, but for ASGI servers (support async features, like WebSockets).
* Required for Django Channels or newer async features.

---

### 🧱 After Creating an App (`python manage.py startapp myapp`)

Your structure becomes:

```
myproject/
├── manage.py
├── myproject/
│   └── ...
├── myapp/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── __init__.py
│   ├── migrations/
│   │   └── __init__.py
```

#### ✅ `admin.py`

* Register your models here to manage them via Django Admin UI.

#### ✅ `apps.py`

* App-specific configuration.
* Used when customizing app behavior.

#### ✅ `models.py`

* Define your database models here.
* Each model maps to a table in the database.

#### ✅ `views.py`

* Business logic lives here.
* Each function or class maps to a web page or action.

#### ✅ `tests.py`

* Write unit tests for your app logic here.

#### ✅ `migrations/`

* Auto-generated files that track changes in models and apply them to the DB.
* Created using `makemigrations` and `migrate` commands.


### 📁 Common Additional Folders (You’ll often create these)

* `templates/` — Store HTML files
* `static/` — CSS, JS, and image files
* `forms.py` — If you're building forms manually
* `urls.py` — App-level routing (included in the main project’s `urls.py`)

### 📁 Why we need these Django App (`myapp`) File Sstructure:

#### ✅ `admin.py` – *Connect Models to Admin Panel*

* Purpose: Lets you **register models** so they appear in Django’s **built-in admin interface**.
* Why it's needed:

  * You can view, add, edit, and delete database records easily.
  * Helps with **internal/admin dashboards** without writing extra views.
* Example:

  ```python
  from django.contrib import admin
  from .models import Post

  admin.site.register(Post)
  ```

---

#### ✅ `apps.py` – *App Configuration File*

* Purpose: Stores **metadata about the app**, such as name and configuration.
* Why it's needed:

  * Django uses it to **recognize your app** and load it correctly.
  * You can override default settings, signals, or app labels here.
* Example:

  ```python
  class BlogConfig(AppConfig):
      name = 'blog'
  ```

---

#### ✅ `models.py` – *Data Schema Definition*

* Purpose: Define your **data structure** using Python classes.
* Why it's needed:

  * Each model maps to a **database table** using Django’s **ORM**.
  * Simplifies database operations without writing raw SQL.
* Example:

  ```python
  class Post(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
  ```

---

#### ✅ `views.py` – *Business Logic & Request Handling*

* Purpose: Define **how data is fetched, processed, and passed to templates**.
* Why it's needed:

  * Acts as the **bridge between models and templates**.
  * Each view handles an HTTP request and returns a response.
* Example:

  ```python
  def post_list(request):
      posts = Post.objects.all()
      return render(request, 'post_list.html', {'posts': posts})
  ```

#### ✅ `tests.py` – *Write Tests for App Functionality*

* Purpose: Contains **unit and functional tests** for your app.
* Why it's needed:

  * Ensures your code works correctly after changes.
  * Helps maintain **reliable and bug-free** applications.
* Example:

  ```python
  from django.test import TestCase

  class SimpleTest(TestCase):
      def test_addition(self):
          self.assertEqual(1 + 1, 2)
  ```

---

#### ✅ `migrations/` – *Track & Apply Database Changes*
**Migration in Django** is the process of propagating changes made to your models (Python classes) into the database schema. Django tracks these changes using special migration files stored in the `migrations/` folder. You create migration files using `python manage.py makemigrations` and apply them to the database using `python manage.py migrate`. This ensures your database structure stays in sync with your model definitions over time.<br>

* Purpose: Stores auto-generated files that represent **schema changes**.
* Why it's needed:

  * Allows Django to manage database evolution (creating/updating tables).
  * Required for `makemigrations` and `migrate` to sync models with DB.
* Files look like:

  ```
  0001_initial.py
  0002_auto_add_field.py
  ```


Together, these files help Django apps stay **modular, scalable, and maintainable**. Each one has a specific role in the development cycle—data handling, logic, testing, or admin interface.




## 🧠 **How Django Works – Step-by-Step Flow**

#### ✅ 1. **User Sends a Request**

* A user opens a website and types a URL or clicks a link.
* The **HTTP request** is sent to the Django server.

---

#### ✅ 2. **URL Dispatcher (urls.py)**

* Django checks the requested URL against the patterns defined in `urls.py`.
* It finds the corresponding **view function** to handle the request.

```python
urlpatterns = [
    path('blog/', views.blog_list),
]
```

---

#### ✅ 3. **View Function (views.py)**

* The matched view function is executed.
* It contains the **business logic**: fetches data from the database (via models), processes it, and chooses which template to render.

```python
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})
```

---

#### ✅ 4. **Model Layer (models.py)**

* If the view needs to read/write data, it interacts with the **Model**.
* Django ORM converts model queries into SQL and communicates with the database.

---

#### ✅ 5. **Template Rendering (templates/)**

* The view sends data to the **template** (HTML file).
* Django Template Engine fills in dynamic content and returns the final HTML page.

---

#### ✅ 6. **HTTP Response**

* The rendered HTML is sent back to the user's browser as an **HTTP response**.

---

### 🔄 Summary Diagram (Text-based):

```
Browser (Request)
      ↓
URL Dispatcher (urls.py)
      ↓
View (views.py)
      ↓
Model (models.py, ORM, DB)
      ↓
Template (HTML)
      ↓
Browser (Response)
```

---

This cycle runs for every request the user makes, and Django handles it efficiently using its **MVT architecture**.



## 🧩 What is Jinja2 Template in Django?

Django uses its own template engine that is **very similar to Jinja2**, inspired by it. Jinja2 is a modern and designer-friendly templating language used to generate dynamic HTML pages.

In Django, **templates** help separate the presentation layer (HTML/CSS) from the business logic (views and models).


### ✅ Basic Syntax of Django (Jinja2-like) Templates

| Purpose      | Syntax                                  |            |
| ------------ | --------------------------------------- | ---------- |
| Variable     | `{{ variable_name }}`                   |            |
| If condition | `{% if condition %}...{% endif %}`      |            |
| For loop     | `{% for item in list %}...{% endfor %}` |            |
| Comments     | `{# This is a comment #}`               |            |
| Filters      | \`{{ name                               | upper }}\` |


## 🏗️ Template Inheritance in Django (Core Concept)

Template inheritance helps you **reuse a base layout** (like navbar, footer, etc.) across multiple pages without repeating code.


### 🔷 Step-by-Step Example:

#### 1. **Create a Base Template – `base.html`**

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        <h1>My Blog</h1>
        <nav>Home | About | Contact</nav>
    </header>

    <main>
        {% block content %}
        <!-- Default content -->
        {% endblock %}
    </main>

    <footer>
        <p>© 2025 My Blog</p>
    </footer>
</body>
</html>
```

#### 2. **Extend Base in a Child Template – `home.html`**

```html
<!-- templates/home.html -->
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
    <h2>Welcome to my blog!</h2>
    <p>This is the homepage content.</p>
{% endblock %}
```


### 🔁 How it Works:

* `{% extends "base.html" %}` tells Django to inherit the structure from `base.html`.
* `{% block title %}` and `{% block content %}` override the respective blocks from the base template.

---

### 🧠 Benefits of Template Inheritance

* **Avoid code duplication** (DRY principle)
* **Easier maintenance**
* Consistent layout across pages
* Add new pages with minimal HTML



### ✅ How to Use in `views.py`:

```python
def home(request):
    return render(request, 'home.html')
```


### Summary

| Term                   | Meaning                              |
| ---------------------- | ------------------------------------ |
| `{{ ... }}`            | Output a variable                    |
| `{% ... %}`            | Template logic (control structures)  |
| `{% block name %}`     | Define overridable content           |
| `{% extends "file" %}` | Inherit layout from another template |

