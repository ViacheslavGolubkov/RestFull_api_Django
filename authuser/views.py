from rest_framework import viewsets
from serializers import UserRegistrationSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserRegistrationSerializer
