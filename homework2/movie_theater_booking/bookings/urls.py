# I saw something like this in a tutorial
# Right now it does nothing I am pretty sure
# leaving it just in case but mostly IGNORE 

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [] 

router = DefaultRouter()
router.register('movies', views.MovieViewSet)
urlpatterns += router.urls 