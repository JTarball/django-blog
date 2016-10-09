#!/usr/bin/env python
"""
    Configuration for py.test (in place of manage.py)
"""
import os

from django.conf import settings

from django_blog.tests import settings as test_settings


def pytest_configure():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.tests.settings')
    settings.configure(default_settings=test_settings)
