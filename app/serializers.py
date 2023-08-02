from rest_framework import serializers

from app.models import Review, Destination

class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review objects."""

    class Meta:
        model = Review
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):
    """Serializer for Destination objects."""

    class Meta:
        model = Destination
        fields = '__all__'
