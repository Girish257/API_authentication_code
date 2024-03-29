from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse

from django.http import HttpResponse, JsonResponse
# Create your views here.

# Model Object - Single Student data


def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    # print(stu)
    serializer = StudentSerializer(stu) 
    # change the complex data to python by serializer
    # print(serializer)
    # print(serializer.data)
    
#json_data = JSONRenderer().render(serializer.data)
    # changes the pyhton data to json data
    # print(json_data)

# return HttpResponse(json_data, content_type='application/json')
    # and send the json data to the client
    return JsonResponse(serializer.data, safe=True)


# Query-set - all student data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True) 
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')