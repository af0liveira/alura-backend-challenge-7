import random

from rest_framework import viewsets, generics

from app.models import Review, Destination
from app.serializers import ReviewSerializer, DestinationSerializer

class ReviewsViewSet(viewsets.ModelViewSet):
    """Viewset to display all Review instances."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class SelectedReviewsViewSet(viewsets.ModelViewSet):
    """Viewset to display three randomly selected Review instances."""

    queryset = Review.objects.order_by('?')[:3]
    serializer_class = ReviewSerializer

class DestinationsViewSet(viewsets.ModelViewSet):
    """Viewset to display all Destination instances."""

    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
