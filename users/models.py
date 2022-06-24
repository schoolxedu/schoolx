from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followed", blank=True)
    bio = models.TextField(blank=True, default="")
    avatar = models.ImageField(default='default.jpg', upload_to='avatars')
    cover_image = models.ImageField(default='cover.jpg', upload_to='avatars')

    def __str__(self):
        return f'{self.username}'
