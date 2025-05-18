from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.



class EmployeeViews(APIView):

    # Get all the records from Employee Table
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
    # Create a new Employee or Add New Employee:
    def post(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as ex:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class EmployeeViews2(APIView):
    
    # Get Object help to get a specific records
    def get_object(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return employee
        
        except Employee.DoesNotExist:
            # return Response({"message": "Employee Not Found"}, status=status.HTTP_404_NOT_FOUND)
            raise Http404

    
    # Get Single Employee based on Primary Key:
    def get(self, request, pk):
        try:
            employee = self.get_object(pk=pk)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as ex:
            raise ex
        
        
    # Update a Specific records:
    def put(self, request, pk):
        try:
            employee = self.get_object(pk=pk) # get the specific recods
            
            serializer = EmployeeSerializer(employee, data=request.data) # update the specific records.
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as ex:
            raise ex
    
    # Delete a specific records:
    def delete(self, request, pk):
        try:
            employee = self.get_object(pk=pk) # get the specific records.
            employee.delete()
            return Response({"message": "Employee Deleted"}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as ex:
            raise ex