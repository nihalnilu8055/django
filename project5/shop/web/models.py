from django.db import models

# Create your models here.
class Mobile(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    images=models.CharField(max_length=255)
class Computer(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    images=models.CharField(max_length=255)
class Product(models.Model):
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    computer=models.ForeignKey(Computer,on_delete=models.CASCADE)
