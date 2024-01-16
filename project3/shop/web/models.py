from django.db import models

# Create your models here.
class Designation(models.Model):
    designation=models.CharField(max_length=255)
class Dept(models.Model):
    dept=models.CharField(max_length=255)
class Staff(models.Model):
    name=models.CharField(max_length=255)
    salary=models.IntegerField()
    designation=models.ForeignKey(Designation,on_delete=models.CASCADE)
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
