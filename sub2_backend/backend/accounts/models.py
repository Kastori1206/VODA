from django.contrib.auth.models import AbstractUser

# Create your models here.
#확장성 보장
class User(AbstractUser):
    pass