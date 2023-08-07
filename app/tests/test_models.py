"""Test suite for app.models."""

from django.test import TestCase
from djmoney.money import Money
from app.models import Review, Destination


class ReviewModelTestCase(TestCase):
    """Test case for the Review model."""

    def setUp(self):
        self.review = Review(
            name="Marvin",
            review="I can see by infra-red,\nHow I hate the night."
        )

    def test_review_attributes(self):
        """Ensure Review attributes are correctly set."""
        self.assertEqual(self.review.name, 'Marvin')
        self.assertNotEqual(self.review.name, 'MARVIN')
        self.assertEqual(self.review.review, 
                         'I can see by infra-red,\nHow I hate the night.')
        self.assertEqual(self.review.photo, '')


class DestinationModelTestCase(TestCase):
    """Test case for the Destination model."""

    def setUp(self):
        self.destination = Destination(
            name="Magrathea",
            price=Money(42, currency='GBP'),
            meta="Ford was here!",
            description="Marvin was too depressed to describe Magrathea.",
        )

    def test_destination_attributes(self):
        """Ensure Destination attributes are correctly set."""
        self.assertEqual(self.destination.name, 'Magrathea')
        self.assertNotEqual(self.destination.name, 'MAGRATHEA')
        self.assertEqual(self.destination.meta, 'Ford was here!')
        self.assertEqual(self.destination.description,
                         'Marvin was too depressed to describe Magrathea.')
        self.assertEqual(self.destination.price, Money(42, currency='GBP'))
        self.assertEqual(self.destination.photo_1, '')
        self.assertEqual(self.destination.photo_2, '')
