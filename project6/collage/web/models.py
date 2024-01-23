from django.db import models

# Create your models here.
# class Collage_Managmnt(models.Model):
#     collge_name=models.CharField(max_length=255)
#     city=models.CharField(max_length=255)
#     contact_no=models.IntegerField()

class Dept(models.Model):
    dept_name=models.CharField(max_length=255)
    hod_name=models.CharField(max_length=255)
    total_staff=models.IntegerField()
    total_stud=models.IntegerField()

class Classroom(models.Model):
    section=models.CharField(max_length=255)
    dept=models.ForeignKey(Dept,on_delete=models.CASCADE)