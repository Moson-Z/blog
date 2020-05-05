#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
]