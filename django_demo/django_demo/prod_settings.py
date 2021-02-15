from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p5abugunn)pry8q86t$p1sjiugxe$&=%-u+tm5+k!e_g+j1+*k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

ROOT_URLCONF = 'django_demo.urls'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
