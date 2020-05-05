from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from user.forms import LoginForm, RegistrationForm, UserProfileForm
from user.models import User


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = User.objects.filter(username=cd["username"], password=cd["password"])
            if user:
                return HttpResponse("Welcome {}".format(user.first().username))
            else:
                return HttpResponse("对不起，您的账号或者密码有误")
        else:
            return HttpResponse("登录错误")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "user/login.html", {"form": login_form})

def user_register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        user_profile = UserProfileForm(request.POST)
        if user_form.is_valid() and user_profile.is_valid():
            new_user = user_form.save(commit=False)
            new_user.password = user_form.cleaned_data["password1"]
            new_user.save()
            new_profile = user_profile.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse("注册成功")
        else:
            print(user_form.is_valid())
            print(user_profile.is_valid())
            return HttpResponse("表单提交有误，注册失败")

    if request.method == "GET":
        user_form = RegistrationForm()
        user_profile = UserProfileForm()
        context = {
            "form": user_form,
            "profile": user_profile
        }
        return render(request, "user/register.html", context=context)
