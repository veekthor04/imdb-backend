from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model"""
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['username']
