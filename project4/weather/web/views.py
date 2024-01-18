from django.shortcuts import render
# from django.http import HttpResponse
from . models import *
import requests
# Create your views here.
def index(requst):
    contxt={}
    api_key='360e4bc3865e745ec844bd7ec054ca11'
    city='kochi'
    if requst.method=='POST':
        city=requst.POST.get('city')
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response=requests.get(url)
    data=response.json()
    contxt['city']=city
    contxt['weather']=data['weather'][0]['description']
    contxt['current_temp']=data['main']['temp']
    contxt['min_temp']=data['main']['temp_min']
    contxt['max_temp']=data['main']['temp_max']
    contxt['feel_like']=data['main']['feels_like']
    return render(requst,'index.html',contxt)