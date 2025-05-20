from django.shortcuts import render
from django.shortcuts import render
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from nesteadSerializer.models import Blog, Comments
from nesteadSerializer.serializers import BlogSerializer, CommentSerializer
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from pagination.pagination import CustomPagination
from .filters import EmployeeFilter




# Employee:
class EmployeeDetails(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination # Use custom Pagination that overrides the global pagination ()
    # filterset_fields = ['emp_designation']
    filterset_class = EmployeeFilter
    
    
# Search Filter:
from rest_framework.filters import SearchFilter, OrderingFilter

class BlogsViewSets(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title']
    ordering_fileds = ['id']
    
    
