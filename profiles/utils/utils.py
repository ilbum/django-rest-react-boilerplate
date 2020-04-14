from django.contrib.auth import get_user_model

from profiles.validators import validate_email_new, validate_username_new

USER = get_user_model()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# User creation methods
#   source: django.contrib.auth.UserManager
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def base_create_user(username, email, password, **extra_fields):
    """
    Create and save a user with the given username, email, and password.
    """
    # --- username validation
    if not username:
        raise ValueError('A username is required')
    validate_username_new(username)

    # --- email validation
    if not email:
        raise ValueError('An email required')
    validate_email_new(email)

    new_user = USER(username=username, email=email, **extra_fields)
    new_user.set_password(password)
    new_user.full_clean()
    new_user.save()
    return new_user


def create_user(username, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return base_create_user(username, email, password, **extra_fields)


def create_superuser(username, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
        raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')

    return base_create_user(username, email, password, **extra_fields)
