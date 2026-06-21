from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):

    help = "Create admin user"

    def handle(self, *args, **kwargs):

        username = "admin"
        password = "admin12345"
        email = "admin@gmail.com"


        if not User.objects.filter(username=username).exists():

            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )

            self.stdout.write(
                "Admin created successfully"
            )

        else:

            self.stdout.write(
                "Admin already exists"
            )