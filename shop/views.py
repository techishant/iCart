from django.http.response import HttpResponse
from django.shortcuts import render
from .models import product
from .forms import addProd as addForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
def shopHome(request):
    products = product.objects.all()
    return render(request, 'shop.html', context={'products': products})

@login_required(login_url="/login")
def addProd(request):
    form = addForm()
    if request.method == 'POST':
        if form.is_valid:
            product_name = request.POST['Product_Name']
            product_img = request.FILES['Image']
            product_desc = request.POST['Description']
            product_price = request.POST['price']
            product_seller = request.user
            newProd = product(name = product_name, prodImg = product_img, desc=product_desc, price= product_price, seller = product_seller)
            newProd.save()
        else:
            print("invalid")
    return render(request, 'addProd.html', context={"form":form})