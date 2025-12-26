from django.urls import path
from .views import PlaceSearchAPIView


urlpatterns = [
    path('search/', PlaceSearchAPIView.as_view()),
]
