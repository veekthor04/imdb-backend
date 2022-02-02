from django.db import models
from django.contrib.auth.models import AbstractUser

from core.tasks import send_registration_email_task


class User(AbstractUser):
    """Custom User model"""
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['username']
        
    def send_registration_email(self):
        """sends the a registration mail to the user"""
        return send_registration_email_task.delay(
            username=self.username,
            email = self.email,
        )


class Movie(models.Model):
    """Movie model"""
    title = models.CharField(max_length=100, db_index=True)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title',]
    

class UserMovieBookmark(models.Model):
    """User Movie Bookmark model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
    
    def __str__(self):
        return f'{self.user.username} bookmark'
