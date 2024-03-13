from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        check_admin = User.objects.filter(username='admin')

        if not check_admin:
            admin = User.objects.create(
                username='admin',
                is_superuser=True,
                is_staff=True,
                is_active=True
            )
            admin.set_password('12345')
            admin.save()

        user = User.objects.create(
            username='user',
            is_superuser=False,
            is_staff=True,
            is_active=False
        )
        user.set_password('12345')
        user.save()
