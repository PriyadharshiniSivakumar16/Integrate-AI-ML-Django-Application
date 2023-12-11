from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any additional fields you want for the user

    def __str__(self):
        return self.username
      from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')  # Add any additional fields
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
      REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer2. Open the project's `urls.py` file and update the URL patterns:
```python
from django.urls import path
from myapp.views import CustomAuthToken, UserRegistrationView

urlpatterns = [
    path('api/login/', CustomAuthToken.as_view(), name='api-login'),
    path('api/register/', UserRegistrationView.as_view(), name='api-register'),
]
