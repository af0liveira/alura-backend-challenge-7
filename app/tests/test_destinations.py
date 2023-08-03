from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from djmoney.money import Money

from app.models import Destination


class DestinationsTestCase(APITestCase):
    """Test case for Destinations instances."""

    def setUp(self):
        self.list_url = reverse('Destinations-list')

        self.destinations = [
            Destination.objects.create(
                name='Destination #1',
                price = Money(666, currency='BRL')
            ),
            Destination.objects.create(
                name='Destination #2',
                price = Money(42_000, currency='BRL')
            ),
        ]

    def test_get_destinations_list(self):
        """Ensure that we can GET the list of Destination objects."""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), len(self.destinations))

    def test_get_destination(self):
        """Ensure that we can GET a single Destination object."""
        response = self.client.get(self.list_url+'1/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_destination_not_found(self):
        """Ensure code 404 if Destination object not found."""
        response = self.client.get(self.list_url+'0/')
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_destination_with_ai_completion(self):
        """Ensure that we can POST a new Destination with ChatGPT completion.
        
        If the 'description' field is not provided, it should be automatically
        generated using ChatGPT.
        """
        price = Money(1_000_000, currency='BRL')
        data = {
            "name": "Valhalla",
            "price_currency": str(price.currency),
            "price": str(price.amount),
            "meta": "Valhala rules!",
        }
        response = self.client.post(self.list_url, data=data, format='json')
        # print(response.data, flush=True)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Destination.objects.count(), len(self.destinations)+1)
        self.assertGreater(len(response.data['description'].strip()), 0)

    def test_post_destination_with_explicit_description(self):
        """Ensure that we can POST a new Destination with explicit description.
        
        The main goal is to ensure that non-blank 'description' is not replaced
        by ChatGPT-generated values.
        """
        price = Money(1_000_000, currency='BRL')
        data = {
            "name": "Valhalla",
            "price_currency": str(price.currency),
            "price": str(price.amount),
            "meta": "Valhala rules!",
            "description": "X",
        }
        response = self.client.post(self.list_url, data=data, format='json')
        # print(response.data, flush=True)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Destination.objects.count(), len(self.destinations)+1)
        self.assertEquals(response.data['description'], 'X')

    def test_put_destination(self):
        """Ensure that we can replace a Destination object with PUT."""
        price = Money(1_500_000, currency='BRL')
        data = {
            "name": "Valhalla",
            "price_currency": str(price.currency),
            "price": str(price.amount),
            "meta": "For honorable Vikings!",
        }
        response = self.client.put(self.list_url+'1/', data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Destination.objects.count(), len(self.destinations))

    def test_delete_destination(self):
        """Ensure that we can DELETE a Destination object."""
        response = self.client.delete(self.list_url+'1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(Destination.objects.count(), len(self.destinations)-1)
