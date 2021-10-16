from django.urls import path
from shop import views

urlpatterns = [
    path('', views.shopHome, name="shopHome"),
    path('add', views.addProd, name="addProd")
]