#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    default_env = 'test' if len(sys.argv) > 1 and sys.argv[1] == 'test' else 'local'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.%s' % default_env)

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
