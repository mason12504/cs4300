# all credit to chatGPT on these
from django.test import TestCase
from django.utils import timezone
from .models import Movie, Seat, Booking
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ValidationError 
from django.urls import reverse 

# per chatGPT this is one test case
class MovieModelTest(TestCase):
    def test_create_movie(self):
        movie = Movie.objects.create(
            title="Inception",
            description="A mind-bending thriller about dreams within dreams.",
            release_date=timezone.now(),
            duration=148
        )

        # Retrieve it back from the database
        saved_movie = Movie.objects.get(title="Inception")

        # Assertions: check that values match
        self.assertEqual(saved_movie.title, "Inception")
        self.assertEqual(saved_movie.description, "A mind-bending thriller about dreams within dreams.")
        self.assertEqual(saved_movie.duration, 148)
        self.assertIsNotNone(saved_movie.release_date)

# same thing but for seats
class SeatModelTest(TestCase):
    def test_create_seat(self):

        # 2 valid seats
        seat = Seat.objects.create(
            seat_number = 1,
            booking_status = 0
        )

        seat1 = Seat.objects.create(
            seat_number = 100,
            booking_status = 1
        )

        # Retrieve it back from the database
        seat1_saved = Seat.objects.get(seat_number=1)
        seat2_saved = Seat.objects.get(seat_number=100)

        # Assertions: check that values match
        self.assertEqual(seat1_saved.seat_number, 1)
        self.assertEqual(seat1_saved.booking_status, False)
        self.assertEqual(seat2_saved.seat_number, 100)

    # one invalid creation attempt check
    # per chat gpt
    def test_invalid_seat_data_raises_error(self):
        """Ensure invalid Seat data raises ValidationError"""

        seat = Seat(
            seat_number="hello",     # invalid type
            booking_status="Zero"    # invalid type
        )

        with self.assertRaises(ValidationError):
            seat.full_clean()  # <-- This runs Django field validation
            seat.save()

# same idea with bookings, all chatGPT here
class BookingModelTest(TestCase):

    # set up movie and seat to attach to booking
    def setUp(self):
        # Create valid related Movie and Seat objects
        self.movie = Movie.objects.create(
            title="Interstellar",
            description="A journey through space and time.",
            release_date=timezone.now(),
            duration=169
        )

        self.seat = Seat.objects.create(
            seat_number=1,
            booking_status=False
        )

    def test_create_booking(self):
        """Test creation of valid Booking objects"""

        # Create 2 valid bookings
        booking1 = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user="Alice",
            booking_date=timezone.now()
        )

        booking2 = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user="Bob",
            booking_date=timezone.now()
        )

        # Retrieve them from the database
        saved_booking1 = Booking.objects.get(user="Alice")
        saved_booking2 = Booking.objects.get(user="Bob")

        # Assertions: check that values match
        self.assertEqual(saved_booking1.user, "Alice")
        self.assertEqual(saved_booking1.movie.title, "Interstellar")
        self.assertEqual(saved_booking1.seat.seat_number, 1)
        self.assertEqual(saved_booking2.user, "Bob")

    def test_invalid_booking_data_raises_error(self):
        """Ensure invalid Booking data raises ValidationError"""

        # Invalid: missing required fields or wrong types
        booking = Booking(
            movie=None,      # ❌ must not be None
            seat=None,       # ❌ must not be None
            user=123,        # ❌ should be a string
            booking_date="notadate"  # ❌ wrong type
        )

        with self.assertRaises(ValidationError):
            booking.full_clean()  # Validates all fields
            booking.save()


class APIRootTest(APITestCase):
    def test_api_root_returns_expected_links(self):
        """Ensure API root returns expected endpoints"""
        url = reverse('api-root')  # assumes DefaultRouter with basename
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('movies', response.data)
        self.assertIn('seats', response.data)
        self.assertIn('bookings', response.data)


class MovieAPITest(APITestCase):
    def test_movie_list_returns_200(self):
        """GET /api/movies/ should return 200 OK"""
        url = reverse('movie-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_movie(self):
        """POST /api/movies/ should create a new movie"""
        url = reverse('movie-list')
        data = {
            "title": "Inception",
            "description": "A mind-bending thriller.",
            "release_date": timezone.now(),
            "duration": 148
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().title, "Inception")


class BookingAPITest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Interstellar",
            description="A journey through space and time.",
            release_date=timezone.now(),
            duration=169
        )
        self.seat = Seat.objects.create(seat_number=1, booking_status=False)

    def test_create_valid_booking(self):
        """POST /api/bookings/ should create a booking"""
        url = reverse('booking-list')
        data = {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": "Alice",
            "booking_date": timezone.now()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.get().user, "Alice")

    def test_create_invalid_booking(self):
        """POST /api/bookings/ with invalid data should fail"""
        url = reverse('booking-list')
        data = {
            "movie": None,  # invalid
            "seat": None,   # invalid
            "user": 123,    # invalid type
            "booking_date": "notadate"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)