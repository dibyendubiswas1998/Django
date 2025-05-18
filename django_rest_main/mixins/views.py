from django.shortcuts import render
from django.shortcuts import render
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics




class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
        mixins.ListModelMixin: Get all the records.
        mixins.CreateModelMixin: Create a new record.
        generics.GenericAPIView: Handle the http methods, like get, post, put, delete
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    # get all the records:
    def get(self, request):
        try:
            return self.list(request)
        
        except Exception as ex:
            raise ex
        
    # Create New Records:
    def post(self, request):
        try:
            return self.create(request)
        
        except Exception as ex:
            raise ex
        

class Employee2(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
        mixins.RetrieveModelMixin: Get a single record or specific record.
        mixins.UpdateModelMixin: Update a single record or specific record.
        mixins.DestroyModelMixin: Delete a single record or specific record.
        generics.GenericAPIView: Handle the http methods, like get, post, put, delete.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
    # Get a Specific Record
    def get(self, request, pk):
        try:
            return self.retrieve(request, pk)
        
        except Exception as ex:
            raise ex
        
    
    # Update Specific Record
    def put(self, request, pk):
        try:
            return self.update(request, pk)
        
        except Exception as ex:
            raise ex
        
    
    def delete(self, request, pk):
        try:
            return self.destroy(request, pk)
        
        except Exception as ex:
            raise ex