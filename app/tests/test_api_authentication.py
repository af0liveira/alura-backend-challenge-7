from django.contrib.auth import authenticate, models
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


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
        """Ensure unauthenticated users cannot GET destinations."""
        list_url = reverse('Destinations-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_reviews_with_unauthenticated_user(self):
        """Ensure unauthenticated users cannot GET reviews."""
        list_url = reverse('Reviews-list')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
