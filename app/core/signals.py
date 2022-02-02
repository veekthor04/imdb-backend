from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import User, UserMovieBookmark


@receiver(post_save, sender=User)
def post_save_user_created_receiver(sender, instance: User, created, **kwargs):
    """
    Sends email when a user is created and create a user movie bookmark model
    """
    if created:

        # creates user bookmark on user creation
        UserMovieBookmark.objects.create(user=instance)
        print('sending email...')
