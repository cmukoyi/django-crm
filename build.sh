#!/usr/bin/env bash
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate

echo "Creating/updating admin user..."
python manage.py shell -c "
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

username = 'admin'
password = 'admin123'
email = 'admin@visightsolutions.co.za'

try:
    user = User.objects.get(username=username)
    print(f'User {username} exists - checking password...')
    
    if check_password(password, user.password):
        print('Password is correct')
    else:
        print('Password is wrong - updating it...')
        user.set_password(password)
        user.save()
        print('Password updated successfully')
        
except User.DoesNotExist:
    user = User.objects.create_superuser(username, email, password)
    print(f'Created new superuser: {username}')

print('=== LOGIN CREDENTIALS ===')
print(f'Username: {username}')
print(f'Password: {password}')
print(f'URL: https://django-crm-605v.onrender.com/en/456-admin/')
"

echo "Build completed!"
