from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'home.html')

def productPage(request):
    return render(request, 'products.html')