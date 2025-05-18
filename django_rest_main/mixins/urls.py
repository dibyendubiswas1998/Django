from django.urls import path
from .views import *

urlpatterns = [
    path("mix", Employees.as_view(), name="mix"),
    path("mix/<int:pk>", Employee2.as_view(), name="mix2")
]
