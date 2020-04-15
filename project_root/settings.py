"""
INFORMATION:
    settings file created by django==3.0.3
"""

import os

# ---------------------------------------------------------
# Misc settings
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# change to below once settings module folder is made
# BASE_DIR = os.path.dirname(
#     os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$y%g_8(sass5-11zd4%!ys2q1z9_sn-3_a%b^-pq8=b+9ew%4y'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
]


# ---------------------------------------------------------
# Application settings
# ---------------------------------------------------------

INSTALLED_APPS = [
    # my apps
    # 'base',
    # 'profiles',

    # django defaults
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third party
    'rest_framework',
    'corsheaders',
    # 'django_s3_storage',
    # 'sslserver',

    # django forms - must be last
    'django.forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_root.urls'

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project_root.wsgi.application'

# ---------------------------------------------------------
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# ---------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# ---------------------------------------------------------
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
# ---------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]


# ---------------------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
# ---------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ---------------------------------------------------------
# django-rest-framework
# https://www.django-rest-framework.org/
# ---------------------------------------------------------

# Rest Settings ...


# ---------------------------------------------------------
# django-cors-headers
# https://github.com/adamchainz/django-cors-headers
# ---------------------------------------------------------

# for connection to react default server
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:3000',
]


# ---------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# ---------------------------------------------------------

STATIC_URL = '/static/'


# ---------------------------------------------------------
# Amazon Static
# ---------------------------------------------------------

# # --- File storage
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# # --- Authentication
# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''

# # --- Bucket information
# S3_BUCKET = ''

# STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"

# AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET

# STATIC_URL = "https://%s.s3.amazonaws.com/" % S3_BUCKET

# # --- Other settings
# AWS_S3_MAX_AGE_SECONDS_STATIC = "94608000"
