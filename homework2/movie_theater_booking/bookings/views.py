from django.shortcuts import render

# Create your views here.
from models import Movie
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

# Basically just from rest api, but changing User to Movie
class MovieViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Movie.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)