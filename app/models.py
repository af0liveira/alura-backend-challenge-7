from django.db import models
from djmoney.models.fields import MoneyField
from app.utils import ask_chatGPT


class Review(models.Model):
    """Represents a user review."""

    name = models.CharField(max_length=50, null=False, blank=False)
    photo = models.ImageField(blank=True)
    review = models.TextField(max_length=280, null=False, blank=False)


class Destination(models.Model):
    """Represents a destination."""

    photo_1 = models.ImageField(blank=True)
    photo_2 = models.ImageField(blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL',
                       null=True, blank=False)
    meta = models.CharField(max_length=160)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = ask_chatGPT(
                f"""Olá! Por favor, faça um resumo sobre {self.name}.

                O resumo deve:
                1) usar linguagem information;
                2) enfatizar os atrativos do local;
                3) ser dividido em dois parágrafos de até 100 caracteres.
                """
            )
        super(Destination, self).save(*args, **kwargs)
