from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .validators import validate_phone
from .managers import UserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, validators=[validate_phone])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['name', 'last_name', 'phone_number']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user_profile'

    def __str__(self):
        return f"{self.name} {self.last_name}"


class UserHealthInfo(models.Model):

    GENDER_CHOICES = [
        ('male', 'مرد'),
        ('female', 'زن'),
    ]
    ECONOMIC_STATUS_CHOICES = [
        ('very low', 'خیلی بد'),
        ('low', ' بد'),
        ('medium', 'متوسط'),
        ('high', 'خوب'),
        ('very high', 'خیلی خوب'),
    ]

    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='wellness_profile')
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    sleep_hours = models.CharField(help_text="Average sleep hours per day")
    economic_status = models.CharField(max_length=10, choices=ECONOMIC_STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User Health Info'
        verbose_name_plural = 'Users Health Info'
        db_table = 'user_health_info'

    def __str__(self):
        return f"Health {self.user.name}"


class UserTrustedContact(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='trusted_contact')
    trusted_name = models.CharField(max_length=30)
    trusted_lastname = models.CharField(max_length=30)
    trusted_phone_number = models.CharField(
        max_length=11,
        validators=[validate_phone],
    )

    class Meta:
        verbose_name = 'Trusted Contact'
        verbose_name_plural = 'Trusted Contacts'
        db_table = 'user_trusted_contacts'

    def __str__(self):
        return f"{self.trusted_name} {self.trusted_lastname} (Contact {self.user.name})"

