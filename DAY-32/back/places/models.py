from django.db import models
from accounts.models import Theme

# Create your models here.

class Place(models.Model):
    google_place_id = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()
    rating = models.FloatField(null=True, blank=True)
    rating_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    themes = models.ManyToManyField(
        Theme,
        blank=True,
        related_name='places'
    )

    def __str__(self):
        return self.name