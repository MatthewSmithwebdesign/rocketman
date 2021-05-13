import os
from .base import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['localhost', 'rocket.matthewsmithwebdesign.com', ]

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES ={
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'rocketman',
        "USER": 'rocketman',
        "PASSWORD":  os.environ['PASSWORD'],
        "HOST": 'localhost',
        "PORT": "",
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://eab2a256b2b24fdc9ee5fb2aefed693f@o637168.ingest.sentry.io/5757792",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
try:
    from .local import *
except ImportError:
    pass
