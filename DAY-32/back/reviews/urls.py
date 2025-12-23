from django.urls import path
from .views import list_by_place, create_review

urlpatterns = [
    path('places/<int:place_id>/', list_by_place),         # GET
    path('places/<int:place_id>/create/', create_review),  # POST
]
