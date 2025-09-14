from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("service", views.services, name="service"),
    path("contact", views.contact, name="contact"),
    path("register/", views.register_view, name="register"), 
    path("login/", views.user_login, name="login"),
]
