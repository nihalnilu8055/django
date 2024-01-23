from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.
def index(requst):
    return render(requst,'index.html')

def mobile(requst):
    mob=Mobile.objects.all()
    return render(requst,'mobile.html',{'mob':mob})

def computer(requst):
    com=Computer.objects.all()
    return render(requst,'computer.html',{'com':com})

def register(requst):
    if requst.method=='POST':
        print(requst.POST.get('fname'))
    return render(requst,'register.html')

def shop(requst):
    if requst.method=='POST':
        items=Mobile_Forms(requst.POST)
        if items.is_valid():
            name=items.cleaned_data['Mobile_name']
            price=items.cleaned_data['price']
            imgs=items.cleaned_data['images']
            data=Mobile.objects.create(name=name,price=price,images=imgs)
            data.save()
    shops=Mobile_Forms()
    return render(requst,'forms.html',{'shops':shops})