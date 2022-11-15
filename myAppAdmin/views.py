from django.shortcuts import render, HttpResponse
from myAppAdmin.models import Contact
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def form(request):
    if request.is_ajax() and request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone1 = request.POST.get("phone1")
        file1 = request.FILES
        file2 = file1.get('file1')
        print('First Name is', name, email, phone1, file2)
        contact = Contact.objects.create(name=name, email=email, phone=phone1, file1= file2)
        contact.save()
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
    
