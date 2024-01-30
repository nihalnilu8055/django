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
            key=requst.POST.get('save')

            if not key:

                form=Todo_Form(requst.POST)

            else:
                todo=Todo.objects.get(id=key)
                form=Todo_Form(requst.POST,instance=todo)





            form.save()
            form=Todo_Form()




            
        elif 'delete' in requst.POST:
            key=requst.POST.get('delete')
            todo=Todo.objects.get(id=key)
            todo.delete()
        elif 'edit' in requst.POST:
            key=requst.POST.get('edit')
            todo=Todo.objects.get(id=key)
            form=Todo_Form(instance=todo)
    else:
        form=Todo_Form()
    todo=Todo.objects.all()
    contxt['form']=form
    contxt['todo']=todo
    return render(requst,'index.html',contxt)