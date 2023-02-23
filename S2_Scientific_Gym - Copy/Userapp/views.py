from django.shortcuts import render, redirect
from django.http import HttpResponse
from Adminapp.models import Register

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def register(request):
    name = request.POST['Uname']
    email = request.POST['Email']
    phone = request.POST['Phone']
    location = request.POST['Location']
    message = request.POST['Msg']

    reg = Register()
    reg.Name = name
    reg.Email = email
    reg.Phone = phone
    reg.Location = location
    reg.Message = message
    reg.save()
    return redirect(index)


def blog(request):
    return render(request, "blog.html", {})




