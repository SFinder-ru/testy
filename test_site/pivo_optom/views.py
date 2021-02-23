from django.shortcuts import render


def home(request):
    return render(request, 'pivo_optom/home.html')
