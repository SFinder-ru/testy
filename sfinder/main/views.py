from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.views.generic.edit import CreateView, UpdateView
from .forms import RegisterUserForm, ChangeUserInfoForm
from .models import AdvUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.core.signing import BadSignature


class RegisterDoneView(TemplateView):
    template_name = 'auth/register_done.html'


class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'auth/logout.html'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'auth/register.html'
    form_class = RegisterUserForm
    success_url = '/accounts/login/'


class UserLoginView(LoginView):
    template_name = 'auth/login.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')


"""def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'auth/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'auth/user_is_activated.html'
    else:
        template = 'auth/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)"""


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = '/accounts/profile/'
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class UserPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = '/accounts/profile/'
    success_message = 'Пароль пользователя изменен'


class UserPasswordResetView(PasswordResetView):
    template_name = 'main/password_reset.html'
    subject_template_name = 'email/reset_subject.txt'
    email_template_name = 'email/reset_email.txt'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'main/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'main/confirm_password.html'


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'main/password_confirmed.html'
