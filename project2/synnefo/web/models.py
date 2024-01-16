from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=255)
    batch=models.CharField(max_length=255)
    collage=models.CharField(max_length=255)
    dept=models.CharField(max_length=255)
    fee=models.IntegerField()