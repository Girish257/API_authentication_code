from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# @api_view()          # BY default it is GET
# def hello_world(request):
#     return Response({'msg': 'Hello World!!'})

# @api_view(['GET']) 
# def hello_world(request):
#     return Response({'msg': 'Hello World!!'})

# @api_view(['POST']) # BY default it is GET
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'Hello POST!!'})
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request):
    if request.method == 'GET':

        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    if request.method == 'POST':

        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created From POST!!'})

        return Response(serializer.errors)

        
    
    if request.method == 'PUT':

        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated From PUT ++++++++'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':

        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})
        