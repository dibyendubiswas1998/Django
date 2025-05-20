## Django Rest Framework Learning Topics:

## 🔹 **1. JSON Serializable**

### ✅ What does JSON Serializable mean?

In Django (especially with APIs), **JSON Serializable** means that **data must be in a format that can be converted to JSON**. JSON (JavaScript Object Notation) is the most common data format used in REST APIs.

Only basic Python data types like `dict`, `list`, `str`, `int`, `float`, `bool`, and `None` are JSON serializable.

### ❌ Not JSON Serializable:

* Custom objects like Django `QuerySet` or `datetime` cannot be directly converted to JSON.

### ✅ Example:

```python
# ✅ JSON serializable
data = {
    "name": "John",
    "age": 30,
    "is_active": True
}

# ❌ Not directly serializable
from datetime import datetime
data = {
    "name": "John",
    "last_login": datetime.now()  # Not JSON serializable directly
}
```

### ✅ Fix:

You must convert such objects (like `datetime`) to string or use Django REST Framework’s **serializers** to make them JSON serializable.



## 🔹 **2. Function-Based Views (FBV)**

### ✅ What are Function-Based Views?

A **Function-Based View** is a traditional approach in Django where you define a view as a Python function. It’s simple and straightforward, ideal for small or beginner projects.

### ✅ Example:

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

### ✅ For APIs using Django REST Framework:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_data(request):
    return Response({"message": "Function-Based View API"})
```

### ✔️ When to use:

* Simple logic
* Clear separation of actions like `GET`, `POST`
* More readable for beginners



## 🔹 **3. Class-Based Views (CBV)**

### ✅ What are Class-Based Views?

**Class-Based Views** use Python classes and object-oriented principles to handle HTTP requests. Each HTTP method (`GET`, `POST`, etc.) is defined as a class method.

CBVs are **more reusable, modular, and DRY** (Don’t Repeat Yourself).

### ✅ Example:

```python
from django.http import HttpResponse
from django.views import View

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello from Class-Based View!")
```

### ✅ For APIs using Django REST Framework:

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class GetData(APIView):
    def get(self, request):
        return Response({"message": "Class-Based View API"})
```

### ✔️ When to use:

* Reusability is needed
* You’re building large, scalable applications
* Want to use Django mixins or generics



## 🔄 **4. FBV vs CBV – Comparison Table**

| Feature              | Function-Based View (FBV)     | Class-Based View (CBV)                             |
| -------------------- | ----------------------------- | -------------------------------------------------- |
| **Definition Style** | Defined as a function         | Defined as a class                                 |
| **Complexity**       | Simple and easy to understand | More abstract and OOP-based                        |
| **Flexibility**      | Great for simple logic        | Better for handling multiple request types cleanly |
| **Readability**      | Very readable for beginners   | Might be complex for new developers                |
| **Code Reusability** | Low                           | High (via inheritance and mixins)                  |
| **Best For**         | Small or medium-sized views   | Large applications or REST APIs                    |
| **Decorator Usage**  | Simple and direct             | Needs method decorators                            |
| **API Integration**  | `@api_view` (DRF)             | `APIView` or `GenericAPIView` (DRF)                |


Let’s walk through each of the listed advanced Django REST Framework (DRF) concepts **in detail with examples**. These are powerful tools that help you build RESTful APIs faster and more cleanly.



## 🔹 5. **Mixins in Django REST Framework**

Mixins are **reusable building blocks** provided by DRF to add specific behavior (like `list`, `create`, `retrieve`, etc.) to your views without repeating code.

You use Mixins by **combining them with `GenericAPIView`**.

### ✅ Available Mixins:

| Mixin                | Purpose                   |
| -------------------- | ------------------------- |
| `ListModelMixin`     | List all records          |
| `CreateModelMixin`   | Create a new record       |
| `RetrieveModelMixin` | Get a single record       |
| `UpdateModelMixin`   | Update an existing record |
| `DestroyModelMixin`  | Delete a record           |

### ✅ Example:

```python
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)  # Handles GET (List)

    def post(self, request):
        return self.create(request)  # Handles POST (Create)
```


## 🔹 6. **`GenericAPIView` (Base View)**

`GenericAPIView` is a **flexible base class** that provides common functionality (like setting `queryset`, `serializer_class`) and lets you plug in Mixins.

### ✅ Key HTTP Methods:

* `get()` → typically combined with `ListModelMixin` or `RetrieveModelMixin`
* `post()` → with `CreateModelMixin`
* `put()` → with `UpdateModelMixin`
* `delete()` → with `DestroyModelMixin`

### ✅ Example:

```python
class StudentDetailView(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)  # Handles GET for a specific item
```


## 🔹 7. **Generics Views (Shortcut Views)**

These are **pre-built views** that combine common Mixins + `GenericAPIView` in one class. You just write the class and it works!

### ✅ Common Generic Views:

| Generic View                   | Behavior               |
| ------------------------------ | ---------------------- |
| `ListAPIView`                  | List all objects       |
| `CreateAPIView`                | Create a new object    |
| `RetrieveAPIView`              | Retrieve single object |
| `UpdateAPIView`                | Update single object   |
| `DestroyAPIView`               | Delete single object   |
| `ListCreateAPIView`            | List + Create          |
| `RetrieveUpdateAPIView`        | Get + Update           |
| `RetrieveUpdateDestroyAPIView` | Get + Update + Delete  |

### ✅ Example:

```python
from rest_framework.generics import ListCreateAPIView
from .models import Student
from .serializers import StudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

You don’t need to write `get()` or `post()` – it’s automatically handled!



## 🔹 8. **ViewSets in Django REST Framework**

### ✅ What is a ViewSet?

A `ViewSet` **bundles multiple related actions (GET, POST, PUT, DELETE)** in one class. It eliminates repetitive code and works best with DRF's **Routers**.


### 🔸 `viewsets.ViewSet`

You manually define each method (`list`, `create`, `retrieve`, `update`, `destroy`).

#### ✅ Example:

```python
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
```


### 🔸 `viewsets.ModelViewSet`

This is the **most powerful and commonly used** viewset. It automatically handles `list`, `create`, `retrieve`, `update`, and `delete` actions.

#### ✅ Example:

```python
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

Just register it with a router and you get a full CRUD API!



### 🔄 Summary Table

| Concept            | Description                  | Example Use                      |
| ------------------ | ---------------------------- | -------------------------------- |
| **Mixins**         | Reusable action classes      | Combine with `GenericAPIView`    |
| **GenericAPIView** | Base class for custom views  | Custom views with flexible logic |
| **Generics**       | Ready-made views with mixins | Fast CRUD setup with less code   |
| **ViewSet**        | Group of related methods     | Good for clean routing           |
| **ModelViewSet**   | Full CRUD in one class       | Best for quick API setup         |




## 🔹 8. **Routers in Django REST Framework**

### ✅ What is a Router?

In Django REST Framework, a **Router** automatically generates **URLConf (URLs)** for your **ViewSets**. It **simplifies routing** and reduces repetitive code.

### ✅ Why Use Routers?

* Automatically handles URL patterns for common actions (`list`, `create`, `retrieve`, `update`, `destroy`).
* Works with `ViewSet` or `ModelViewSet`.
* Clean and DRY approach for CRUD API routing.



### ✅ Example (Using `ModelViewSet` and `DefaultRouter`)

#### **views.py**

```python
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

#### **urls.py**

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

### ✅ Auto-generated URLs:

| URL               | Method | Action               |
| ----------------- | ------ | -------------------- |
| `/students/`      | GET    | List all students    |
| `/students/`      | POST   | Create a new student |
| `/students/<id>/` | GET    | Retrieve a student   |
| `/students/<id>/` | PUT    | Update a student     |
| `/students/<id>/` | DELETE | Delete a student     |



## 🔹 9. **Nested Serializers**

### ✅ What is a Nested Serializer?

Nested serializers allow you to **embed related data** inside another serializer. It's useful when you have **foreign key relationships** or **related models**.



### ✅ Example Scenario

Let’s say you have two models:

#### **models.py**

```python
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='students', on_delete=models.CASCADE)
```



### ✅ Without Nested Serializer

You’d only get course `id` inside student:

```json
{
  "name": "John",
  "course": 1
}
```


### ✅ With Nested Serializer

You can include the full course details in the student serializer:

#### **serializers.py**

```python
from rest_framework import serializers
from .models import Student, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'course']
```

### ✅ Output with nested data:

```json
{
  "id": 1,
  "name": "John",
  "course": {
    "id": 1,
    "name": "Math"
  }
}
```


### ✅ Writable Nested Serializer (Optional)

If you want to **create/update nested models**, you need to override `create()` or `update()` methods inside the serializer.



### 🔄 Summary Table

| Concept               | Description                             | Example Use                                 |
| --------------------- | --------------------------------------- | ------------------------------------------- |
| **Router**            | Automatically creates URLs for viewsets | `DefaultRouter().register()`                |
| **Nested Serializer** | Embed related models in API response    | `StudentSerializer` with `CourseSerializer` |





## 🔹 10. **Pagination in Django REST Framework**

Pagination is used to **break up large result sets** into manageable "pages" so that your API doesn't return too much data at once.

DRF supports various pagination styles like:

* `PageNumberPagination`
* `LimitOffsetPagination`

---

### ✅ A. **PageNumberPagination**

Returns results **page by page** (like page 1, 2, 3...).

#### 🔸 Configuration:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}
```

#### 🔸 Example API call:

```http
GET /students/?page=2
```

#### 🔸 Output:

```json
{
  "count": 20,
  "next": "http://api.example.org/students/?page=3",
  "previous": "http://api.example.org/students/?page=1",
  "results": [
    {"id": 6, "name": "John"},
    ...
  ]
}
```


### ✅ B. **LimitOffsetPagination**

Uses **`limit`** and **`offset`** query params.

* **`limit`** = number of items per page.
* **`offset`** = starting index of records.

#### 🔸 Configuration:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5
}
```

#### 🔸 Example API call:

```http
GET /students/?limit=3&offset=6
```

* This returns **3 items**, starting from the **7th record (offset 6)**.

#### 🔸 Output:

```json
{
  "count": 20,
  "next": "http://api.example.org/students/?limit=3&offset=9",
  "previous": "http://api.example.org/students/?limit=3&offset=3",
  "results": [...]
}
```

---

## 🔹 11. **Filtering in Django REST Framework**

Filtering is used to **narrow down querysets** based on client parameters.

DRF supports:

* Custom Filters (via `DjangoFilterBackend`)
* Search Filter
* Ordering Filter



### ✅ A. **Custom Filter (DjangoFilterBackend)**

Filter by specific fields using query params.

#### 🔸 Install and configure:

```bash
pip install django-filter
```

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

#### 🔸 views.py

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'course']
```

#### 🔸 Example API:

```
GET /students/?name=John&course=Math
```

---

### ✅ B. **SearchFilter**

Used for simple keyword search across one or more fields.

#### 🔸 views.py

```python
from rest_framework.filters import SearchFilter

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'course__name']
```

#### 🔸 Example API:

```
GET /students/?search=John
```



### ✅ C. **OrderingFilter**

Allows client to sort the results.

#### 🔸 views.py

```python
from rest_framework.filters import OrderingFilter

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'id']
```

#### 🔸 Example API:

```
GET /students/?ordering=name
GET /students/?ordering=-id
```

---

### ✅ D. **Combined Filters**

```python
filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
```

Now you can:

```
GET /students/?search=John&course=Math&ordering=name
```



## 🔄 Summary Table

| Feature               | Purpose                   | Example              |
| --------------------- | ------------------------- | -------------------- |
| PageNumberPagination  | Page-based navigation     | `?page=2`            |
| LimitOffsetPagination | Custom limits/offsets     | `?limit=5&offset=10` |
| Custom Filter         | Filter by specific fields | `?name=John`         |
| Search Filter         | Keyword search            | `?search=math`       |
| Ordering Filter       | Sort results              | `?ordering=name`     |