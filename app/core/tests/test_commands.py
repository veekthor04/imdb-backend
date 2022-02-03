from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class CommandTests(TestCase):

    def test_initadmin(self):
        """Test initial admin account was created"""
        call_command('initadmin')
        admin_accounts = User.objects.filter(is_superuser=True)
        self.assertTrue(admin_accounts.exists())
