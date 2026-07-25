from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [("author", "Автор"), ("participant", "Участник")]

    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="participant",
                            verbose_name="Роль пользователя")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
