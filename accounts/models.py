from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    ROLES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin')
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, choices=ROLES, default='user')
    description = models.TextField(blank=True, default='')
