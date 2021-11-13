from django.urls import path
from shop import views

urlpatterns = [
    path('', views.shopHome, name="shopHome"),
    path('add', views.addProd, name="addProd"),
    path('checkout', views.checkout, name="checkout"),
    path('<str:slug>', views.productDetail, name="productDetail")
]