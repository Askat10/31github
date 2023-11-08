from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(max_length=24, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=10, blank=True)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
