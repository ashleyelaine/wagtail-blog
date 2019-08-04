# flake8: noqa

from .production import *
import os
import dj_database_url
from storages.backends.s3boto3 import S3Boto3Storage


INSTALLED_APPS = ('collectfast', ) + INSTALLED_APPS + ('django_ses',)

###################
# MAIN AWS SETTINGS
###################

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_ACL = None

####
# S3
####

AWS_S3_SECURE_URLS = os.environ.get('S3_SECURE_URLS', '1') == '1'
AWS_S3_USE_SSL = AWS_S3_SECURE_URLS
AWS_S3_URL_PROTOCOL = 'https:' if AWS_S3_SECURE_URLS else 'http:'
AWS_S3_REGION_NAME = 'us-east-2'
AWS_S3_SIGNATURE_VERSION = 's3v4'

CACHES['collectfast'] = {
    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    'LOCATION': 'collectfast',
}

COLLECTFAST_CACHE = 'collectfast'

STATIC_URL = '/assets/'
MEDIA_URL = '/uploads/'


class StaticStorage(S3Boto3Storage):
    querystring_auth = False
    bucket_name = '%s-assets' % os.environ.get('S3_BUCKET_NAME')
    preload_metadata = True


class MediaStorage(S3Boto3Storage):
    bucket_name = '%s-media' % os.environ.get('S3_BUCKET_NAME')
    default_acl = 'public-read'
    querystring_auth = False


DEFAULT_FILE_STORAGE = 'core.settings.aws.MediaStorage'
STATICFILES_STORAGE = 'core.settings.aws.StaticStorage'

#####
# SES
#####

EMAIL_BACKEND = 'django_ses.SESBackend'

#####
# RDS
#####

_database = dj_database_url.config()
if not _database:
    _database = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('RDS_DB_NAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'PORT': os.environ.get('RDS_PORT'),
    }
DATABASES = {'default': _database}
