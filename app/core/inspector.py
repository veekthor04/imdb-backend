from drf_yasg.inspectors import PaginatorInspector
from drf_yasg import openapi
from collections import OrderedDict


class PageNumberPaginatorInspectorClass(PaginatorInspector):
    def get_paginated_response(self, paginator, response_schema):
        paged_schema = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=OrderedDict((
                ("count", openapi.Schema(type=openapi.TYPE_INTEGER)),
                ("next", openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                ("previous", openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, x_nullable=True)),
                ("results", response_schema),
            )),
            required=['results']
        )

        return paged_schema
