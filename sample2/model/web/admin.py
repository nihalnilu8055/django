from django.contrib import admin
from . models import *

class Student_disply(admin.ModelAdmin):
    list_display=['name','age','phone_number']
# Register your models here.
admin.site.register(Student,Student_disply)
