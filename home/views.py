from django.shortcuts import render

# Create your views here.
def homePage(request):
    return render(request, 'home.html')

def productPage(request):
    return render(request, 'products.html')

def accountPage(request):
    return render(request, 'account.html')

def cartPage(request):
    return render(request, 'cart.html')

def productDetailPage(request, slug):
    print(slug)
    return render(request, 'productDetails.html')