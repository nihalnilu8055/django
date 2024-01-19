from django.contrib import admin
from web.models import Mobile,Computer,Product
from . models import *
class Mobile_display(admin.ModelAdmin):
    list_display=['name','price','images']
class Computer_display(admin.ModelAdmin):
    list_display=['name','price','images']
class Product_display(admin.ModelAdmin):
    list_display=['mobile','computer']
# Register your models here.
admin.site.register(Mobile,Mobile_display)
admin.site.register(Computer,Computer_display)
admin.site.register(Product,Product_display)