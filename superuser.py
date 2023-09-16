import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_portfolio.settings')
django.setup()

from django.contrib.auth.models import User

# Crea el superusuario
User.objects.create_superuser(username='danielcedeno', email='daniel@gmail.com', password='Daniel_2003')
