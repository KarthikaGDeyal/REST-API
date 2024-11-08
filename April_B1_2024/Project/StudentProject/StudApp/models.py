from django.db import models

# Create your models here.
class StudentDb(models.Model):
    Name=models.CharField(max_length=100)
    Course = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Age = models.IntegerField()
    Mobile = models.IntegerField()

    def __str__(self):
        return self.Name
