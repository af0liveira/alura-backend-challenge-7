import random

from rest_framework import viewsets, generics

from app.models import Review
from app.serializers import ReviewSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    """Viewset to display all Review instances."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
