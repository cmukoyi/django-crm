#!/usr/bin/env bash
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Creating admin user..."
python manage.py shell -c "
from django.contrib.auth.models import User
username = 'admin'
password = 'admin123'
email = 'admin@visightsolutions.co.za'

if User.objects.filter(username=username).exists():
    print(f'User {username} already exists')
else:
    user = User.objects.create_superuser(username, email, password)
    print(f'Created superuser: {username} with password: {password}')

print('=== LOGIN CREDENTIALS ===')
print(f'Username: {username}')
print(f'Password: {password}')
print(f'URL: https://django-crm-605v.onrender.com/en/456-admin/')
"

echo "Build completed!"
