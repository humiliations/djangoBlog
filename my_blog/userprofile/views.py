from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm


def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect('article:article_list')
            else:
                return HttpResponse("账号或密码输入有误")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("使用GET或POST方法请求数据")


def user_logout(request):
    logout(request)
    return redirect('article:article_list')


def user_register(request):
    if request.method == "POST":
        pass
    elif request.mothod == "GET":
        pass
    else:
        return HttpResponse("使用GET或POST方法请求数据")