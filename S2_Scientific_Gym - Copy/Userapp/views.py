from django.shortcuts import render, redirect
from django.http import HttpResponse
from Adminapp.models import Register, SignupInfo, WorkoutCategory, WorkoutExercise, WorkoutSubcategory, Packages
from django.contrib import messages

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
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]

        try:
            user = SignupInfo.objects.get(Username=uname, Password=pwd)
        except:
            messages.success(request, 'Invalid login !')
            return redirect(login)
        else:
            request.session["Username"] = uname
            return redirect(index)


def Signout(request):
    request.session.clear()
    return redirect(index)


def Signup(request):
    uname = request.POST['uname']
    email = request.POST['email']
    pwd = request.POST['pwd']
    mobile = request.POST['mobile']

    try:
        user = SignupInfo.objects.get(Username=uname)
    except :

        sig = SignupInfo()
        sig.Username = uname
        sig.Email = email
        sig.Password = pwd
        sig.Mobile = mobile
        sig.save()
    else:
        messages.success(request, 'Username already available!')

    return redirect(login)


def membership(request):
    pack = Packages.objects.all()
    return render(request, "membership.html", {"pack":pack})


def workout(request):
    catg = WorkoutCategory.objects.all()
    pack = Packages.objects.all()
    return render(request, "workout.html", {"catg":catg, "pack":pack})


def Subcategory(request):
    subcat = WorkoutSubcategory.objects.all()
    return render(request, "WorkoutSubcategory.html", {"subcat":subcat})


def Exercise(request, did):
    cat = WorkoutCategory.objects.get(id=did)
    exer = WorkoutExercise.objects.filter(Category=cat)
    return render(request, "WorkoutExercise.html", {"exer":exer})


def trainer(request):
    return render(request, "trainer.html", {})


def TrainerProfile(request):
    return render(request, "TrainerProfile.html", {})

def HealthyLives(request):
    return render(request, "HealthyLives.html", {})