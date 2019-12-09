from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
import datetime
import re


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year)]


def current_year():
    return datetime.date.today().year


class AlumniAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not re.search(".*@iitg\.ac\.in", email):
            raise ValueError("Must be an iitg email, example: abc@iitg.ac.in")

        user = self.model(
            email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Alumni(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    #username = models.CharField(max_length=30, unique=True)
    #password = models.CharField(max_length=30)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(
        verbose_name="last joined", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics')

    graduation_year = models.IntegerField(
        choices=year_choices(), default=current_year)
    contact_number = PhoneNumberField()
    current_job = models.CharField(max_length=100)
    linkedin_url = models.URLField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AlumniAccountManager()

    def __str__(self):
        return '{self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
