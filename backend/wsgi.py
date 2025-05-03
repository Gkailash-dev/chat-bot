"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
path = '/home/kailash7dev/chatbot'
if path not in sys.path:
    sys.path.append(path)

# Set the environment variable for your Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

# Get the WSGI application for Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
