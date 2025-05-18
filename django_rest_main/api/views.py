from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



# Static Data Passing:
def studentsViews(request):
    students = {
        "id": 1,
        "name": "Dibyendu Biswas",
        "email": "dibyendubiswas1998@gmail.com",
        "phone": "+91-xxxxxxxxxx"
    }
    return JsonResponse(students)


# Dynamic Data:
# Use Manual Serializer
def studentViews2(request):
    students = Student.objects.all()

    student_list = list(students.values())
    
    return JsonResponse(student_list, safe=False)


# Dynamic Data:
# Use Serializer Auto using rest_framework
@api_view(['GET','POST'])
def studentViews3(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# Fetch single student info using primary key:
@api_view(['GET','POST'])
def studentViews4(request, pk:int):
    try:
        students = Student.objects.get(pk=pk)
        print(students)
    
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data, status=status.HTTP_200_OK)