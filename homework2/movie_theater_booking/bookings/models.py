from django.db import models
from django.utils import timezone 
# Create your models here.

# Movie: title, description, release date, duration. 
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    release_date = models.DateTimeField("date published")
    duration = models.IntegerField(default=0)

# Seat: seat number, booking status.
class Seat(models.Model):
    seat_number = models.IntegerField(default=0)
    booking_status = models.BooleanField(default=0)

# Booking: movie, seat, user, booking date. 
class Booking(models.Model): 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    booking_date = models.DateTimeField(default=timezone.now)
