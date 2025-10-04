from django.shortcuts import render

# Create your views here.
from .models import Movie
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer, BrowsableAPIRenderer 
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .templates.bookings import *

# Basically just from rest api, but changing User to Movie
# From my understanding modelviewsets provide CRUD by default
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 
    # can remove the below code if I want to go back to API renderer
    # need to figure a way to allow both modes basically. 
    # ALSO need to remove the entire bit in settings
    renderer_class = [TemplateHTMLRenderer, BrowsableAPIRenderer]
    template_name = 'movie_list.html'

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer 
