from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework import generics, permissions, pagination, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from core.models import Movie, UserMovieBookmark
from movie.serializers import MovieSerializer
from movie.swagger import get_bookmark_auto_schema, post_bookmark_auto_schema,\
    delete_bookmark_auto_schema


class MovieListCreateView(generics.ListCreateAPIView):
    """List and Creates Movies"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)
    my_tags = ["Movie"]
    
    def get_queryset(self):
        movie_queryset = cache.get('movie_queryset')
        
        if movie_queryset == None:
            movie_queryset = Movie.objects.all()
        cache.set('movie_queryset', movie_queryset)
        return movie_queryset
        

@get_bookmark_auto_schema()
@post_bookmark_auto_schema()
@delete_bookmark_auto_schema()
@permission_classes([IsAuthenticated,])
@api_view(['GET', 'POST', 'DELETE'])
def user_bookmark(request):
    
    if request.method == 'GET':
        paginator = pagination.PageNumberPagination()
        user_movies = cache.get(f'user_movies_{request.user.id}')

        if user_movies is None:
            user_movies = UserMovieBookmark.objects.get(
                user=request.user
            ).movies.all()
            cache.set(f'user_movies_{request.user.id}', user_movies)

        page = paginator.paginate_queryset(user_movies, request)
        serializer = MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':
        movie_id = request.data.get('movie_id')
        movie = get_object_or_404(Movie, id=movie_id)
        
        UserMovieBookmark.objects.get(
            user=request.user
        ).movies.add(movie)
        cache.delete(f'user_movies_{request.user.id}')

        return Response(
            "Movie has been added to user's bookmark successfully", 
            status=status.HTTP_201_CREATED
        )
    
    elif request.method == 'DELETE':
        movie_id = request.data.get('movie_id')
        movie = get_object_or_404(Movie, id=movie_id)
        
        UserMovieBookmark.objects.get(
            user=request.user
        ).movies.remove(movie)
        cache.delete(f'user_movies_{request.user.id}')
        
        return Response(
            "Movie has been removed from user's bookmark successfully", 
            status=status.HTTP_201_CREATED
        )
