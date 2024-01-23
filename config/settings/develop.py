from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

ENCRYPT_KEY = b'AIHl3YFL63GrufwMK8ANqI1mvHgh_J-XD3Zc-LcZB_E='

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "UPDATE_LAST_LOGIN": True,
}

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
