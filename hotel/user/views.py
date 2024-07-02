from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from user.forms import RegisterForm, AuthForm


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    register_form = RegisterForm()
    if request.method== "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request,user)
            return redirect('profile')

    ctx = {
        'form':register_form
    }
    return render(request, 'user/register.html', context=ctx)

def auth(request):
    if request.user.is_authenticated:
        return redirect('profile')
    auth_form = AuthForm()
    if request.method== "POST":
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            user_name = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(request, username=user_name,password=password)
            if user:
                login(request,user)
                return redirect('profile')

    ctx = {
        'form':auth_form
    }
    return render(request, 'user/auth.html', context=ctx)


def profile(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    ctx = {
        'user': request.user
    }
    return render(request, 'user/profile.html', context=ctx)

def logout_view(request):
    logout(request)
    return redirect('auth')