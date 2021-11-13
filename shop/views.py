from typing import ContextManager
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import product
from .forms import addProd as addForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.http import Http404

# Create your views here.
def shopHome(request):
    products = product.objects.all()
    return render(request, 'shop.html', context={'products': products})

def productDetail(request, slug):
    products = product.objects.filter(slug=slug).first()
    if products is None:
        raise Http404("Poll does not exist")
    else:
        return render(request ,'product.html', context={'product':products})

@login_required(login_url="/login")
def addProd(request):
    form = addForm()
    if request.method == 'POST':
        if form.is_valid:
            import string    
            import random
            product_name = request.POST['Product_Name']
            product_img = request.FILES['Image']
            product_desc = request.POST['Description']
            product_price = request.POST['price']
            product_seller = request.user
            product_slug = product_name
            product_slug = product_slug.lower().replace('-','').replace(' ', '-')
            for i in product_slug:
                if i not in['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    product_slug = product_slug.replace(i, '')
            slugRan = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 10)))
            product_slug = product_slug + f"-{slugRan}"
            print(product_slug)
            newProd = product(name = product_name, prodImg = product_img, desc=product_desc, price= product_price, seller = product_seller, slug = product_slug)
            newProd.save()
            messages.success(request, 'Product sold successfully!!')
            return redirect(f'/shop/{product_slug}')
        else:
            print("invalid")
    return render(request, 'addProd.html', context={"form":form})

def checkout(request):
    if request.method == 'POST':
        slug = request.POST["slug"]
        return redirect(f'/shop/{slug}')
    return redirect('')