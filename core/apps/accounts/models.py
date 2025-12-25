from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, role='USER', first_name='', last_name=''):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            role=role, 
            first_name=first_name, 
            last_name=last_name)
        user.set_password(password)
        user.save()
        return user 

    def create_superuser(self, email, password, first_name='', last_name=''):
        user = self.create_user(
            email, 
            password, 
            role='ADMIN', 
            first_name=first_name, 
            last_name=last_name)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('USER', 'User'),
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)   

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} {self.last_name} {self.first_name}"