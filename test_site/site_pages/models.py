from django.db import models


class User(models.Model):
    user_login = models.CharField(max_length=50, verbose_name='Логин')
    user_password = models.CharField(max_length=50, verbose_name='Пароль')
    email = models.EmailField(max_length=50, blank=True,
                              verbose_name='Электронная почта')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True,
                                 verbose_name='Фамилия')
    prof_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                 verbose_name='Аватарка')
    github_url = models.URLField(max_length=150, blank=True,
                                 verbose_name='Ссылка на GitHub')
    gitlab_url = models.URLField(max_length=150, blank=True,
                                 verbose_name='Ссылка на GitLab')
    vk_url = models.URLField(max_length=150, blank=True,
                             verbose_name='Ссылка на VK')

    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# Create your models here.
