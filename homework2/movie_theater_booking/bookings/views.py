from django.shortcuts import render

# Create your views here.
from .models import Movie
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action 
from rest_framework.renderers import TemplateHTMLRenderer, BrowsableAPIRenderer, JSONRenderer 
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .templates.bookings import *

# Basically just from rest api, but changing names
# From my understanding modelviewsets provide CRUD by default
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer 

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer 

# I gave a good try to do this correctly with viewsets but crawled back to regular django views as it was much easier 

# just lists all the movies 
def Movie_ListView_HTML(request):
    movies = Movie.objects.all()
    # pass movies as the list of all movies so we can display them to the page
    return render(request, 'movie_list.html', {'movies': movies})

def seat_bookingView_HTML(request):
    # for display
    seats = Seat.objects.all()

    # when we send a post by clicking the form in seat_booking.html, we make a new seat.
    # 
    if request.method == 'POST':
        seat_num = request.POST.get('seat_number')
        Seat.objects.create(seat_number = seat_num, booking_status = False)

        return render(request, 'seat_booking.html', {"seats" : seats})

    return render(request, 'seat_booking.html',{"seats": seats})

def Booking_ViewHTML(request):
    bookings = Booking.objects.all() 
    return render(request, 'bookings_history.html', {'bookings': bookings})

# just a basic home page html view 
def home_page(request):
    return render(request, 'home_page.html')