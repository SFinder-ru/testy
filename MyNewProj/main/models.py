from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(
        default=True,
        db_index=True,
        verbose_name='Прошел активацию?'
    )
    vk_link = models.URLField(
        max_length=150,
        blank=True,
        verbose_name='Ссылка на вк'
    )

    """notifications = models.BooleanField(
        default=True,
        verbose_name='Слать оповещения?')"""

    class Meta(AbstractUser.Meta):
        pass


