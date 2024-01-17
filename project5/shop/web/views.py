from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def index(requst):
    return render(requst,'index.html')

def mobile(requst):
    mob=Mobile.objects.all()
    return render(requst,'phone.html',{'mob':mob})

def computer(requst):
    com=Computer.objects.all()
    return render(requst,'computer.html',{'com':com})