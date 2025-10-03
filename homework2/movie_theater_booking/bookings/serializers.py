# part of rest framework 

from rest_framework import serializers
from bookings.models import * 

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer this looked way better than the tutorials so going with it
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'