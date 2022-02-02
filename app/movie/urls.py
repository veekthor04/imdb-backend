"""
Movie setup url config
"""
from django.urls import path

from movie.views import MovieListCreateView, user_bookmark


urlpatterns = [
    path('', MovieListCreateView.as_view(), name='movie-create-list'),
    path('bookmark/', user_bookmark, name='my-bookmark'),
]
