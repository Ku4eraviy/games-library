from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя с дополнительными полями."""
    full_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Полное имя'
    )
    phone = models.CharField(
        max_length=16,
        blank=True,
        verbose_name='Телефон'
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Email'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
