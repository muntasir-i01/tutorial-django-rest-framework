from django.shortcuts import render
from django.contrib.auth.models import Group, User
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
from rest_framework import permissions, viewsets


# Create your views here.