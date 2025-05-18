from django.urls import path
from .views import  *

urlpatterns = [
    path("students/", studentsViews, name="studentViews"),
    path("students2/", studentViews2, name="studentViews2"),
    path("students3/", studentViews3, name="studentViews3"),
    path("students4/<int:pk>/", studentViews4, name="studentViews4"),
]
