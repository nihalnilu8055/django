from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def index(requst):
    contxt={}
    tea=Teacher.objects.all()
    bch=Batch.objects.all()
    dept=Dept.objects.all()
    contxt['tea']=tea
    contxt['bch']=bch
    contxt['dept']=dept
    return render(requst,'index.html',contxt)