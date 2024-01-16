from django.contrib import admin
from . models import *
class Staff_details(admin.ModelAdmin):
    list_display=['name','salary','phone_number']
# Register your models here.
admin.site.register(Staff,Staff_details)
