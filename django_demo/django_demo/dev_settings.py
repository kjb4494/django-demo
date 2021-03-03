from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p5abugunn)pry8q86t$p1sjiugxe$&=%-u+tm5+k!e_g+j1+*k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'django_demo.urls'

INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug_formatter': {
            'format': '[%(levelname)s][%(pathname)s:%(funcName)s():%(lineno)d][%(asctime)s] "%(message)s"',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'debug_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'debug_formatter',
        }
    },
    'loggers': {
        'debug': {
            'level': 'DEBUG',
            'handlers': ['debug_console']
        },
    },
}
