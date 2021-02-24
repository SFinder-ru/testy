from django.shortcuts import render


def home(request):
    return render(request, 'site_pages/home.html')


def chat(reguest):
    return render(reguest, 'site_pages/chat.html')
