from django.contrib.auth import models
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from app.models import Review


class ReviewsTestCase(APITestCase):
    """Test case for Reviews instances."""

    def setUp(self):
        self.list_url = reverse('Reviews-list')
        self.reviews = [
            Review.objects.create(
                name='Reviewer #1',
                review = 'Review of Reviewer #1.',
            ),
            Review.objects.create(
                name='Reviewer #2',
                review = 'Review of Reviewer #2.',
            ),
        ]
        self.user = models.User.objects.create_user(username='the_user',
                                                    password='the_password')
        self.client.force_authenticate(self.user)

    def test_get_reviews_list(self):
        """Ensure that we can GET the list of Review objects."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.reviews))

    def test_get_review(self):
        """Ensure that we can GET a single Review object."""
        response = self.client.get('/depoimentos/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_not_found(self):
        """Ensure code 404 if Review object not found."""
        response = self.client.get('/depoimentos/0/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_review(self):
        """Ensure that we can POST a new Review object."""
        data = {
            'name': 'Boneco Josias',
            'review': 'Boneco Josias vai matar sua família!'
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), len(self.reviews)+1)

    def test_put_review(self):
        """Ensure that we can replace a Review object with PUT."""
        data = {
            'name': 'Boneco Josias',
            'review': 'Boneco Josias é um bandjindjinho!'
        }
        response = self.client.put('/depoimentos/1/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Review.objects.count(), len(self.reviews))

    def test_delete_review(self):
        """Ensure that we can DELETE a Review object."""
        response = self.client.delete('/depoimentos/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), len(self.reviews)-1)
