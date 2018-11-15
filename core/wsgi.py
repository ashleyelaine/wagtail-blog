"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

sys.path.insert(0, '/opt/python/current/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.local')
application = Cling(get_wsgi_application())
