from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def chat(reguest):
    return render(reguest, 'chat.html')