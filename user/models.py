from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager



class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatarka/', verbose_name='аватарка', blank=True, null=True)
    phone = models.CharField(max_length=50, verbose_name='номер телефона', unique=True)
    address = models.CharField(max_length=50, verbose_name='адрес', blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone