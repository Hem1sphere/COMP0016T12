from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Developer, Clinician


class DeveloperRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)  # commit set to False to return object not saved to db yet
        user.is_developer = True
        user.save()
        developer = Developer.objects.create(user=user)
        return user


class ClinicianRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_clinician = True
        if commit:
            user.save()
        return user
