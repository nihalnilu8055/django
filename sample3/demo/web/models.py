from django.db import models

# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=255)
    salary=models.IntegerField()
    phone_number=models.IntegerField()