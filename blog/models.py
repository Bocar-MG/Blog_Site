import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    date_publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')

    published = PublishedManager()

    class Meta:
        ordering = ['-date_publish']
        indexes = [
            models.Index(fields=['-date_publish'])
        ]

    def __str__(self):
        return self.title
