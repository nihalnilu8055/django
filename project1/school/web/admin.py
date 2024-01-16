from django.contrib import admin
from . models import *
class Teacher_display(admin.ModelAdmin):
    list_display=['name','age']
class Batch_display(admin.ModelAdmin):
    list_display=['batch']
class Dept_display(admin.ModelAdmin):
    list_display=['dept']
class Student_display(admin.ModelAdmin):
    list_display=['name','dept','batch','teacher']
# Register your models here.
admin.site.register(Teacher,Teacher_display)
admin.site.register(Batch,Batch_display)
admin.site.register(Dept,Dept_display)
admin.site.register(Student,Student_display)