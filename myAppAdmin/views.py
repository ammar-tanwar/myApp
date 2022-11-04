from datetime import datetime
from django.shortcuts import render, HttpResponse
from myAppAdmin.models import Contact
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        file = request.POST.get('file')
        contact = Contact(name=name, email=email, phone=phone, file=file, date=datetime.today())
        contact.save()
        messages.success(request, 'Profile details updated!')
    return render(request, 'form.html')
    
def charts(request):
    return render(request, 'charts.html')

def forgot(request):
    return render(request, 'forgot-password.html')

def error(request):
    return render(request, '404.html')

def blank(request):
    return render(request, 'blank.html')

def about(request):
    return HttpResponse("about page")
    
