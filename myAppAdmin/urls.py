from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register.html', views.register, name='register'),
    path('login.html', views.register, name='register'),
    path('404.html', views.error, name='error'),
    path('forgot-password.html', views.forgot, name='forgot'),
    path('blank.html', views.blank, name='blank'),
    path('index.html', views.index, name='index'),
    path('form.html', views.form, name='form'),
    path('charts.html', views.charts, name='charts'),
]