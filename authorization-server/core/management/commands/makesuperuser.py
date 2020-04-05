import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create superuser unless it exists"

    def handle(self, *args, **options):
        username = os.environ['DJANGO_SUPERUSER_USERNAME']
        password = os.environ['DJANGO_SUPERUSER_PASSWORD']
        email = os.environ['DJANGO_SUPERUSER_EMAIL']

        User = get_user_model()
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
