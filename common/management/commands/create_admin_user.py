from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@visightsolutions.co.za'
        password = 'changeme123'
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(f'Created admin user: {username}')
            self.stdout.write(f'Email: {email}')
            self.stdout.write(f'Password: {password}')
        else:
            self.stdout.write(f'Admin user {username} already exists')
