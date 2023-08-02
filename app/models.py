from django.db import models

class Review(models.Model):
    """Represents a user review."""

    name = models.CharField(max_length=50, null=False, blank=False)
    photo = models.ImageField(blank=True)
    review = models.TextField(max_length=280, null=False, blank=False)


class Destination(models.Model):
    """Represents a destination."""

    photo = models.URLField()
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=False)
