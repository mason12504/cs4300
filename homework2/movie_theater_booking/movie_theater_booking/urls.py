"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.contrib.auth.models import User
from bookings.models import Movie
from bookings.views import *
from bookings.serializers import *
from rest_framework import routers, serializers, viewsets

# So all the view sets we register here are defined in bookings.views 

# Routers provide an easy way of automatically determining the URL conf.
# default router includes an API root view for the base directory
routerHTML = routers.DefaultRouter()
routerHTML.register(r'movies', MovieViewSet)
routerHTML.register(r'seats', SeatViewSet)
routerHTML.register(r'bookings', BookingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(routerHTML.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
