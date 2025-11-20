from django.contrib.auth.models import AbstractUser
from django.db import models

class Gender(models.TextChoices):
    MALE = 'male'
    FEMALE = 'female'

class Member(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=Gender.choices, max_length=6,
                              default=Gender.MALE)
    age = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    show_closet = models.BooleanField(default=False)
    profile_image_url = models.URLField(max_length=300)
    follower_cnt = models.IntegerField(default=0)
    following_cnt = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'member'
        app_label = 'member'
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_user_email')
        ]

