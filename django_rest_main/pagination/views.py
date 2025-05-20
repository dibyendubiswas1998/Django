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
from .pagination import CustomPagination



# Here we use generics:
class BlogsViewSets(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    
class CommentsViewSets(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    
    
# Perform PK based Operations:
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    

# Employee:
class EmployeeDetails(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination # Use custom Pagination that overrides the global pagination ()