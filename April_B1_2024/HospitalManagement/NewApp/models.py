from django.db import models

# Create your models here.
class PatientDb(models.Model):
    PatientId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Age = models.IntegerField()
    Place = models.CharField(max_length=100)
    Mobile = models.IntegerField()
    Image = models.CharField(max_length=100)
