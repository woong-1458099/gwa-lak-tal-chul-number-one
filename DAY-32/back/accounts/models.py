from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

    nickname = models.CharField(
        max_length=30,
        unique=True,
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=(
            ('M', '남성'),
            ('F', '여성'),
            ('O', '기타'),
        ),
        blank=True
    )

    age = models.PositiveSmallIntegerField(null=True, blank=True)



class Theme(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class UserPreference(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    themes = models.ManyToManyField(
        Theme,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}의 취향"

