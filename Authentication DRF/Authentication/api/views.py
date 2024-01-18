from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny




class StudentModelViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated] # All user can access
    # permission_classes = [AllowAny]  # anyone can access


    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser] # only admin/staff user can access



# if we have so many class in a project so that we can enable aunthentication and
# permission in settings.py file globally.