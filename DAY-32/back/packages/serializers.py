from rest_framework import serializers
from .models import Package


class PackageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ('id', 'prompt')

