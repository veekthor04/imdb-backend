from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

# try: #to allow authentication through phone number or any other
# field, modify the below statement
#             user = UserModel.objects.get(Q(username__iexact=
# username) | Q(email__iexact=username))
#         except UserModel.DoesNotExist:
#             UserModel().set_password(password)
#         except MultipleObjectsReturned:
#             return User.objects.filter(email=username).order_by
# ('id').first()
#         else:
#             if user.check_password(password) and
# self.user_can_authenticate(user):
#                 return user
