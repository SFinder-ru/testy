# Generated by Django 3.1.7 on 2021-03-18 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]