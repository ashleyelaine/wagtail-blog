# flake8: noqa

from .base import *
import os
from django.http import Http404


SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'


ROLLBAR = {
    'enabled': True,
    'access_token': os.environ.get('ROLLBAR_ACCESS_TOKEN'),
    'environment': os.environ.get('ROLLBAR_ENV', 'development' if DEBUG else 'production'),
    'branch': 'master' if os.environ.get('ROLLBAR_ENV') == 'production' else 'development',
    'root': BASE_DIR,
    'exception_level_filters': [
        (Http404, 'ignored'),
    ],
}
