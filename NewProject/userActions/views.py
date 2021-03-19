from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'userActions/registration.html', {'form': form})


def login(request):
    return render(request, 'userActions/login.html')
