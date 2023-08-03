import random

from rest_framework import viewsets, status
from rest_framework.response import Response

from app.models import Review, Destination
from app.serializers import ReviewSerializer, DestinationSerializer
from app.filters import DestinationFilter


class ReviewsViewSet(viewsets.ModelViewSet):
    """Viewset to display all Review instances."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['post', 'get', 'put', 'delete']


class SelectedReviewsViewSet(viewsets.ModelViewSet):
    """Viewset to display three randomly selected Review instances."""

    queryset = Review.objects.order_by('?')[:3]
    serializer_class = ReviewSerializer
    http_method_names = ['get']


class DestinationsViewSet(viewsets.ModelViewSet):
    """Viewset to display the Destination list."""

    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    filterset_class = DestinationFilter
    http_method_names = ['post', 'get', 'put', 'delete']

    def retrieve(self, request, *args, **kwargs):
        """Respond with custom message if object cannot be retrieved."""

        queryset = Destination.objects.filter(id=self.kwargs['pk'])

        if not queryset:
            response = Response({'mensagem': "Nenhum destino encontrado."},
                                 status=status.HTTP_404_NOT_FOUND)
        else:
            response = super(DestinationsViewSet, self).retrieve(request, *args, **kwargs)

        return response

    def list(self, request, *args, **kwargs):
        """Respond with HTTP 404 if request returns an empty list."""

        std_response = super(DestinationsViewSet, self).list(request, *args, **kwargs)

        filter_queryset = self.filter_queryset(queryset=self.queryset)
        if filter_queryset.count() > 0:
            response = std_response
        else:
            response = Response({'mensagem': "Nenhum destino encontrado."},
                                 status=status.HTTP_404_NOT_FOUND)

        return response
