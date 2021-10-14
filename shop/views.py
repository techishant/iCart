from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def shopHome(request):
    return render(request, 'shop.html')