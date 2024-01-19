from django.db import models

# Create your models here.
class Mobile(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    images=models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Computer(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    images=models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Product(models.Model):
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    computer=models.ForeignKey(Computer,on_delete=models.CASCADE)
