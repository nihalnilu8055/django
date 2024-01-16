from django.contrib import admin
from . models import *
class Desi_display(admin.ModelAdmin):
    list_display=['designation']
class Dept_display(admin.ModelAdmin):
    list_display=['dept']
class Staff_display(admin.ModelAdmin):
    list_display=['name','salary','designation','department']
# Register your models here.
admin.site.register(Designation,Desi_display)
admin.site.register(Dept,Dept_display)
admin.site.register(Staff,Staff_display)