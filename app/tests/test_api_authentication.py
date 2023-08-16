from django.contrib.auth import authenticate, models
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from djmoney.money import Money


class UserAuthenticationTestCase(APITestCase):
    """Test case for user authentication."""

    def setUp(self):
        self.user = models.User.objects.create_user(username='the_user',
                                                    password='the_password')

    def test_user_authentication(self):
        """Ensure user authentication with existing username and password."""
        user = authenticate(username='the_user', password='the_password')
        self.assertTrue(user is not None and user.is_authenticated)

    def test_user_authentication_wrong_username(self):
        """Ensure user authentication fails with wrong username."""
        user = authenticate(username='a_user', password='the_password')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_user_authentication_wrong_password(self):
        """Ensure user authentication fails with wrong password."""
        user = authenticate(username='the_user', password='a_password')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_get_destinations_with_unauthenticated_user(self):
        """Ensure unauthenticated users can GET destinations."""
        list_url = reverse('Destinations-list')
        response = self.client.get(list_url)
        self.assertIn(response.status_code,
                      [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND])

    def test_get_reviews_with_unauthenticated_user(self):
        """Ensure unauthenticated users can GET reviews."""
        list_url = reverse('Reviews-list')
        response = self.client.get(list_url)
        self.assertIn(response.status_code,
                      [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND])

    def test_post_destinations_with_unauthenticated_user(self):
        """Ensure that unauthenticated users cannot POST destinations."""
        list_url = reverse('Destinations-list')
        price = Money(1_000_000, currency='BRL')
        data = {
            "name": "Valhalla",
            "price_currency": str(price.currency),
            "price": str(price.amount),
            "meta": "Valhala rules!",
            "description": "X",
        }
        response = self.client.post(list_url, data=data, format='json')
        self.assertIn(response.status_code,
                      [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_post_reviews_with_unauthenticated_user(self):
        """Ensure that unauthenticated users cannot POST reviews."""
        list_url = reverse('Reviews-list')
        data = {
            "name": "Reh V. Ewer",
            "review": "I viewed and reviewed that place.",
        }
        response = self.client.post(list_url, data=data, format='json')
        self.assertIn(response.status_code,
                      [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])
