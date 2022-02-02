"""
Movie setup url config
"""
from django.urls import path

from movie.views import MovieListCreateView, UserMovieBookmarkList, my_bookmark


urlpatterns = [
    path('', MovieListCreateView.as_view(), name='movie-create-list'),
    path('bookmark/', my_bookmark, name='my-bookmark'),
    path('my-bookmark/', UserMovieBookmarkList.as_view(), name='my-bookmark'),
]
