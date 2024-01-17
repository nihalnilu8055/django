from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def index(requst):
    contxt={}
    desi=Designation,object.all()
    dept=Dept,object.all()
    staff=Staff,object.all()
    contxt['desi']=desi
    contxt['dept']=dept
    contxt['staff']=Staff
    return render(requst,'index.html',contxt)