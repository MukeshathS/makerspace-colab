from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import RegistrationForm
from django.conf import settings

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        args = {'user': request.user}
        return render(request, 'profile/home.html',args)
    else:
        args = {'user': 'Hello Guest!'}
        return render(request, 'base.html', args)

def register(request):
    form = RegistrationForm()
    args = {'form': form, 'user': 'Hello Guest!'}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            args = {'form': form, 'user': 'Hello Guest!'}
            return render(request, 'profile/register.html', args)

    return render(request, 'profile/register.html', args)

def logout(request):
    auth.logout(request)
    args = {'user': 'Hello Guest!'}
    return render(request, 'profile/logout.html', args)
