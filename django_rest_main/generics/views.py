from django.shortcuts import render
from django.shortcuts import render
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics





# Generics: Single
class Eemployee1(generics.ListAPIView, generics.CreateAPIView):
    """
        generics.ListAPIView: Get all the records.
        generics.CreateAPIView: Create/Add the records.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
class EemployeeDetails1(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    """
        generics.RetrieveAPIView: Get all the records.
        generics.UpdateAPIView: Update the specific records based on primary key.
        generics.DestroyAPIView: Delete the specific records based on primary key.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'


################################################################################################################

# Use Combination of Generic
class Eemployee2(generics.ListCreateAPIView):
    """
        generics.ListCreateAPIView: Get all the Records and Create/Add the records.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class EemployeeDetails2(generics.RetrieveUpdateDestroyAPIView):
    """
        RetrieveUpdateDestroyAPIView: Get all the records by primary key, Update the specific records based on primary key and Delete the specific records based on primary key.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
