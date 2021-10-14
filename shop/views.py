from django.http.response import HttpResponse
from django.shortcuts import render
from .models import product

# Create your views here.
def shopHome(request):
    products = product.objects.all()
    return render(request, 'shop.html', context={'products': products})