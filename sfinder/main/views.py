from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
    
from .forms import ChangeUserInfoForm, ProjectForm
from .models import AdvUser, Project


def landing_index(request):
    return render(request, 'landing/index.html')


def landing_about(request):
    return render(request, 'landing/about.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


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
    subject_template_name = 'account/email/reset_subject.txt'
    email_template_name = 'account/email/reset_email.txt'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'main/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'main/confirm_password.html'


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'main/password_confirmed.html'


class CreateProject(LoginRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = 'project/create_project.html'


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            last_key = Project.objects.count()
            current_key = last_key + 1
            project.id = current_key
            user = request.user
            project.creators.project_id = current_key
            project.creators.advuser_id = user.pk
            project.save()
            return redirect(project.get_absolute_url())
    else:
        form = ProjectForm()
        return render(request, 'project/create_project.html', {'form': form})


class ViewProject(DetailView):
    model = Project
    template_name = 'project/project_detail.html'


class ViewAllProjects(ListView):
    model = Project
    template_name = 'project/project_list.html'
