from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.utils import timezone
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        """Create and save a new superuser"""
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True')

        return self.create_user(email, first_name, last_name, password, **other_fields)

    def create_user(self, email, first_name, last_name, password=None, **other_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

genderChoice = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('Prefer not to say', 'Prefer Not to Respond'),
)

class CustomUser(AbstractBaseUser):
    """Custom user model that support using email instead of username"""
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    gender = models.CharField(max_length=100, choices=genderChoice)
    telephone = models.CharField(max_length=20, null=False, blank=False)
    spot = models.ForeignKey("api.Spots", on_delete=models.CASCADE, related_name="collector_spot", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_Label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)