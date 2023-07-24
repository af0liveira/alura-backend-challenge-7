from django.contrib import admin

from app.models import Review

class Reviews(admin.ModelAdmin):
    """Representation of the reviews table."""

    list_display = ('id', 'name', 'review', 'photo')
    list_display_links = ('id', 'name')
    list_per_page = 25

admin.site.register(Review, Reviews)
