from django.contrib import admin
from . models import *

class Student_display(admin.ModelAdmin):
    list_display=['name','batch','collage','dept','fee']
# Register your models here.
admin.site.register(Student,Student_display)
