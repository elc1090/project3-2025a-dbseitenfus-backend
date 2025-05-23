from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User, Document
from .serializers import UserSerializer, DocumentSerializer
from rest_framework import viewsets


class UserListViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = UserSerializer

# Create your views here.
def databaseEmDjango():
    data = User.objects.get(pk=1)
    data = User.objects.filter(username='daniel')
