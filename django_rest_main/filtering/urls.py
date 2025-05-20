from django.urls import path
from .admin import *
from .views import *

urlpatterns = [
    # employee:
    path("employees/", EmployeeDetails.as_view(), name="employees"),
    
    # Blog by search
    path("blogs/", BlogsViewSets.as_view(), name="blog"),
]
