from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()