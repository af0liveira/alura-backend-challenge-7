from django.db import models

class Review(models.Model):
    """Represents a user review."""

    photo = models.URLField()
    review = models.TextField(max_length=280, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
