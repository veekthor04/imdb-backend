from collections import OrderedDict
import imp
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import pagination
from drf_yasg.inspectors import PaginatorInspector

from movie.serializers import MovieSerializer


def get_bookmark_auto_schema():
    return swagger_auto_schema(
        method='get',
        responses={200: MovieSerializer(many=True)},
        operation_description="List user's bookmarked movies",
        paginator_inspectors=[PaginatorInspector,],
        pagination_class=pagination.PageNumberPagination
    )


def post_bookmark_auto_schema():    
    return swagger_auto_schema(
        method='post', 
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'movie_id': openapi.Schema(type=openapi.TYPE_INTEGER)
            }
        ),
        responses={
            200: "Movie has been removed from user's bookmark successfully",
            404: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(type=openapi.TYPE_STRING, example='Not found.'),
                }
            ),
        },
        operation_description="Adds a movie to user's bookmark"
    )
    

def delete_bookmark_auto_schema():
    return swagger_auto_schema(
        method='delete', 
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'movie_id': openapi.Schema(type=openapi.TYPE_INTEGER)
            }
        ),
        responses={
            200: "Movie has been removed from user's bookmark successfully",
            404: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(type=openapi.TYPE_STRING, example='Not found.'),
                }
            ),
        },
        operation_description="Removes a movie from user's bookmark"
    )