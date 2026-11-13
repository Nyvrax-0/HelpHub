from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователь сайта. Это обычный Django-пользователь + роль, город и телефон."""

    class Role(models.TextChoices):
        VOLUNTEER = "volunteer", "Волонтёр"
        NGO = "ngo", "НКО"

    email = models.EmailField("Email", unique=True)
    role = models.CharField("Роль", max_length=20, choices=Role.choices, default=Role.VOLUNTEER)
    city = models.CharField("Город", max_length=100, blank=True)
    phone = models.CharField("Телефон", max_length=30, blank=True)

    @property
    def is_volunteer(self):
        return self.role == self.Role.VOLUNTEER

    @property
    def is_ngo(self):
        return self.role == self.Role.NGO

    def __str__(self):
        return self.username
