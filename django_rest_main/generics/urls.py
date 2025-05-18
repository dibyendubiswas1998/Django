from django.urls import path
from .views import *



urlpatterns = [
    path("generic1/", Eemployee1.as_view(),  name="as_view1"),
    path("generic1/<int:pk>/", EemployeeDetails1.as_view(), name="as_view11"),
    
    # Use the Combination of generic
    path("generic2/", Eemployee2.as_view(),  name="as_view()"),
    path("generic2/<int:pk>/", EemployeeDetails2.as_view(),  name="as_view()"),
]
