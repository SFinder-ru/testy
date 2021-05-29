from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import AdvUser, Project

import re


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(
        required=False
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Пароль (повторно)',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2')


class ChangeUserInfoForm(forms.ModelForm):
    class Meta:
        model = AdvUser
        fields = ('first_name', 'last_name',
                  'prof_pic', 'github_url', 'gitlab_url', 'vk_link')


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'technologies', 'contacts', 'project_logo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_control'}),
            'description': forms.Textarea(attrs={'class': 'form_control', 'rows': 5}),
            'technologies': forms.SelectMultiple(attrs={'class': 'form_control'}),
            'contacts': forms.Textarea(attrs={'class': 'form_control', 'rows': 3}),
            'project_logo': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
