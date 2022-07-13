from ctypes import addressof
from pydoc import describe
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from registration.models import ProjectRegistration


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

        user.is_staff = True if user.user_type == 'admin' else False
        user.is_superuser = True if user.user_type == 'admin' else False
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        # extra_fields.setdefault('is_superuser', True)

        extra_fields.setdefault('name', 'administrator')
        extra_fields.setdefault('phone', '0000-0000')
        extra_fields.setdefault('address', 'VietNam')
        extra_fields.setdefault('user_type','admin')
        extra_fields.setdefault('note', '')

        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class ProjectUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email address', max_length=255, unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)

    status_choices = [
        ('activate','Activate'),
        ('lock','Lock'),
    ]
    status = models.CharField(max_length=15,choices=status_choices,default='Activate')

    user_type_choices = [
        ('token_distributor','Token distributor'),
        ('pools_owner','Pools owner'),
        ('admin','Admin'),
    ]

    user_type = models.CharField(max_length=20,choices=user_type_choices, default='Token distributor')
    project = models.ForeignKey(ProjectRegistration, on_delete=models.CASCADE, blank=True, null=True)

    note = models.CharField(max_length=200, default=None, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ProjectUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    # @property
    def is_staff(self):
        if self.user_type == 'admin':
            return True
        return False

# class MatchingProjectPool(models.Model):
#     project = models.ForeignKey(ProjectRegis, on_delete=models.CASCADE)
#     pool = models.ForeignKey(PoolRegis, on_delete=models.CASCADE)
#     start_time = models.DateTimeField(default=datetime.now(), blank=False)
#     end_time = models.DateTimeField(default = datetime.now() + relativedelta(month=6), blank=False)