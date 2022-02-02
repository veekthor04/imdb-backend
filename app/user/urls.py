"""
User setup url config
"""
from django.urls import path
from rest_framework.routers import SimpleRouter

from user.views import MyTokenObtainPairView, CreateUserView,\
    ProfileUserView, MyTokenRefreshView, UserViewSet


router = SimpleRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path(
        'token/refresh/',
        MyTokenRefreshView.as_view(),
        name='token_refresh'
    )
]

urlpatterns += router.urls
