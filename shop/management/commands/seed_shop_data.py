import random

from django.core.management.base import BaseCommand
from faker import Faker

from shop.models import Product, Customer, Order, OrderItem


class Command(BaseCommand):
    help = 'Create random data'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of each model type to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        for _ in range(total):
            Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                street=fake.street_address(),
                city=fake.city(),
                state=random.choice([i[0] for i in Customer.STATE_CHOICES]),
                postal_code=fake.zipcode(),
                country=random.choice([i[0] for i in Customer.COUNTRY_CHOICES]),
            )

            Product.objects.create(
                name=fake.catch_phrase(),
                price=fake.random_int(min=1000, max=9999, step=1) / 100
            )

        customers = Customer.objects.all()
        products = Product.objects.all()

        for _ in range(total):
            order = Order.objects.create(
                placed_at=fake.past_datetime(start_date="-30d"),
                status=random.choice([i[0] for i in Order.STATUS_CHOICES]),
                customer=random.choice(customers)
            )

            for _ in range(random.randint(1, 5)):  # Let's say an order can contain 1-5 items
                OrderItem.objects.create(
                    product=random.choice(products),
                    order=order,
                    quantity=random.randint(1, 5)
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} each of Customers, Products, Orders!'))
