from rest_framework.mixins import ListModelMixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView

# from rest_framework import generics

from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin



#In the Mixins -> List and Create does not need pk so they can merge

# Together Mixins

class StudentWithOutPK(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)


class StudentWithPK(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        
        return self.destroy(request, *args, **kwargs)




# Single-Single Mixins


# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
        
#         return self.list(request, *args, **kwargs)


# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs):
        
#         return self.create(request, *args, **kwargs)



# class StudentRetrive(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
        
#         return self.retrieve(request, *args, **kwargs)
    

# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def put(self, request, *args, **kwargs):
        
#         return self.update(request, *args, **kwargs)
    

    
# class StudentDelete(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def delete(self, request, *args, **kwargs):
        
#         return self.destroy(request, *args, **kwargs)