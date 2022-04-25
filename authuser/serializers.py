from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    is_author = serializers.HiddenField(default=False)

    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'password', 'is_author')