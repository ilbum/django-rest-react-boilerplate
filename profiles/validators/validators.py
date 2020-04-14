import re
import unicodedata

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# from profiles.validators.banned_words ...

USER = get_user_model()

acceptable_name_characters = r'^[a-zA-Z0-9\s\w,.\']+$'
acceptable_username_characters = r'^[a-zA-Z0-9]+$'
message_name_characters = 'Invalid characters in name. Please remove special.'\
                          ' characters from name.'
message_email_characters = 'Invalid email, please review'
message_email_duplicate = 'Email already exists. Please try a different email.'
message_username_characters = 'Invalid characters in username. Permitted ' \
                             'characters: A-Z, a-z, and 0-9'
message_username_duplicate = 'Username already exists. Please try a ' \
                             'different username.'
message_username_offensive = 'Username invalid, please try a different ' \
                             'username.'


# ---------------------------------------------------------
# validate first_name, last_name function
# ---------------------------------------------------------

def validate_name(value):
    """
    Use for 'first_name' and 'last_name'
    value: string
    """
    # check if characters are valid
    if not re.match(acceptable_name_characters, value):
        raise ValidationError(
            message_name_characters
        )
    # passed characters validation tests
    else:
        return value


# ---------------------------------------------------------
# validate username functions
# ---------------------------------------------------------

def base_validate_username(value):
    """
    value: string
    """
    # check if characters are valid
    if not re.match(acceptable_username_characters, value):
        raise ValidationError(
            message_username_characters
        )
    # passed characters validation tests
    else:
        value = normalize_username(value)
        check_for_offensive_username(value)
        return value


def validate_username_new(value):
    """
    value: string
    """
    # check if duplicate user exists
    if USER.objects.filter(username__iexact=value):
        raise ValidationError(message_username_duplicate)
    else:
        return base_validate_username(value)


def validate_username_change(new_username, user):
    """
    new_username: string
        new username string
    user: django user object
        it users to exclude it when searching for duplicates
        This should be a signal, when you modify the Profile
    """
    # check if duplicate user exists, exclude user in arguments
    if USER.objects.filter(username__iexact=new_username).exclude(
                           id=user.id):
        raise ValidationError(message_username_duplicate)
    else:
        return base_validate_username(new_username)


# ---------------------------------------------------------
# validate email functions
# ---------------------------------------------------------

def base_validate_email(value):
    """
    value: string
    """
    if not re.match(r'[^@]+@[^@]+\.[^@]+', value):
        raise ValidationError(message_email_characters)
    else:
        value = normalize_email(value)
        return value


def validate_email_new(value):
    """
    value: string
    """
    # check if duplicate user exists
    if USER.objects.filter(email__iexact=value):
        raise ValidationError(message_email_duplicate)
    else:
        return base_validate_email(value)


def validate_email_change(new_email, user):
    """
    new_email: string
        new email string
    user: django user object
        it users to exclude it when searching for duplicates
        This should be a signal, when you modify the Profile
    """
    # check if duplicate user exists, exclude user in arguments
    if USER.objects.filter(email__iexact=new_email).exclude(
                           id=user.id):
        raise ValidationError(message_email_duplicate)
    else:
        return base_validate_email(new_email)


# ---------------------------------------------------------
# BaseUserManager functions
#   source: django.contrib.auth.base_user.BaseUserManager
# ---------------------------------------------------------

def normalize_email(email):
    """
    Normalize the email address by lowercasing the domain part of it.
    """
    email = email or ''
    try:
        email_name, domain_part = email.strip().rsplit('@', 1)
    except ValueError:
        pass
    else:
        email = email_name + '@' + domain_part.lower()
    return email


def normalize_username(username):
    return unicodedata.normalize('NFKC', username) \
        if isinstance(username, str) else username


# ---------------------------------------------------------
# misc. methods
# ---------------------------------------------------------

def check_for_offensive_username(value):
    """
    value: string
    """
    # TODO(ilbum): add banned words
    pass
    # # Check the banned_word_list, lowercase
    # value_lower = value.lower()
    # for offensive_word in banned_word_list:
    #     if re.search(offensive_word, value_lower):
    #         # write a log regarding the offensive word
    #         raise ValidationError(message_username_offensive)
