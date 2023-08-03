from django.contrib import admin

from app.models import Review, Destination

class Reviews(admin.ModelAdmin):
    """Representation of the reviews table."""

    list_display = ('id', 'name', 'review', 'photo')
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Review, Reviews)


class Destinations(admin.ModelAdmin):
    """Representation of the destinations table."""

    list_display = ('id', 'name', 'price', 'photo_1', 'photo_2', 'meta',
                    'description')
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Destination, Destinations)
