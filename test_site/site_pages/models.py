from django.db import models
from django.utils.timezone import now


class User(models.Model):
    user_login = models.CharField(max_length=50, verbose_name='Логин')
    user_password = models.CharField(max_length=50, verbose_name='Пароль')
    email = models.EmailField(max_length=50, blank=True,
                              verbose_name='Электронная почта')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True,
                                 verbose_name='Фамилия')
    created_at = models.DateTimeField(verbose_name='Дата создания профиля',
                                      default=now, editable=False,)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Последняя активность')
    prof_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                 verbose_name='Аватарка')
    github_url = models.URLField(max_length=150, blank=True,
                                 verbose_name='Ссылка на GitHub')
    gitlab_url = models.URLField(max_length=150, blank=True,
                                 verbose_name='Ссылка на GitLab')
    vk_url = models.URLField(max_length=150, blank=True,
                             verbose_name='Ссылка на VK')
    fav_users = models.ManyToManyField('FavUsers', blank=True)
    part_projects = models.ManyToManyField('PartProjects', blank=True)
    fav_projects = models.ManyToManyField('FavProjects', blank=True)

    def __str__(self):
        return self.user_login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class FavUsers(models.Model):
    fav_users = models.CharField(max_length=200, default='Отсутствует',
                                 verbose_name="Избранные пользователи")

    def __str__(self):
        return self.fav_users

    class Meta:
        verbose_name = 'Избранный пользователь'
        verbose_name_plural = 'Избранные пользователи'


class PartProjects(models.Model):
    part_projects = models.CharField(max_length=200, default='Отсутствует',
                                     verbose_name="Проекты, в которых"
                                                  "участвует")

    def __str__(self):
        return self.part_projects

    class Meta:
        verbose_name = 'Проект, в котором участвует'
        verbose_name_plural = 'Проекты, в которых участвует'


class FavProjects(models.Model):
    fav_projects = models.CharField(max_length=200, default='Отсутствует',
                                    verbose_name="Избранные проекты")

    def __str__(self):
        return self.fav_projects

    class Meta:
        verbose_name = 'Избранный проект'
        verbose_name_plural = 'Избранные проекты'


# Create your models here.
