from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, pagination, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.models import Movie, UserMovieBookmark
from movie.serializers import MovieSerializer, UserMovieBookmarkSerializer
from movie.swagger import get_bookmark_auto_schema, post_bookmark_auto_schema,\
    delete_bookmark_auto_schema


class MovieListCreateView(generics.ListCreateAPIView):
    """List and Creates Movies"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)
    my_tags = ["Movie"]


class UserMovieBookmarkList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)
    my_tags = ["Movie Bookmark"]
    
    def get_queryset(self):
        return UserMovieBookmark.objects.get(user=self.request.user).movies.all()


# class UserMovieBookmark(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserMovieBookmark.objects.all()
#     serializer_class = UserMovieBookmarkSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#     my_tags = ["Movie Bookmark"]
    
    
@get_bookmark_auto_schema()
@post_bookmark_auto_schema()
@delete_bookmark_auto_schema()
@api_view(['GET', 'POST', 'DELETE'])
def my_bookmark(request):
    if request.method == 'GET':
        paginator = pagination.PageNumberPagination()

        queryset = UserMovieBookmark.objects.get(
            user=request.user
        ).movies.all()
        
        page = paginator.paginate_queryset(queryset, request)
        serializer = MovieSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':
        movie_id = request.data.get('movie_id')
        movie = get_object_or_404(Movie, id=movie_id)
        
        UserMovieBookmark.objects.get(
            user=request.user
        ).movies.add(movie)
        
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
        
        return Response(
            "Movie has been removed from user's bookmark successfully", 
            status=status.HTTP_201_CREATED
        )
