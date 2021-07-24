from ._base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WEBSITE_URL = "http://127.0.0.1:8000"  # without trailing slash

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },

    # 'mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': get_secret('DATABASE_NAME'),
    #     'USER': get_secret('DATABASE_USER'),
    #     'PASSWORD': get_secret('DATABASE_PASSWORD'),
    #     'HOST': get_secret('DATABASE_HOST'),
    #     'PORT': get_secret('DATABASE_PORT'),
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     }
    # },

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': get_secret('DATABASE_NAME'),
    #     'USER': get_secret('DATABASE_USER'),
    #     'PASSWORD': get_secret('DATABASE_PASSWORD'),
    #     'HOST': 'db',
    #     # 'PORT': int(get_secret('DATABASE_PORT')),
    #     'PORT': 5432,
    # }
}

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# ROOT_URLCONF = f'{PROJECT_NAME}.urls'

try:
    from .local import *
except ImportError:
    pass
