# flake8: noqa

from .local import *


INSTALLED_APPS += ('behave_django',)
TEST_RUNNER = 'rainbowtests.test.runner.RainbowDiscoverRunner'
