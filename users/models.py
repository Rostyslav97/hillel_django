from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from shared.models import TimeStampMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **kwargs):
        if not email:
            raise ValueError("Email is required")
        if not password:
            raise ValueError("Password is required")
       
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username=None, password=None, **kwargs):
        superuser_payload = {
            "email": email,
            "username": username,
            "password": password,
            "is_superuser": True, 
            "is_staff": True, 
            "is_active": True,
        }
        return self.create_user(**superuser_payload)


class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    """Custom User model."""

    email = models.EmailField(db_index=True, unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True, unique=True)
    sex = models.BooleanField(null=True, blank=True, default=None)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_username(self):
        return self.email