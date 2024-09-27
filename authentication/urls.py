
from django.contrib import admin
from django.urls import path , include
from . import views 

urlpatterns = [
    path('home' , views.home , name = 'home'),
    path('signup' , views.signup , name = 'signup'),
    path('' , views.signin , name = 'signin'),
    path('signout' , views.signin , name = 'signout'),
]
