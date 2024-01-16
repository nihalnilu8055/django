from django.shortcuts import render
from django.http import HttpResponse
from . models import*
# Create your views here.
def index(requst):
    std=Student.objects.all()
    return render(requst,'index.html',{'std':std})