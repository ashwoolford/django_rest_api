from rest_framework import viewsets

from my_api.models import Students
from .serializers import StudentSerializers

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializers
    queryset = Students.objects.all()  
    #queryset = Student.objects.filter(name="Ashraf")