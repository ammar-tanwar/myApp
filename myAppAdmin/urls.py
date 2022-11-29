from django.urls import path
from .views import allformfunc 

urlpatterns = [
    path('', allformfunc.index, name='index'),
    path('register.html', allformfunc.register, name='register'),
    path('login.html', allformfunc.register, name='register'),
    path('404.html', allformfunc.error, name='error'),
    path('forgot-password.html', allformfunc.forgot, name='forgot'),
    path('blank.html', allformfunc.blank, name='blank'),
    path('index.html', allformfunc.index, name='index'),
    path('form.html', allformfunc.form, name='form'),
    path('charts.html', allformfunc.charts, name='charts'),
]