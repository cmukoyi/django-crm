# Add these imports at the top
import os
import sys
from pathlib import Path
from datetime import datetime as dt
from django.utils.translation import gettext_lazy as _

# ... keep your existing imports and settings until the static files section ...

# Replace your current static files section with this:

# Static files (CSS, JavaScript, Images) - FIXED CONFIGURATION
STATIC_URL = '/static/'  # Must have leading slash
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Different from source directory

# Static files directories for development
STATICFILES_DIRS = []
static_dir = BASE_DIR / 'static'
if static_dir.exists():
    STATICFILES_DIRS = [static_dir]

# Add WhiteNoise middleware for serving static files in production
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.utils.usermiddleware.UserMiddleware'
]

# WhiteNoise settings for production static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'  # Must have leading slash
MEDIA_ROOT = BASE_DIR / 'media'

# Production settings
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Security settings
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
