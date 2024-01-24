from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.
def index(requst):
    contxt={}   #make empty dict
    form=Todo_form()    #passing clss to an object
    if requst.method=='POST':
        form=Todo_form(requst.POST)     #feching data from the txt box
        form.save()     #adding data to table
    # print(requst.POST.get('task'))
    todo=Todo.objects.all()        #passing all data from an object
    contxt['form']=form     #adding to dict
    contxt['todo']=todo
    return render(requst,'index.html',contxt)       #passing values to frontend