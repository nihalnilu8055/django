from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.
def index(requst):
    contxt={}
    form=Todo_Form()
    if requst.method=='POST':
        if 'save' in requst.POST:
            form=Todo_Form(requst.POST)
            form.save()
        elif 'delete' in requst.POST:
            key=requst.POST.get('delete')
            todo=Todo.objects.get(id=key)
            todo.delete()
    todo=Todo.objects.all()
    contxt['form']=form
    contxt['todo']=todo
    return render(requst,'index.html',contxt)