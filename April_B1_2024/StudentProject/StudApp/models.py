from django.db import models

# Create your models here.
class StudentDb(models.Model):
    StudId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Place = models.CharField(max_length=50)
    Course = models.CharField(max_length=50)

class TeacherDb(models.Model):
    TeacherId=models.AutoField(primary_key=True)
    tName=models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Mobile=models.IntegerField()

