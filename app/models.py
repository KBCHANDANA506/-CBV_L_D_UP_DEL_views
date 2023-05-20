from django.db import models
from django.urls import reverse
# Create your models here.


class School(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
   


class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='schools')
    sname=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.sname

    
