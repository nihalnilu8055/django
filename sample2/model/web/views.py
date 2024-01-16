from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requst):
    return HttpResponse('<h1>index</h1>')

def about(requst):
    return HttpResponse('<h1>about</h1>')