"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


SchemaView = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="""Test description
        The `swagger-ui` view can be found [here](/swagger).
        The `ReDoc` view can be found [here](/redoc).
        The `swagger YAML document` can be found [here](/swagger.yaml).
        The `Django administration` can be accessed [here](/admin).
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="victoradenuga04@yahoo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Redirect to redoc
def root_redirect(request):
    schema_view = 'redoc'
    return redirect(schema_view, permanent=True)


urlpatterns = [
    path('', root_redirect, name='root_page'),
    re_path(
        r'^swagger(?P<format>.json|.yaml)$',
        SchemaView.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        SchemaView.with_ui('swagger', cache_timeout=0),
        name='swagger-ui'
    ),
    path(
        'redoc/',
        SchemaView.with_ui('redoc', cache_timeout=0),
        name='redoc'),
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]
