from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.
def index(requst):
    contxt={}
    form=Todo_Form()
    if requst.method=='POST':
        form=Todo_Form(requst.POST)
        form.save()
    todo=Todo.objects.all()
    contxt['form']=form
    contxt['todo']=todo
    return render(requst,'index.html',contxt)