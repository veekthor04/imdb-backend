from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


username = settings.ADMIN_USERNAME
email = settings.ADMIN_EMAIL
password = settings.ADMIN_PASSWORD

User = get_user_model()


class Command(BaseCommand):
    """Creates a new superuser account if no super user account exist"""

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).count() == 0:
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(
                email=email,
                username=username,
                password=password
            )
            admin.is_active = True
            admin.is_admin = True
            admin.user_type = 'super_admin'
            admin.save()
        else:
            print('Admin accounts can only be initialized if no '
                  'Super User Account exist')
