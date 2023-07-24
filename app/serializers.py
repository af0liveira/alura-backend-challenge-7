from rest_framework import serializers

from app.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review objects."""

    class Meta:
        model = Review
        fields = '__all__'
