from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
        default=True,
        db_index=True,
        verbose_name='Прошел активацию?'
    )
    prof_pic = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        verbose_name='Аватарка'
    )
    github_url = models.URLField(
        max_length=150,
        blank=True,
        verbose_name='Ссылка на GitHub'
    )
    gitlab_url = models.URLField(
        max_length=150,
        blank=True,
        verbose_name='Ссылка на GitLab'
    )
    vk_link = models.URLField(
        max_length=150,
        blank=True,
        verbose_name='Ссылка на вк'
    )
    fav_users = models.ManyToManyField(
        'FavUsers',
        blank=True,
        verbose_name='Избранные пользователи'
    )
    part_projects = models.ManyToManyField(
        'PartProjects',
        blank=True,
        verbose_name='Проекты, в которых участвует'
    )
    fav_projects = models.ManyToManyField(
        'FavProjects',
        blank=True,
        verbose_name='Избранные проекты'
    )

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        pass


class FavUsers(models.Model):
    fav_users = models.CharField(
        max_length=200,
        default='Отсутствует',
        verbose_name="Избранные пользователи"
    )

    def __str__(self):
        return self.fav_users

    class Meta:
        verbose_name = 'Избранный пользователь'
        verbose_name_plural = 'Избранные пользователи'


class PartProjects(models.Model):
    part_projects = models.CharField(
        max_length=200,
        default='Отсутствует',
        verbose_name="Проекты, в которых участвует"
    )

    def __str__(self):
        return self.part_projects

    class Meta:
        verbose_name = 'Проект, в котором участвует'
        verbose_name_plural = 'Проекты, в которых участвует'


class FavProjects(models.Model):
    fav_projects = models.CharField(
        max_length=200,
        default='Отсутствует',
        verbose_name="Избранные проекты"
    )

    def __str__(self):
        return self.fav_projects

    class Meta:
        verbose_name = 'Избранный проект'
        verbose_name_plural = 'Избранные проекты'


class Comment(models.Model):
    details = models.CharField(
        max_length=250,
        verbose_name='Текст комментария'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания комментария',
        default=now,
        editable=False
    )
    user_id = models.ForeignKey(
        'AdvUser',
        on_delete=models.SET_DEFAULT,
        default='Пользователь удалён',
        verbose_name='Пользователь, оставивший комментарий'
    )
    project_id = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        verbose_name='Проект, о котором оставлен комментарий'
    )
    project_html = models.URLField(
        max_length=150,
        blank=True,
        verbose_name='Ссылка на проект'
    )

    def __str__(self):
        return self.details

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название проекта'
    )
    description = models.CharField(
        max_length=50,
        verbose_name='Описание проекта'
    )
    technologies = models.ManyToManyField(
        'Technologies',
        blank=True,
        default='Отсутствуют',
        verbose_name='Используемые технологии'
    )
    contacts = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Контакты для связи с командой разработки'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания проекта',
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Последнее изменение'
    )
    project_logo = models.ImageField(
        upload_to='logos/%Y/%m/%d/',
        blank=True,
        verbose_name='Логотип(картинка) проекта')
    part_users = models.ManyToManyField(
        'PartUsers',
        blank=True,
        default='Отсутствуют',
        verbose_name='Участники проекта'
    )
    creator_project = models.ForeignKey(
        'AdvUser',
        verbose_name='Создатель проекта',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    def get_part_users(self):
        part_users_list = self.part_users.get_queryset()
        part_users_str = ''
        for part_user in part_users_list:
            part_users_str += ', ' + part_user.part_users
        return part_users_str.lstrip(', ')

    get_part_users.short_description = 'Пользователи-участники'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class PartUsers(models.Model):
    part_users = models.ManyToManyField(
        'AdvUser',
        default='Отсутствуют',
        verbose_name="Участники проекта"
    )
    role = models.ForeignKey(
        'Roles',
        blank=True,
        on_delete=models.PROTECT,
        verbose_name='Роль в проекте'
    )

    def __str__(self):
        return self.part_users, self.role

    class Meta:
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'


class Roles(models.Model):
    role = models.CharField(
        max_length=100,
        default='Участник',
        blank=True
    )

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователя'


class Technologies(models.Model):
    active_area = models.ManyToManyField(
        'ActiveArea',
        blank=True,
        default='Отсутствует',
        verbose_name='Сфера деятельности'
    )
    qualification = models.ManyToManyField(
        'Qualification',
        blank=True,
        default='Отсутствует',
        verbose_name='Квалификация'
    )
    prof_skills = models.ManyToManyField(
        'ProfSkills',
        blank=True,
        default='Отсутствуют',
        verbose_name='Профессиональные навыки'
    )

    def get_active_area(self):
        active_area_list = self.active_area.get_queryset()
        active_area_str = ''
        for tech in active_area_list:
            active_area_str += ', ' + tech.active_area
        return active_area_str.lstrip(', ')

    get_active_area.short_description = 'Сфера деятельности'

    def get_qualification(self):
        qualification_list = self.qualification.get_queryset()
        qualification_str = ''
        for tech in qualification_list:
            qualification_str += ', ' + tech.qualification
        return qualification_str.lstrip(', ')

    get_qualification.short_description = 'Квалификация'

    def get_prof_skills(self):
        prof_skills_list = self.prof_skills.get_queryset()
        prof_skills_str = ''
        for tech in prof_skills_list:
            prof_skills_str += ', ' + tech.prof_skills
        return prof_skills_str.lstrip(', ')

    get_prof_skills.short_description = 'Профессиональные навыки'

    class Meta:
        verbose_name = 'Технология программирования'
        verbose_name_plural = 'Технологии программирования'


class ActiveArea(models.Model):
    active_area = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Сфера деятельности'
    )

    def __str__(self):
        return self.active_area

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'


class Qualification(models.Model):
    qualification = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Квалификация'
    )

    def __str__(self):
        return self.qualification

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификации'


class ProfSkills(models.Model):
    prof_skills = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Профессиональный навык'
    )

    def __str__(self):
        return self.prof_skills

    class Meta:
        verbose_name = 'Профессиональный навык'
        verbose_name_plural = 'Профессиональные навыки'
