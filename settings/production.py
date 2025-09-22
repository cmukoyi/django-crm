import os
import dj_database_url
from .base import *

# Production settings
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://localhost/djangocrm',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Allowed hosts
ALLOWED_HOSTS = ['*']

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Middleware for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
] + MIDDLEWARE

# Security settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
