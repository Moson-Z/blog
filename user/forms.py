#!/usr/bin/python3.6+
# -*- coding:utf-8 -*-
from django import forms

from .models import User, UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)


class RegistrationForm(forms.ModelForm):

    password1 = forms.CharField(label="密码", widget=forms.PasswordInput)
    password2 = forms.CharField(label="再次输入密码", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("两次输入的密码不匹配")
        return cd["password2"]

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["email", "birth", "phone"]