from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model"""
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['username']


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
