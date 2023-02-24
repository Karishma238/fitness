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


def login(request):
    if(request.method == "GET"):
        return render(request, "login.html", {})
    else:
        pass


def membership(request):
    return render(request, "membership.html", {})


def workout(request):
    return render(request, "workout.html", {})


