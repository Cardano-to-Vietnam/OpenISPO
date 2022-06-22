from ctypes import addressof
from pydoc import describe
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProjectUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class ProjectUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)

    status_choices = [
        ('registered','registered'),
        ('activate','activate'),
        ('lock','lock'),
    ]
    status = models.CharField(max_length=15,choices=status_choices,default='registered')

    user_type_choices = [
        ('token_distributor','token_distributor'),
        ('pools_owner','pools_owner'),
        ('deligated_users','deligated_users'),
    ]

    user_type = models.CharField(max_length=20,choices=user_type_choices,default='deligated_users')

    note = models.CharField(max_length=200)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProjectUserManager()

    def __str__(self):
        return self.email


class PoolRegis(models.Model):
    name = name = models.CharField(max_length=100)
    pool_addr = models.CharField(max_length=200)
    user_owner = models.OneToOneField(ProjectUser, on_delete=models.CASCADE)
    disclaimer = models.OneToOneField(Disclaimer, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
