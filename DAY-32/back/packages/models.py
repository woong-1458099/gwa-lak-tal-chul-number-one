from django.db import models
from django.conf import settings
from places.models import Place


class Package(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    prompt = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    places = models.ManyToManyField(
        Place,
        related_name='packages',
        blank=True
    )

    def __str__(self):
        return self.prompt or f"Package {self.id}"
