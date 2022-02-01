from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework_simplejwt.views import TokenObtainPairView,\
     TokenRefreshView
from rest_framework import generics, permissions, viewsets

from .serializers import MyTokenObtainPairSerializer, Userserializer


class MyTokenObtainPairView(TokenObtainPairView):
    """Custom token view
    """
    serializer_class = MyTokenObtainPairSerializer
    my_tags = ["User Authentication"]


class MyTokenRefreshView(TokenRefreshView):
    """Custom refresh token view
    """
    my_tags = ["User Authentication"]


class CreateUserView(generics.CreateAPIView):
    """create a new user in the project"""
    serializer_class = Userserializer
    my_tags = ["User Authentication"]


class ProfileUserView(generics.RetrieveUpdateDestroyAPIView):
    """Retives and updates the authenticated user's profile
    """
    queryset = get_user_model().objects.all()
    serializer_class = Userserializer
    permission_classes = (permissions.IsAuthenticated,)
    my_tags = ["Profile"]

    def get_object(self):
        """Retrieve authenticated user"""
        return self.request.user


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Listing or retrieving users"""
    queryset = get_user_model().objects.all()
    serializer_class = Userserializer
    my_tags = ['Users']

    # cache all list and view for a minute
    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
