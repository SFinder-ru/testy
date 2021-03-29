from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm
from .models import AdvUser


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = '/accounts/login/'


class BBLoginView(LoginView):
    template_name = 'main/login.html'


