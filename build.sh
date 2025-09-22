#!/usr/bin/env bash
set -o errexit

echo "=== Starting Django CRM Build Process ==="

echo "1. Installing Python dependencies..."
pip install -r requirements.txt

echo "2. Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "3. Running database migrations..."
python manage.py migrate

echo "4. Creating admin user..."
python manage.py shell -c "
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

username = 'admin'
email = 'admin@visightsolutions.co.za'
password = 'changeme123'

if User.objects.filter(username=username).exists():
    user = User.objects.get(username=username)
    print(f'Admin user \"{username}\" already exists')
    # Verify password works
    if check_password(password, user.password):
        print('Password verification: PASS')
    else:
        print('Password verification: FAIL - updating password')
        user.set_password(password)
        user.save()
        print('Password updated successfully')
else:
    user = User.objects.create_superuser(username, email, password)
    print(f'Created admin user: {username}')
    print(f'Email: {email}')
    print('Password verification: PASS')

print(f'Login credentials: {username} / {password}')
"

echo "=== Build completed successfully! ==="
echo "Admin login: https://django-crm-605v.onrender.com/en/456-admin/"
echo "CRM access: https://django-crm-605v.onrender.com/en/123/"
