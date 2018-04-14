from __future__ import absolute_import, unicode_literals
import django_heroku
import os
from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

SECURE_SSL_REDIRECT = True

SENTRY_DSN = os.environ.get('SENTRY_DSN')
if SENTRY_DSN:
    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
        'release': os.environ.get('HEROKU_SLUG_COMMIT', ''),
    }


django_heroku.settings(locals())
