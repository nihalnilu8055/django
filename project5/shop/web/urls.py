from django.urls import path
from . import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('mobile',views.mobile,name='mobile'),
    path('computer',views.computer,name='computer'),
    path('register',views.register,name='register'),
    path('forms',views.shop,name='forms')
]