from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.products.models import Category, Product
import random
from faker import Faker

faker = Faker()

class Command(BaseCommand):
    help = 'Populate the database with products'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=50,
            help='Number of products to create'
        )

    def handle(self, *args, **options):
        count = options['count']
        categories = Category.objects.all()
        users = User.objects.all()

        if not categories.exists():
            self.stdout.write(self.style.SUCCESS('No categories found. Please populate categories first.'))

        if not users.exists():
            self.stdout.write(self.style.SUCCESS('No users found. Please ensure there are users in the system.'))

        products = []
        for _ in range(count):
            product = Product(
                added_by=random.choice(users),
                name=faker.unique.word().title(),
                description=faker.text(max_nb_chars=200),
                quantity=random.randint(1, 100),
                is_active=random.choice([True, False]),
                category=random.choice(categories) if categories.exists() else None,
                price=round(random.uniform(10.0, 1000.0), 2)
            )
            products.append(product)
        Product.objects.bulk_create(products)