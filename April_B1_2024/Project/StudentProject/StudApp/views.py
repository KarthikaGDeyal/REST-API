from django.shortcuts import render
from rest_framework import viewsets
from StudApp.models import StudentDb
from StudApp.serializers import Student_Serializer

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = Student_Serializer
    queryset=StudentDb.objects.all()
    model=StudentDb
