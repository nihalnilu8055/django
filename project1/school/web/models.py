from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    def __str__(self):
        return self.name
class Batch(models.Model):
    batch=models.CharField(max_length=255)
    def __str__(self):
        return self.batch 
class Dept(models.Model):
    dept=models.CharField(max_length=255)
    def __str__(self):
        return self.dept 
class Student(models.Model):
    name=models.CharField(max_length=255)
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)