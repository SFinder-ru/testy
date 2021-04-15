from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import AdvUser


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
        """user_registered.send(RegisterUserForm, instance=user)"""
        return user

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2')


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label='Адрес электронной почты'
    )

    class Meta:
        model = AdvUser
        fields = ('email', 'first_name', 'last_name',
                  'prof_pic', 'github_url', 'gitlab_url', 'vk_link')
