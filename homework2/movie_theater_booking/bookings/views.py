from django.shortcuts import render

# Create your views here.
from .models import Movie
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer 
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *

# Basically just from rest api, but changing User to Movie
# From my understanding modelviewsets provide CRUD by default
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 
    renderer_class = [TemplateHTMLRenderer]
    template_name = ''

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer 