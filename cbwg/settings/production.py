from __future__ import absolute_import, unicode_literals
import dj_database_url
import os
from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ["SECRET_KEY"]

if "DATABASE_URL" in os.environ:
    # Configure Django for DATABASE_URL environment variable.
    DATABASES["default"] = dj_database_url.config(conn_max_age=600)

# SECURE_SSL_REDIRECT = True

SENTRY_DSN = os.environ.get('SENTRY_DSN')
if SENTRY_DSN:
    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
        'release': os.environ.get('HEROKU_SLUG_COMMIT', ''),
    }
