#!/usr/bin/env python3
from django.urls import path
from main import views

urlpatterns = [
    path("home/", views.homepage, name="home"),
    path("items/", views.itemspage, name="items"),
    path("login/", views.loginpage, name="login"),
    path("register/", views.registerpage, name="register"),
]
