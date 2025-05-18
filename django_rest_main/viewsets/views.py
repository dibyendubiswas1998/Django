from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics, viewsets




# Use viewsets:
class EmployeeViewSet(viewsets.ViewSet):
    
    def list(self, request):
        try:
            queryset = Employee.objects.all()
            serializer = EmployeeSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as ex:
            raise ex
        
    
    def create(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as ex:
            raise ex
        
    def retrieve(self, request, pk=None):
        try:
            employee = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        except Exception as ex:
            raise ex
        
        
    def update(self, request, pk=None):
        try:
            employee = get_object_or_404(Employee, pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as ex:
            raise ex
        
    
    def delete(self, request, pk=None):
        try:
            employee = get_object_or_404(Employee, pk=pk)
            employee.delete()
            return Response(data="Employee deleted successfully", status=status.HTTP_204_NO_CONTENT)
        
        except Exception as ex:
            raise ex
        
        

class EmployeeModelViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer