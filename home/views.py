from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def homePage(request):
    return render(request, 'homePage.html')

def aboutPage(request):
    return render(request, 'about.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['Lusername']
        paswrd = request.POST['Lpass']
        user = authenticate(request, username= username, password = paswrd)
        messages.success(request, "Successfully logged in !!!")
        return redirect("/")
    return render(request,'auth.html', context={'auth':'login'})

def registerPage(request):
    if request.method == "POST":
        username = request.POST['Rusername']
        mail = request.POST['email']
        fName = request.POST['fName']
        lName = request.POST['lName']
        password = request.POST['Rpass']
        newUser = User.objects.create_user(username, mail, password)
        newUser.first_name = fName
        newUser.last_name = lName
        newUser.save()
        messages.success(request, "Account made Successfully")
        print(username, mail, fName, lName, password)
        return redirect("/login")
    return render(request,'auth.html', context={'auth':'logup'})

@login_required(login_url='/login')
def contactPage(request):
    if request.method == 'POST':
        user = request.user.username
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        mail = request.POST['mail']
        cont = request.POST['conts'].replace("\n", "</br>")
        sub =  request.POST['sub']
        if (len(Lname)<3 or len(Fname)<3 or len(sub)<3 or len(cont)<15):
            messages.error(request, "Please Fill the form properly")
            return redirect('/contact')
        newContact = contact(user = user, fname = Fname, lname = Lname, mail = mail,sub=sub, cont = cont)
        newContact.save()
        messages.success(request, "Your form has been submitted!")
        return redirect("/contact")
    userContact = contact.objects.all().filter(user = request.user)
    # print(userContact[1].cont)
    return render(request, 'contact.html', context={'contact':userContact})

def logoutPage(request):
    logout(request)
    messages.warning(request, "Successfully Logged out!!")
    return redirect("/")