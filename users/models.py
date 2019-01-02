from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_clinician = models.BooleanField(default=False)


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Clinician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
