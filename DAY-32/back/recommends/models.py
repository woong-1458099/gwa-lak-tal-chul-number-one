from django.db import models
from django.conf import settings
from places.models import Place
from packages.models import Package

# Create your models here.

class SearchLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    keyword = models.CharField(max_length=200)
    center_lat = models.FloatField(null=True, blank=True)
    center_lng = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PlaceClickLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE
    )
    source = models.CharField(max_length=30)  
    # 예: 'map', 'recommend', 'package'
    created_at = models.DateTimeField(auto_now_add=True)


class AIRecommendLog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE
    )
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)