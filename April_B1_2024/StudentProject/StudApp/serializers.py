from StudApp.models import StudentDb,TeacherDb
from rest_framework import serializers

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDb
        fields=(
            'StudId',
            'Name',
            'Place',
            'Course'
        )

class Teacher_Serializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherDb
        fields=(
            'TeacherId',
            'tName',
            'Qualification',
            'Subject',
            'Email',
            'Mobile'
        )