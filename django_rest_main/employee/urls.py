from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", EmployeeViews.as_view(), name="employee"),
    path("employee/<int:pk>", EmployeeViews2.as_view(), name="getEmployee"),
    
]
