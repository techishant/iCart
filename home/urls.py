from django.urls import path
from home import views

urlpatterns = [
    path('', views.homePage, name ="homePage"),
    path('contact', views.contactPage, name ="contactPage"),
    path('about', views.aboutPage, name="aboutPAge"),
    path('login', views.loginPage, name="loginPage"),
    path('logup', views.registerPage, name="registerPage"),
    path('logout', views.logoutPage, name="logoutPage"),
]
