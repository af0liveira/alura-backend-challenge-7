from django.db import models
from djmoney.models.fields import MoneyField

class Review(models.Model):
    """Represents a user review."""

    name = models.CharField(max_length=50, null=False, blank=False)
    photo = models.ImageField(blank=True)
    review = models.TextField(max_length=280, null=False, blank=False)


class Destination(models.Model):
    """Represents a destination."""

    photo = models.ImageField(blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL',
                       null=True, blank=False)
