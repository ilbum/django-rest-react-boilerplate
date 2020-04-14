from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from profiles.validators import (validate_email_change, validate_name,
                                 validate_username_change)

# --- blank line: vscode auto sort issue ---


"""
---------------------------------------------------------
Profile
    'Profile' extends django's default 'User' model

    To modify the 'User':
        change_username(string_value)
        change_email(string_value)
        change_first_name(string_value)
        change_last_name(string_value)

    To create a 'User' use:
        profiles.utils.create_user
        profiles.utils.create_super_user

        # creates a profile for new 'User'
        profiles.signals.create_user_profile
---------------------------------------------------------
"""


class Profile(models.Model):
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # id & relationships fields
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    id = models.BigAutoField(
        primary_key=True,
    )
    # https://docs.djangoproject.com/en/3.0/ref/contrib/auth/
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True,
    )
    slug = models.SlugField(
        max_length=150,  # length of django default username
        unique=True,
        error_messages={'unique': 'That slug is already in use.'},
    )

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # decorators
    #   for displaying 'User' information
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def full_name(self):
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + ' ' + self.user.last_name
        elif self.user.first_name:
            return self.user.first_name
        elif self.user.last_name:
            return self.user.last_name
        else:
            return ''

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # methods & meta
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def change_username(self, new_username):
        self.user.username = validate_username_change(
            new_username,
            user=self.user
        )
        self.user.save()

    def change_password(self, new_password):
        self.user.set_password(new_password)
        self.user.full_clean()
        self.user.save()

    def change_email(self, new_email):
        self.user.email = validate_email_change(
            new_email,
            user=self.user
        )
        self.user.save()

    def change_first_name(self, new_first_name):
        validate_name(new_first_name)
        self.user.first_name = new_first_name
        self.user.save()

    def change_last_name(self, new_last_name):
        validate_name(new_last_name)
        self.user.last_name = new_last_name
        self.user.save()

    # --- django related
    def __str__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #     return reverse('profiles:profile-detail', kwargs={'slug': self.slug})

    # overriding save
    def save(self, *args, **kwargs):
        self.slug = str(self.username)
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['user']
