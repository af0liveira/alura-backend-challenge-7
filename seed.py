import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.core.files import File
from djmoney.money import Money

import random
from faker import Faker

from app.models import  Review, Destination


def create_reviews(num_reviews):
    fake = Faker('pt_BR')
    Faker.seed(10)

    for _ in range(num_reviews):
        sex = random.choice(['male', 'female'])
        gen_name = getattr(fake, f'name_{sex}')
        name = gen_name()
        review = fake.text()
        review_obj = Review(name=name, review=review)
        with open(f'assets/userpic_placeholder_{sex}.png', 'rb') as fp:
            review_obj.photo.save('userpic.png', File(fp), save=False)
        review_obj.save()

def create_destinations(num_destinations):
    fake = Faker('pt_BR')
    Faker.seed(10)

    for _ in range(num_destinations):
        name = fake.country()
        price = Money(random.randrange(10_000, 500_000), 'BRL')
        destination_obj = Destination(name=name, price=price)
        with open(f'assets/destination_placeholder.png', 'rb') as fp:
            destination_obj.photo.save('destination.png', File(fp), save=False)
        destination_obj.save()


if __name__ == '__main__':

    create_reviews(20)
    create_destinations(50)
