from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requst):
    return HttpResponse('<h1>this is the index page</h1>')

def about(requst):
    return HttpResponse('<h1>this is the about page</h1>')

def contact(requst):
    return HttpResponse('<h1>this is the contact page</h1>')