from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from core.models import User, UserMovieBookmark, Movie


@receiver(post_save, sender=User)
def post_save_user_created_receiver(sender, instance: User, created, **kwargs):
    """
    Sends email when a user is created and create a user movie bookmark model
    Also, clears user_queryset cache
    """
    if created:

        # creates user bookmark on user creation
        UserMovieBookmark.objects.create(user=instance)

        instance.send_registration_email()  # send mail
    
    cache.delete('user_queryset')  # clear user queryset cache


@receiver(post_save, sender=Movie)
def post_save_user_created_receiver(sender, instance: Movie, created, **kwargs):
    """
    clears movie_queryset cache
    """
    cache.delete('movie_queryset')  # clear movie queryset cache
