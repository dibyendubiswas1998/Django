from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("employee", EmployeeViewSet, basename="employee")
# ModelViewSet:
router.register("employee2", EmployeeModelViewSets, basename="employee2")



urlpatterns = [
    path("", include(router.urls)),
]
