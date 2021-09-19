from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

# Create your views here.
def homePage(request):
    return render(request, 'homePage.html')

def aboutPage(request):
    return render(request, 'about.html')

def loginPage(request):
    return render(request,'auth.html', context={'auth':'login'})

def registerPage(request):
    return render(request,'auth.html', context={'auth':'logup'})

@login_required(login_url='/admin')
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