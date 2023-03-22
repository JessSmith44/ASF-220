"""
WSGI config for web_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os

import sys

import site

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')

application = get_wsgi_application()

# Add the app’s directory to the PYTHONPATH

sys.path.append('C:/Users/user/Desktop/charts_django/dashboard/Census_Dashboard/dashboard')

sys.path.append('C:/Users/myuser/Desktop/charts_django/dashboard/Census_Dashboard/dashboard/board')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dashboard.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')

application = get_wsgi_application()