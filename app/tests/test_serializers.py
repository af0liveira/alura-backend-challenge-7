"""Test suite for app.serializers."""

from django.test import TestCase
from djmoney.money import Money
from app.models import Review, Destination
from app.serializers import ReviewSerializer, DestinationSerializer


class ReviewSerializerTestCase(TestCase):
    """Test case for ReviewSerializer."""

    def setUp(self):
        self.review = Review(
            name="Ford Prefect",
            review="Make sure to have your towel!",
        )
        self.serializer = ReviewSerializer(instance=self.review)

    def test_serialized_review_fields(self):
        """Ensure Review fields have been serialized."""
        data = self.serializer.data
        expected_fields = set(['id', 'name', 'photo', 'review'])
        serialized_fields = set(data.keys())
        self.assertEqual(serialized_fields, expected_fields)

    def test_serialized_review_field_values(self):
        """Ensure Review fields have been serialized with correct values."""
        data = self.serializer.data
        self.assertEqual(data['id'], self.review.id)
        self.assertEqual(data['name'], self.review.name)
        self.assertEqual(data['review'], self.review.review)
        self.assertEqual(data['photo'], None)
        # NOTE: If the photo is not informed, the serializer should parse it to
        # None; 'self.review.photo' will actually give a
        # django.db.models.ImageField object.
        

class DestinationSerializerTestCase(TestCase):
    """Test case for DestinationSerializer."""

    def setUp(self):
        self.destination = Destination(
            name="Betelgeuse V",
            price=Money(42, currency='USD'),
            meta="Ford's birthplace.",
            description="Near the star Betelgeuse!",
        )
        self.serializer = DestinationSerializer(instance=self.destination)

    def test_serialized_destination_fields(self):
        """Ensure Destination fields have been serialized."""
        data = self.serializer.data
        expected_fields = set([
            'id',
            'photo_1',
            'photo_2',
            'name',
            'price',
            'price_currency',  # created by djmoney.money.Money()  
            'meta',
            'description',
        ])
        serialized_fields = set(data.keys())
        self.assertEqual(serialized_fields, expected_fields)

    def test_serialized_destination_field_values(self):
        """Ensure Destination fields have been serialized correctly."""
        data = self.serializer.data
        self.assertEqual(data['id'], self.destination.id)
        self.assertEqual(data['photo_1'], None)
        self.assertEqual(data['photo_2'], None)
        self.assertEqual(data['name'], self.destination.name)
        # NOTE: 'price' is serialized to 'price' and 'price_currency'!
        n = self.destination.price.decimal_places
        self.assertEqual(data['price'], 
                         f"{self.destination.price.amount:.{n}f}")
        self.assertEqual(data['price_currency'],
                         str(self.destination.price.currency))
