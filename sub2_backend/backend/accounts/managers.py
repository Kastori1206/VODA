from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    # def create_user(self, email, password, **extra_fields):
    #     """
    #     Create and save a User with the given email and password.
    #     """
    #     if not email:
    #         raise ValueError(_('The Email must be set'))
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save()
    #     return user

    # def create_superuser(self, email, password, **extra_fields):
    #     """
    #     Create and save a SuperUser with the given email and password.
    #     """
    #     # extra_fields.setdefault('is_staff', True)
    #     # extra_fields.setdefault('is_superuser', True)
    #     # extra_fields.setdefault('is_active', True)

    #     # if extra_fields.get('is_staff') is not True:
    #     #     raise ValueError(_('Superuser must have is_staff=True.'))
    #     # if extra_fields.get('is_superuser') is not True:
    #     #     raise ValueError(_('Superuser must have is_superuser=True.'))
    #     return self.create_user(email, password, **extra_fields)
    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('이메일은 필수입니다.')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password, **kwargs):
        """
        일반 유저 생성
        """
        kwargs.setdefault('is_admin', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        """
        관리자 유저 생성
        """
        kwargs.setdefault('is_admin', True)
        return self._create_user(email, password, **kwargs)
