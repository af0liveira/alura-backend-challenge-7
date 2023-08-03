import os
import openai

from rest_framework import viewsets, status
from rest_framework.response import Response

from app.models import Review, Destination
from app.serializers import ReviewSerializer, DestinationSerializer
from app.filters import DestinationFilter

openai.api_key = str(os.getenv('OPENAI_API_KEY'))

def ask_chatgpt(message):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": message}],
    )
    return completion.choices[0].message.content.strip()


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

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return None

        if not serializer.validated_data.get('description', None):
            name = serializer.validated_data['name']
            description = ask_chatgpt(
                f"""Olá! Por favor, faça um resumo sobre {name}.

                O resumo deve usar linguagem informal e enfatizar os atrativos
                do local. Além disso, deve conter 2 parágrafos de até 100
                caracteres cada.
                """
            )
            serializer.validated_data['description'] = description

        serializer.save()

        response = Response(serializer.data, status=status.HTTP_201_CREATED)

        return response

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
