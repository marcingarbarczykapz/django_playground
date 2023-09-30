import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from reviews.models import Review
from shop.models import Product  # assuming your shop app is named 'shop'


class Command(BaseCommand):
    help = 'Create random reviews'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of reviews to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        users = User.objects.all()
        products = Product.objects.all()

        for _ in range(total):
            Review.objects.create(
                user=random.choice(users),
                product=random.choice(products),
                text=fake.text()  # Random text for review
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} reviews'))
