from django.shortcuts import render
from django.shortcuts import render
from .models import Blog, Comments
from .serializers import BlogSerializer, CommentSerializer
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics




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