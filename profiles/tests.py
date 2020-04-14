import re

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import Client, TestCase

from profiles.models import Profile
from profiles.utils import create_user
from profiles.validators import validate_email_change, validate_username_change

# tests here
