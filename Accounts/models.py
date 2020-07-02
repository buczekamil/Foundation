from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['first_name', 'last_name']

