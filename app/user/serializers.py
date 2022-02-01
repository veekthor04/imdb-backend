from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom Token serializer to add extra fields
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Custom fields
        token['username'] = user.username
        token['email'] = user.email

        return token


class Userserializer(serializers.ModelSerializer):
    """Serializer for users object"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def validate_password(self, value):
        """Validates password using the AUTH_PASSWORD_VALIDATORS
        """
        user = self.context['request'].user
        validate_password(password=value, user=user)

    def create(self, validated_data):
        """Creates a new user using the create_user
        """
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Updates a user, sets the password and returns it
        """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user
