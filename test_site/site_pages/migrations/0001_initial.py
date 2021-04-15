# Generated by Django 3.1.7 on 2021-04-15 14:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='Пароль')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Последний актив')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='Суперпользователь')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Персонал')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Активный')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации')),
                ('prof_pic', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Аватарка')),
                ('github_url', models.URLField(blank=True, max_length=150, verbose_name='Ссылка на GitHub')),
                ('gitlab_url', models.URLField(blank=True, max_length=150, verbose_name='Ссылка на GitLab')),
                ('vk_url', models.URLField(blank=True, max_length=150, verbose_name='Ссылка на VK')),
                ('part_projects', models.CharField(blank=True, max_length=300, verbose_name='Проекты, в которых участвует')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ActiveArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_area', models.CharField(blank=True, max_length=100, verbose_name='Сфера деятельности')),
            ],
            options={
                'verbose_name': 'Сфера деятельности',
                'verbose_name_plural': 'Сферы деятельности',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=250, verbose_name='Текст комментария')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания комментария')),
                ('project_html', models.URLField(blank=True, max_length=150, verbose_name='Ссылка на проект')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='ProfSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_skills', models.CharField(blank=True, max_length=100, verbose_name='Профессиональный навык')),
            ],
            options={
                'verbose_name': 'Профессиональный навык',
                'verbose_name_plural': 'Профессиональные навыки',
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(blank=True, max_length=100, verbose_name='Квалификация')),
            ],
            options={
                'verbose_name': 'Квалификация',
                'verbose_name_plural': 'Квалификации',
            },
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_area', models.ManyToManyField(blank=True, default='Отсутствует', to='site_pages.ActiveArea', verbose_name='Сфера деятельности')),
                ('prof_skills', models.ManyToManyField(blank=True, default='Отсутствуют', to='site_pages.ProfSkills', verbose_name='Профессиональные навыки')),
                ('qualification', models.ManyToManyField(blank=True, default='Отсутствует', to='site_pages.Qualification', verbose_name='Квалификация')),
            ],
            options={
                'verbose_name': 'Технология программирования',
                'verbose_name_plural': 'Технологии программирования',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', models.CharField(max_length=50, verbose_name='Описание проекта')),
                ('contacts', models.CharField(blank=True, max_length=100, verbose_name='Контакты для связи с командой разработки')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания проекта')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее изменение')),
                ('project_logo', models.ImageField(blank=True, upload_to='logos/%Y/%m/%d/', verbose_name='Логотип(картинка) проекта')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='site_pages.comment', verbose_name='Комментарии')),
                ('creator_project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_creator_project', to=settings.AUTH_USER_MODEL, verbose_name='Создатель проекта')),
                ('part_users', models.ManyToManyField(blank=True, related_name='_project_part_users_+', to=settings.AUTH_USER_MODEL, verbose_name='Участники проекта')),
                ('technologies', models.ManyToManyField(blank=True, default='Отсутствуют', to='site_pages.Technologies', verbose_name='Используемые технологии')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'unique_together': {('creator_project',)},
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_pages.project', verbose_name='Проект, о котором оставлен комментарий'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, оставивший комментарий'),
        ),
        migrations.AddField(
            model_name='user',
            name='fav_projects',
            field=models.ManyToManyField(blank=True, to='site_pages.Project', verbose_name='Избранные проекты'),
        ),
        migrations.AddField(
            model_name='user',
            name='fav_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Избранные пользователи'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='job_desc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='site_pages.technologies', verbose_name='Возможности работы'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
