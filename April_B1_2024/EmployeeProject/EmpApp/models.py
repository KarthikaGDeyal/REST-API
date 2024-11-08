from django.db import models

# Create your models here.
class EmpDb(models.Model):
    EmpId=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Place = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)

