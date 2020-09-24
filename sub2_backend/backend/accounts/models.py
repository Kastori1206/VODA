from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#확장성 보장
class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField('이메일', unique=True)
    password = models.CharField('비밀번호', max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_RIELDS = []

    objects = UserManager()