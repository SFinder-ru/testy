from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm
from .models import AdvUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.core.signing import BadSignature
from .utilities import signer


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'test/register.html'
    form_class = RegisterUserForm
    success_url = '/accounts/login/'


class BBLoginView(LoginView):
    template_name = 'auth/login.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html'
    else:
        template = 'main/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)

