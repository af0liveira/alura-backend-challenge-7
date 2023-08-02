"""Implement filters for the application database."""

from django_filters.rest_framework import FilterSet, CharFilter
from app.models import Destination


class DestinationFilter(FilterSet):
    """Define filters for Destination instances."""

    name = CharFilter(lookup_expr='iexact')
    nome = CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Destination
        fields = ['name', 'nome']