from django.urls import path
from . import views


urlpatterns = [
    path("artists/", views.artists_view, name="artists_view"),
]