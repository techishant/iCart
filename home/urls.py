
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('products', views.productPage, name="productsPage"),
    path('account', views.accountPage, name="accountPage"),
    path('cart', views.cartPage, name='cartPage'),
    path('products/<str:slug>', views.productDetailPage, name="productDetailPage")
]
