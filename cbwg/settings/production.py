from __future__ import absolute_import, unicode_literals
import django_heroku
from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

django_heroku.settings(locals())
