from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from accounts.api.serializers import UserSerializer

# Create your views here.




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]