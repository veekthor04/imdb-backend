from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


User = get_user_model()


class EmailModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = User
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
