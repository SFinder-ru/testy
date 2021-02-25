from django.shortcuts import render


def home(request):
    return render(request, 'site_pages/home.html')


def about_us(request):
    return render(request, "site_pages/about.html")


def chat(reguest):
    return render(reguest, 'site_pages/chat.html')

