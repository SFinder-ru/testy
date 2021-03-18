from django.shortcuts import render
from .models import User


def user_profile(request):
    profile = User.objects.filter(user_login='user2')
    context = {
        'profile': profile,
        'title': 'Профиль пользователя'
    }
    return render(request, 'site_pages/user_profile.html', context=context)


def home(request):
    return render(request, 'site_pages/home.html')


def about_us(request):
    return render(request, "site_pages/about.html")


def chat(reguest):
    return render(reguest, 'site_pages/chat.html')

