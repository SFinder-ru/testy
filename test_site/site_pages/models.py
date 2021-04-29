from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    prof_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True,
                                 verbose_name='Аватарка')
    github_url = models.URLField(max_length=150, blank=True,
                                 verbose_name='Ссылка на GitHub')
    gitlab_url = models.URLField(max_length=150, blank=True,
                                 verbose_name='Ссылка на GitLab')
    vk_url = models.URLField(max_length=150, blank=True,
                             verbose_name='Ссылка на VK')
    fav_users = models.ManyToManyField('User', blank=True, related_name='user_favourites',
                                       verbose_name='Избранные пользователи')
    part_projects = models.ManyToManyField('Project', blank=True, related_name='project_participates',
                                           verbose_name='Проекты, в которых участвует')
    fav_projects = models.ManyToManyField('Project', blank=True, related_name='project_favourites',
                                          verbose_name='Избранные проекты')
    job_desc = models.ForeignKey('Technologies', blank=True, on_delete=models.CASCADE,
                                 null=True, verbose_name='Возможности работы')

    def __str__(self):
        return self.username

    def get_all_users(self):
        all_users_list = User.objects.all()
        all_users_str = ''
        for user in all_users_list:
            all_users_str += ', ' + user.username
        return all_users_str.lstrip(', ')

    get_all_users.short_description = 'Список всех пользователей'

    def get_fav_users(self):
        fav_users_list = self.fav_users.get_queryset()
        fav_users_str = ''
        for user in fav_users_list:
            fav_users_str += ', ' + user.username
        return fav_users_str.lstrip(', ')

    get_fav_users.short_description = 'Список избранных пользователей'

    def get_part_projects(self):
        all_projects_list = self.part_projects.get_queryset()
        part_projects_str = ''
        for project in all_projects_list:
            part_projects_str += ', ' + project.name
        return part_projects_str.lstrip(', ')

    get_part_projects.short_description = 'Список проектов участия'

    def get_fav_projects(self):
        fav_projects_list = self.fav_projects.get_queryset()
        fav_projects_str = ''
        for project in fav_projects_list:
            fav_projects_str += ', ' + project.name
        return fav_projects_str.lstrip(', ')

    get_fav_projects.short_description = 'Список избранных проектов'

    class Meta(AbstractUser.Meta):
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Comment(models.Model):
    details = models.CharField(max_length=250,
                               verbose_name='Текст комментария')
    created_at = models.DateTimeField(verbose_name='Дата создания комментария',
                                      default=now, editable=False)
    user_name = models.ForeignKey('User', on_delete=models.SET_DEFAULT,
                                  default='0',
                                  verbose_name='Пользователь, оставивший комментарий')
    project_name = models.ForeignKey('Project', on_delete=models.CASCADE,
                                     verbose_name='Проект, о котором оставлен комментарий')
    project_html = models.URLField(max_length=150, blank=True,
                                   verbose_name='Ссылка на проект')

    def __str__(self):
        return self.details

    def get_all_comments(self):
        all_comments_list = Comment.objects.all()
        all_comments_str = ''
        for comment in all_comments_list:
            all_comments_str += ', ' + comment.details
        return all_comments_str.lstrip(', ')

    get_all_comments.short_description = 'Список всех комментариев'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Project(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название проекта')
    description = models.CharField(max_length=50,
                                   verbose_name='Описание проекта')
    technologies = models.ManyToManyField('Technologies', blank=True,
                                          default='Отсутствуют',
                                          verbose_name='Используемые технологии')
    contacts = models.CharField(max_length=100, blank=True,
                                verbose_name='Контакты для связи с '
                                             'командой разработки')
    created_at = models.DateTimeField(verbose_name='Дата создания проекта',
                                      default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Последнее изменение')
    project_logo = models.ImageField(upload_to='logos/%Y/%m/%d/', blank=True,
                                     verbose_name='Логотип(картинка) проекта')
    part_users = models.ManyToManyField('User', blank=True, related_name='+',
                                        verbose_name='Участники проекта')
    creators = models.ManyToManyField('User', verbose_name='Создатели проекта',
                                      related_name='project_creator_project')
    comments = models.ManyToManyField('Comment', verbose_name='Комментарии', blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный')

    def __str__(self):
        return self.name

    def get_part_users(self):
        part_users_list = self.part_users.get_queryset()
        part_users_str = ''
        for user in part_users_list:
            part_users_str += ', ' + user.username
        return part_users_str.lstrip(', ')

    get_part_users.short_description = 'Пользователи-участники'

    def get_creators(self):
        creators_list = self.creators.get_queryset()
        creators_str = ''
        for creator in creators_list:
            creators_str += ', ' + creator.username
        return creators_str.lstrip(', ')

    get_creators.short_description = 'Создатели проекта'

    def get_comments(self):
        all_comments_list = Comment.objects.all()
        all_comments_str = ''
        for comment in all_comments_list:
            if comment.project_name == self.name:
                all_comments_str += ', ' + comment.project_name
        return all_comments_str.lstrip(', ')

    get_comments.short_description = 'Список всех комментариев проекта'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Technologies(models.Model):
    active_area = models.ManyToManyField('ActiveArea', blank=True,
                                         default='Отсутствует',
                                         verbose_name='Сфера деятельности')
    qualification = models.ManyToManyField('Qualification', blank=True,
                                           default='Отсутствует',
                                           verbose_name='Квалификация')
    prof_skills = models.ManyToManyField('ProfSkills', blank=True,
                                         default='Отсутствуют',
                                         verbose_name='Профессиональные навыки')

    def __str__(self):
        return self.get_active_area() + ', ' + self.get_qualification() + ', ' + self.get_prof_skills()

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
    active_area = models.CharField(max_length=100, blank=True,
                                   verbose_name='Сфера деятельности')

    def __str__(self):
        return self.active_area

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'


class Qualification(models.Model):
    qualification = models.CharField(max_length=100, blank=True,
                                     verbose_name='Квалификация')

    def __str__(self):
        return self.qualification

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификации'


class ProfSkills(models.Model):
    prof_skills = models.CharField(max_length=100, blank=True,
                                   verbose_name='Профессиональный навык')

    def __str__(self):
        return self.prof_skills

    class Meta:
        verbose_name = 'Профессиональный навык'
        verbose_name_plural = 'Профессиональные навыки'

# Create your models here.
